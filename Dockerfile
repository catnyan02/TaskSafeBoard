FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2023-04-17
COPY main.py .
EXPOSE 8000
ENTRYPOINT ["python", "main.py"]