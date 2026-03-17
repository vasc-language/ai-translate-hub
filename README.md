# AI 翻译助手

输入中文，一键翻译为英文并提取关键词。

## 技术栈

- **后端**：Python + FastAPI + OpenAI 兼容 API
- **前端**：React + Vite

## 项目结构

```
ai-translate-hub/
├── backend/
│   ├── main.py           # FastAPI 服务，/translate 接口
│   ├── requirements.txt  # Python 依赖
│   └── .env              # API 配置（需自行配置）
├── frontend/
│   └── src/
│       ├── App.jsx       # 翻译界面组件
│       ├── App.css       # 样式
│       └── main.jsx      # 入口
└── README.md
```

## 运行说明

### 1. 启动后端

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

后端运行在 http://localhost:8000，API 文档在 http://localhost:8000/docs

### 2. 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端运行在 http://localhost:5173

### 3. 使用

1. 打开浏览器访问 http://localhost:5173
2. 在输入框中输入中文内容
3. 点击「翻译」按钮
4. 查看英文翻译结果和关键词

## API 接口

### POST /translate

**请求：**

```json
{
  "text": "要翻译的中文内容"
}
```

**返回：**

```json
{
  "translation": "英文翻译结果",
  "keywords": ["关键词1", "关键词2", "关键词3"]
}
```

## 配置说明

在 `backend/.env` 中配置你的 API：

```env
OPENAI_API_KEY=你的API密钥
OPENAI_BASE_URL=你的API地址
OPENAI_MODEL=模型名称
```

支持任何 OpenAI 兼容的 API（OpenAI、DeepSeek、通义千问等）。
