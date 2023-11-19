FROM  python:3.9.18-slim
WORKDIR /log_py
ADD . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]