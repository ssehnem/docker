FROM python:3.13-slim
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn
RUN pip install -r requirements.txt
EXPOSE 8000
COPY app/main.py main.py
CMD ["python", "main.py", "uvicorn", "--host", "--port", "8000"]