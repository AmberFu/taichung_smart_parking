from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from agents.core import run_agent_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "API is running"}

@app.get("/query")
def query(keyword: str = Query(..., description="地點或查詢指令")):
    result = run_agent_pipeline(keyword)
    return result
