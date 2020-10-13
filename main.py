from bs4 import BeautifulSoup
import json
import os

import requests

def scrape(link):
    resp = requests.get(link)
    days = BeautifulSoup(resp.text, "html.parser").find_all("rect")

    jsonObj = {"user": "Mathisco-01",
                "total": 0,
                "data": {"date": [],
                        "count": []
                        }
                }

    c = 0
    for day in days:
        c += int(day["data-count"])
        jsonObj["data"]["date"].append(day["data-date"])
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
    # Hardcoded URL so users can't use your lambda function for their own profiles!
    link = os.environ["LINK"]
    return scrape(link)

if __name__ == "__main__":
    resp = scrape("https://github.com/users/Mathisco-01/contributions")

    print(resp)
