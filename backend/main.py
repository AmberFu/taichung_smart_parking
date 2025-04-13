# 📁 backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from parking_agents.core import run_agent_pipeline
# from parking_agents.mcp_server import mcp_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(mcp_router, prefix="/mcp")

@app.get("/ping")
def ping():
    return {"message": "API is running"}

@app.get("/query")
def query(keyword: str):
    return run_agent_pipeline(keyword)


# # 📁 backend/parking_agents/__init__.py
# # 空的初始化檔


# # 📁 backend/parking_agents/core.py
# from parking_agents.mcp_client import mcp_client

# def run_agent_pipeline(user_query: str):
#     location = mcp_client.call("extract_location", {"query": user_query})
#     parking_data = mcp_client.call("fetch_taichung_parking", {})
#     nearby = mcp_client.call("search_nearby", {
#         "lat": location["lat"],
#         "lng": location["lng"],
#         "parking": parking_data
#     })
#     return mcp_client.call("respond_summary", {"nearby": nearby})


# # 📁 backend/parking_agents/mcp_client.py
# from openai import OpenAI
# from parking_agents.tools import extract_location, fetch_taichung_parking, search_nearby, respond_summary

# class LocalMCPClient:
#     def __init__(self):
#         self.tools = {
#             "extract_location": extract_location.run,
#             "fetch_taichung_parking": fetch_taichung_parking.run,
#             "search_nearby": search_nearby.run,
#             "respond_summary": respond_summary.run
#         }

#     def call(self, tool_name: str, kwargs: dict):
#         return self.tools[tool_name](**kwargs)

# mcp_client = LocalMCPClient()


# # 📁 backend/parking_agents/mcp_server.py
# from fastapi import APIRouter, Request
# from openai import OpenAI
# from parking_agents.tools import extract_location, fetch_taichung_parking, search_nearby, respond_summary

# mcp_router = APIRouter()

# @mcp_router.post("/tool_call")
# async def mcp_tool_handler(req: Request):
#     body = await req.json()
#     tool_name = body.get("tool")
#     args = body.get("args", {})
#     if tool_name == "extract_location":
#         return extract_location.run(**args)
#     elif tool_name == "fetch_taichung_parking":
#         return fetch_taichung_parking.run()
#     elif tool_name == "search_nearby":
#         return search_nearby.run(**args)
#     elif tool_name == "respond_summary":
#         return respond_summary.run(**args)
#     else:
#         return {"error": "Unknown tool"}


# # 📁 backend/parking_agents/tools/extract_location.py
# def run(query: str):
#     if "勤美" in query:
#         return {"lat": 24.1521, "lng": 120.6649}
#     return {"lat": 24.1477, "lng": 120.6736}  # 台中市政府作為 fallback


# # 📁 backend/parking_agents/tools/fetch_taichung_parking.py
# def run():
#     return [{"name": "台中市停車場A", "lat": 24.1478, "lng": 120.6737, "surplus": 5}]


# # 📁 backend/parking_agents/tools/search_nearby.py
# def run(lat: float, lng: float, parking: list):
#     return [p for p in parking if abs(p["lat"] - lat) < 0.01 and abs(p["lng"] - lng) < 0.01]


# # 📁 backend/parking_agents/tools/respond_summary.py
# def run(nearby: list):
#     return {
#         "message": f"附近找到 {len(nearby)} 個停車點，有空位的有：" + ", ".join([p["name"] for p in nearby if p["surplus"] > 0])
#     }
