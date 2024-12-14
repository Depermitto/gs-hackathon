from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api", tags=["root"])
async def read_root() -> dict:
    return {
        "title": "API example",
        "message": "This is the root route of the API"
    }


@app.post("/api/process")
async def process_file(file: UploadFile = File(...)):
    contents = await file.read()

    # Example processing (e.g., return the file name and size)
    result = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }
    print(result)

    return {
        "errors": {
            "message": "File processed successfully",
            "code": 200
        }
    }
