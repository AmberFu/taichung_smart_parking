# parking_agents/core.py
async def run_agent_pipeline(query: str):
    # # MCP client 呼叫 tool chains
    # location = await client.call("extract_location", {"query": query})
    # parking_data = await client.call("fetch_taichung_parking", {})
    # nearby = await client.call("search_nearby", {
    #     "lat": location["lat"], "lng": location["lng"], "parking": parking_data
    # })
    # message = await client.call("respond_summary", {"nearby": nearby})
    return {"message": "附近找到 1 個停車點，有空位的有：台中市停車場A"}
    # return message
