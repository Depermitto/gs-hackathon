from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import injection
import scraper
import scraper.parse_endpoints
from . import auth_check


app = FastAPI()

origins = ["http://localhost:5173", "localhost:5173"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api", tags=["root"])
async def read_root() -> dict:
    return {"title": "API example", "message": "This is the root route of the API"}


def find_vulnerabilites(url, routes) -> dict:
    raport = {}
    raport["vulnerabilities"] = 0

    raport["https"] = auth_check.check_https(url)
    raport["vulnerabilities"] += not raport["https"]

    raport["cookie_secure"] = auth_check.check_cookie_secure(url)
    raport["vulnerabilities"] += not raport["cookie_secure"]

    raport["cookie_permanent"] = not auth_check.check_cookie_timeout(url)
    raport["vulnerabilities"] += raport["cookie_permanent"]

    raport["sql"] = injection.pipeline(url, routes, "injections.txt")
    for sql_raport in raport["sql"]:
        raport["vulnerabilities"] += sql_raport["body_injection"]
        raport["vulnerabilities"] += sql_raport["path_injection"]

    return raport


@app.post("/api/process/file")
async def process_file(file: UploadFile = File(...)) -> dict:
    contents = await file.read()
    base_url, endpoints = injection.parse_endpoints.parse_yaml(contents)
    return find_vulnerabilites(base_url, endpoints)


@app.post("/api/process/scraper")
async def process_scraper(url: str) -> dict:
    base_url, endpoints = scraper.parse_endpoints.scrape_endpoints(url)
    return find_vulnerabilites(base_url, endpoints)
