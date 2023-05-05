FROM python:latest

ENV NEO4J_BOLT_URL=bolt://neo4j:hicaropassword@neo4j_container:7687

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
