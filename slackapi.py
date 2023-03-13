import requests
import os
from dotenv import load_dotenv
load_dotenv()
USER_TOKEN = os.environ["USER_TOKEN"]
BOT_TOKEN = os.environ["BOT_TOKEN"]


def getAPI(url, params):
    headers = {"Authorization": "Bearer "+USER_TOKEN}
    return requests.get(url, headers=headers, params=params)


def getTeamInfo():
    url = "https://slack.com/api/team.info"
    params = {}
    headers = {"Authorization": "Bearer "+BOT_TOKEN}
    r = requests.get(url, headers=headers, params=params)
    result = r.json()["team"]
    return result


def getChannelList():
    url = "https://slack.com/api/conversations.list"
    params = {}
    r = getAPI(url, params)
    result = r.json()["channels"]
    return result


def getMessages(channelID,):
    url = "https://slack.com/api/conversations.history"
    params = {
        "channel": channelID,
        # "oldest" : oldest,
        # "latest" : latest,
        # "limit" : limit,
        # "inclusive": inclusive,
    }
    r = getAPI(url, params)
    result = r.json()["messages"]
    return result


def getReplies(channelID, ts):
    url = "https://slack.com/api/conversations.replies"
    params = {
        "channel": channelID,
        "ts": ts
    }
    r = getAPI(url, params)
    result = r.json()["messages"]
    return result


def getMembers(channelID):
    url = "https://slack.com/api/conversations.members"
    params = {
        "channel": channelID,
        # "oldest" : oldest,
        # "latest" : latest,
        # "limit" : limit,
        # "inclusive": inclusive,
    }
    r = getAPI(url, params)
    result = r.json()["members"]
    return result


def getMemberList(channels):
    url = "https://slack.com/api/conversations.members"
    members = []
    for channel in channels:
        params = {
            "channel": channel["id"]
        }
        r = getAPI(url, params)
        if "members" in r.json().keys():
            m = r.json()["members"]
        else:
            m = []
        members.append({"id": channel["id"], "members":  m})
    return {members[i]["id"]: members[i]["members"] for i in range(len(members))}


def getUserList():
    url = "https://slack.com/api/users.list"
    params = {}
    r = getAPI(url, params)
    result = r.json()["members"]
    return result


def getEmoji():
    url = "https://slack.com/api/emoji.list"
    params = {}
    r = getAPI(url, params)
    result = r.json()["emoji"]
    return result
