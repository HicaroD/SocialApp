# SocialApp

SocialApp é um aplicativo mobile simples que possui o intuito de simular uma rede social, como Instagram, mas de forma simples.

A ideia é fazer a utilização de grafos com o auxílio do [Neo4J](https://neo4j.com/) para armazenar os usuários e as relações
entre eles. O usuário terá a possibilidade de dar follow e unfollow em outro usuário.

## Tecnologias utilizadas

- Flutter para desenvolvimento do aplicativo mobile
- Python com FastAPI para criação de uma API para interagir com o banco de dados Neo4J.
- Docker para criar um container para o banco de dados Neo4J.

## Estratégia utilizada

Como eu irei rodar esse aplicativo apenas localmente em meu computador, eu irei apenas rodar a API localmente e utilizar em
meu aplicativo, dessa forma eu poupo esforços de deploy. A minha API rodará no endereço "127.0.0.1:8000".

A minha API irá se comunicar com um banco de dados Neo4J que eu criei dentro de um container Docker e irei me comunicar no
endereço "127.0.0.1:7687". A minha API irá se comunicar com esse banco de dados para eu conseguir extrair as informações
necessárias. A minha API foi feita em FastAPI, o qual é um framework web de Python que torna simples a criação de APIs.

## Licença
Este projeto é licenciado sob a licença MIT. Ver [LICENSE](LICENSE).
