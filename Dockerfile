FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-2023-04-17
RUN pip install psutil
RUN apt-get update && apt-get install spass
COPY main.py .
COPY example.p .
EXPOSE 8000
ENTRYPOINT ["python", "main.py"]