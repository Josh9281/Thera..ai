"""
This agent is responsible for getting weather data from the open meteo API.
"""
from uagents import Agent, Context
import json
import requests
from datetime import datetime

agent = Agent()

URL = "https://api.open-meteo.com/v1/forecast?"
# no API key needed

MY_DATA = {                 # New York City
    "latitude": "40.7128",
    "longitude": "-74.0060",
    "hour": 15
}

def get_weather(ctx) -> dict or None:
    """Function to get the data from the open meteo API"""
    latitude = MY_DATA["latitude"]
    longitude = MY_DATA["longitude"]
    url = (
        URL
        + f"latitude={latitude}&longitude={longitude}"
        + "&hourly=temperature_2m&forecast_days=1"
    )
    current_date = datetime.utcnow().date().isoformat()
    cached_data = ctx.storage.get("last_request")
    if cached_data:
        data = json.loads(cached_data)
        if data["date"] == current_date and data["url"] == url:
            return data["response"]

    response = requests.get(url=url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        ctx.storage.set("last_request",
            json.dumps({"date": current_date, "url": url, "response": data})
        )
        return data
    else:
        ctx.logger.info(f"Status {response.status_code}: {response.text}")
    return None


@agent.on_event("startup")
async def query_data(ctx: Context):
    """Query weather data and logs the local temperature at a specified hour"""
    data = get_weather(ctx)
    time = MY_DATA["hour"]
    if data:
        ctx.logger.info(f"Your local temperature at {time} is {data['hourly']['temperature_2m'][time]}°C.")

def get_last_log(ctx) -> str:
    """Retrieve the last logged message from the context storage"""
    return ctx.storage.get("last_log", "No log available.")
  
if __name__ == "__main__":
    agent.run()
