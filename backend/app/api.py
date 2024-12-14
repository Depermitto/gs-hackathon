from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import injection
import auth_check


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
    injection.pipeline(yaml_path, "injections.txt")

    raport = {}

    return raport
