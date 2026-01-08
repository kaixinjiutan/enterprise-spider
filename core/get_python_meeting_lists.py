import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.encoding="utf-8"

html = response.text

soup = BeautifulSoup(html, "html.parser")
events = soup.select("ul.list-recent-events li")
result = []

for event in events:
    title = event.find("h3").get_text(strip=True)
    time = event.find("time").get_text(strip=True)
    location = event.find("span", class_="event-location").get_text(strip=True)
    link = event.find("a")["href"]
    if link.startswith("http"):
        link = link
    else:
        link = "https://www.python.org" + link

    result.append({
        "title": title,
        "time": time,
        "location": location,
        "link": link
    })
for item in result:
    print(item)

def validate_event(event):
    assert event["title"]
    assert event["time"]
    assert event["location"]
    assert event["link"].startswith("https://")

for e in result:
    validate_event(e)
