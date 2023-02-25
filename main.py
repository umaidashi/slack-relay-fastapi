from starlette.middleware.cors import CORSMiddleware  # 追加
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from slackapi import getChannelList, getMemberList, getMessages, getReplies, getUserList, getMembers, getTeamInfo


app = FastAPI(default_response_class=JSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def index():
    return {"message": "Hello World!!"}


@app.get("/team")
async def index():
    team = getTeamInfo()
    return {
        "team": team
    }


@app.get("/channel")
async def index():
    channels = getChannelList()
    return {
        "channels": channels
    }


@app.get("/users")
async def index():
    users = getUserList()
    return {
        "users": users
    }


@app.get("/channel/{channelID}")
async def index(channelID: str):
    messages = getMessages(channelID)
    members = getMembers(channelID)
    return {
        "messages": messages,
        "members": members
    }


@ app.get("/channel/{channelID}/{ts}")
async def index(channelID: str, ts: str):
    replies = getReplies(channelID, ts)
    return {
        "replies": replies,
    }
