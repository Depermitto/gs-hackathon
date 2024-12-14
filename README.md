# Vulnerability analysis

## Setting up backend

1. Install poetry. One of the options is using `pipx`:

```shell
pipx install poetry
```

2. Setup project files:

```shell
poetry install
```

3. Run webserver:

```shell
poetry run python backend
```

After that, you can access API at `http://127.0.0.1:8000/`


## Setting up frontend
**Attention:** `npm` has to be installed.

```
cd frontend
npm install
npm run dev
```

After that, you can access site at `127.0.0.1:5173`


## Example API:
**Attention:** `docker` has to be installed.

```
docker run --rm -p 5000:5000 erev0s/vampi:latest
curl -X 'GET' 'http://127.0.0.1:5000/createdb' -H 'accept: application/json'
```

After that, you can access the API documentation at `127.0.0.1:5000/ui`
