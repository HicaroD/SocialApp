FROM mysql:latest

# TODO: create database from file entrypoint

EXPOSE 3306
CMD [ "mysqld" ]