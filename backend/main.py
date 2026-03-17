import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="AI 翻译助手", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")


class TranslateRequest(BaseModel):
    text: str


class TranslateResponse(BaseModel):
    translation: str
    keywords: list[str]


@app.post("/translate", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text 不能为空")

    prompt = (
        "你是一个专业翻译助手。请将以下中文翻译成英文，并提取 3-5 个关键词。\n"
        "严格按照以下 JSON 格式返回，不要包含任何其他内容：\n"
        '{"translation": "英文翻译", "keywords": ["关键词1", "关键词2", "关键词3"]}\n\n'
        f"中文内容：{req.text}"
    )

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        content = resp.choices[0].message.content.strip()
        # 处理可能的 markdown 代码块包裹
        if content.startswith("```"):
            content = content.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        result = json.loads(content)
        return TranslateResponse(
            translation=result["translation"],
            keywords=result["keywords"],
        )
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="模型返回格式异常，请重试")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "ok"}
