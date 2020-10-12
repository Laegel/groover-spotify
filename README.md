# Groover Spotify mini webservice

Technology choices:
- PostgreSQL, as it was mandatory;
- FastAPI, as a simple (yet more powerful than Flask) HTTP microframework;
- sqlalchemy, as it plays well with FastAPI;
- Docker, for production-ready images. 

## Use with Docker and Docker Compose

For ease of use, this project is powered by Docker.

It creates a PostgreSQL and a FastAPI container.

### 1) Install Docker and Docker Compose

- [Docker](https://docs.docker.com/get-docker/)

- [Docker Compose](https://docs.docker.com/compose/install/)

Or just follow [this guide](https://websiteforstudents.com/how-to-install-docker-and-docker-compose-on-ubuntu-16-04-18-04/)

### 2) Clone the repository

```sh
git clone git@github.com:Laegel/groover-spotify.git
```

### 3) Spotify app credentials

In docker-compose.yml, replace "XXX" placeholders with the real credentials.

### 4) Run the containers

At the root of the repository, execute:
```sh
docker-compose up -d
```

Latest releases are fetched once at startup then periodically (once every 12 hours) with a cron job. At least, it should have worked but cron jobs and Docker don't seem to work well.
To fetch releases manually, run:

```sh
docker exec -it groover-spotify_backend python -m grooverspotify.fetch_releases
```
