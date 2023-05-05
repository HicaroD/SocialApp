FROM postgres:latest
ENV POSTGRES_PASSWORD example
COPY postgres_db.sql /docker-entrypoint-initdb.d/