from bs4 import BeautifulSoup
import json
import os

import logging

import requests

def scrape(link, granularity):
    resp = requests.get(link)
    days = BeautifulSoup(resp.text, "html.parser").find_all("rect")

    jsonObj = {"user": "Mathisco-01",
                "total": 0,
                "data": {"date": [],
                        "count": []
                        }
                }

    c = 0
    for i in range(len(days)):
        c += int(days[i]["data-count"])
        if i % granularity == 0:
            jsonObj["data"]["date"].append(days[i]["data-date"])
            jsonObj["data"]["count"].append(c)

    jsonObj["total"] = c

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        'body': json.dumps(jsonObj)
    }

def handler(event, context):
    jsobBody = json.loads(event["body"])

    try:
        if jsobBody["link"] in os.environ["LINK"].split(","):
            link = jsobBody["link"]
        else:
            link = os.environ["LINK"]

        granularity = int(jsobBody["granularity"])

        return scrape(link, granularity)
    except Exception as e:
        logging.warning(e)
        return e
        return {
            'statusCode': 400,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True
            },
        }

if __name__ == "__main__":
    link = "https://github.com/users/Mathisco-01/contributions"
    granularity = 10
    resp = scrape(link, granularity)

    print(resp)
