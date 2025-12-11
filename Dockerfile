FROM python:3.10-slim

LABEL authors="piotr"
LABEL org.opencontainers.image.source="https://github.com/lole-21/ASI"
LABEL org.opencontainers.image.description="Iris Streamlit Docker image"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

CMD ["streamlit", "run", "app/app.py"]


#docker build -t iris-streamlit .
#docker run -p 8501:8501 iris-streamlit

