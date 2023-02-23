from starlette.middleware.cors import CORSMiddleware  # 追加
from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ["SLACK_TOKEN"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def getAPI(url, params):
    headers = {"Authorization": "Bearer "+TOKEN}
    return requests.get(url, headers=headers, params=params)


@app.get("/")
async def index():
    return {"message": "Hello World!!"} 


@app.get("/channel")
async def index():
    url = "https://slack.com/api/conversations.list"
    params = {}
    r = getAPI(url, params)
    result = r.json()["channels"]
    return {"message": result}
