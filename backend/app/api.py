from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import injection
from . import auth_check


app = FastAPI()

origins = ["http://localhost:3000", "localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "This is the root route of the API"}


@app.post("/scan")
async def scan() -> dict:
    yaml_path = "example.yaml"
    url, _ = injection.parse_endpoints.parse_yaml(yaml_path)

    raport = {}
    raport["vulnerabilities"] = 0

    raport["https"] = auth_check.check_https(url)
    raport["vulnerabilities"] += not raport["https"]

    raport["cookie_secure"] = auth_check.check_cookie_secure(url)
    raport["vulnerabilities"] += not raport["cookie_secure"]

    raport["cookie_permanent"] = not auth_check.check_cookie_timeout(url)
    raport["vulnerabilities"] += raport["cookie_permanent"]

    raport["sql"] = injection.pipeline(yaml_path, "injections.txt")
    for sql_raport in raport["sql"]:
        raport["vulnerabilities"] += sql_raport["body_injection"]
        raport["vulnerabilities"] += sql_raport["path_injection"]

    return raport
