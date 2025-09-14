# 選擇 Python 3.10 官方 slim 版本
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements 並安裝
COPY requirements.txt .

# 升級 pip 並安裝套件
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案所有檔案
COPY . .

# 容器啟動指令
# 假設你的 FastAPI app 在 main.py 且有 app = FastAPI()
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
