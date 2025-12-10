
docker login ghcr.io -u lole-21 --password-stdin

docker run -p 8501:8501 ghcr.io/lole-21/iris-streamlit:latest
