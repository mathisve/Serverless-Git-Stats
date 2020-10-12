from bs4 import BeautifulSoup
import json
import os

import requests

def scrape(link):
    resp = requests.get(link)
    days = BeautifulSoup(resp.text, "html.parser").find_all("rect")

    jsonObj = {"user": "Mathisco-01", "total": 0, "days": []}
    for day in days:
        d = {"count": int(day["data-count"]),
             "date":  day["data-date"]}
        jsonObj["days"].append(d)
        jsonObj["total"] += d["count"]

    return jsonObj

def handler(event, context):
    # Hardcoded URL so users can't use your lambda function for their own profiles!
    link = os.environ["LINK"]
    return scrape(link)
