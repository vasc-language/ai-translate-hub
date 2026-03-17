# AI 翻译助手 — 开发过程说明

## 一、项目概述

本项目是一个「AI 翻译助手」，支持输入中文、一键翻译为英文并提取关键词。

- **后端**：Python + FastAPI + OpenAI 兼容 API
- **前端**：React + Vite，Glassmorphism 毛玻璃 UI 风格
- **仓库地址**：https://github.com/vasc-language/ai-translate-hub

---

## 二、开发过程

### Step 1：技术选型讨论

开发前，我让 AI（Claude Code）进行联网搜索，对比了以下技术方案：

| 维度 | 选项 A | 选项 B | 最终选择 |
|------|--------|--------|----------|
| 后端框架 | Flask | FastAPI | **FastAPI**（性能更好、自动生成 API 文档） |
| 大模型 API | DeepSeek | 通义千问 | **OpenAI 兼容 API**（通用性强） |
| 前端框架 | Flutter | React | **React + Vite**（开发速度快） |

### Step 2：后端开发

AI 生成了 FastAPI 后端代码，核心逻辑：
- `POST /translate` 接口接收中文文本
- 调用大模型 API，通过 prompt 要求返回 JSON 格式的翻译结果 + 关键词
- 使用 Pydantic 做请求/响应校验
- 使用 python-dotenv 管理 API 密钥配置

**我的参与**：
- 提供了 API Key 和 Base URL 配置
- 要求使用 Python 虚拟环境（venv）而非全局安装依赖

### Step 3：前端开发

AI 先生成了基础版 React 界面（输入框 + 按钮 + 结果展示），功能跑通后，我使用 UI/UX Pro Max 技能进行了 UI 优化。

**优化前**：纯白背景 + 基础蓝色按钮，视觉效果一般

**优化后**：
- Glassmorphism 毛玻璃风格（backdrop-filter + 半透明卡片）
- 清新 Cyan/Teal 配色方案（主色 #0891b2）
- Plus Jakarta Sans 字体
- 骨架屏加载动画（shimmer 效果）
- Ctrl+Enter 快捷键翻译
- 实时字数统计
- 结果淡入动画
- SVG 图标替代纯文字
- 响应式布局 + 无障碍支持

**我的参与**：
- 决定使用 React 而非 Flutter
- 要求用 UI/UX Pro Max 技能优化界面

### Step 4：测试验证

- 启动后端：`uvicorn main:app --reload`，验证 `/health` 和 `/translate` 接口
- 启动前端：`npm run dev`，在浏览器中测试翻译功能
- 测试了短句、长难句、中英混合等多种输入场景，均正常返回结果

### Step 5：Git 提交与推送

- 初始化 Git 仓库，配置 .gitignore（排除 .env、node_modules、venv 等）
- 安装 GitHub CLI（gh），通过浏览器授权登录
- 创建 GitHub 仓库并推送代码

---

## 三、AI 使用说明

### 使用的 AI 工具

- **Claude Code**（Claude Opus 4.6 模型）— Anthropic 官方 CLI 工具

### 哪些代码是 AI 生成的

| 文件 | AI 生成 | 我的修改 |
|------|---------|----------|
| `backend/main.py` | 100% AI 生成 | 提供 API 配置参数 |
| `backend/requirements.txt` | 100% AI 生成 | 无 |
| `backend/.env` | AI 生成模板 | 我提供了实际的 API Key |
| `frontend/src/App.jsx` | 100% AI 生成 | 无 |
| `frontend/src/App.css` | 100% AI 生成 | 无 |
| `frontend/index.html` | AI 生成 | 无 |
| `README.md` | 100% AI 生成 | 无 |

**总结**：所有代码均由 AI 生成，我的工作主要是：
1. 确定技术选型方向
2. 提供 API Key 等配置信息
3. 提出优化需求（虚拟环境、UI 美化）
4. 测试验证并确认功能正常

### 遇到的问题及解决方式

| 问题 | 解决方式 |
|------|----------|
| Vite 创建了 vanilla 模板而非 React | 让 AI 重新用 `--template react` 创建 |
| Python 路径找不到（pip 命令不可用） | AI 自动搜索 Python 安装路径，使用完整路径执行 |
| 全局安装依赖不规范 | 我提出使用虚拟环境，AI 创建了 venv |
| curl 在 Git Bash 中发送中文 JSON 失败 | AI 改用 printf 管道传递请求体 |
| Git 提交缺少用户配置 | 我提供了 GitHub 用户名和邮箱 |
| gh CLI 未安装，winget 在 Git Bash 中不可用 | AI 下载 zip 版本手动解压安装 |
| gh auth login 流程被中断 | 通过浏览器 device code 方式重新授权 |

---

## 四、运行说明

### 环境要求

- Python 3.10+
- Node.js 18+

### 启动后端

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

后端运行在 http://localhost:8000

### 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端运行在 http://localhost:5173

### 配置 API

在 `backend/.env` 中配置：

```env
OPENAI_API_KEY=你的API密钥
OPENAI_BASE_URL=你的API地址
OPENAI_MODEL=模型名称
```

支持任何 OpenAI 兼容的 API（OpenAI、DeepSeek、通义千问等）。
