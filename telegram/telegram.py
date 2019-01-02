#make a telegram
import requests
import json
from pprint import pprint
import os
from bs4 import BeautifulSoup


token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
update = requests.get(url).json()
# chat_id = 675957715
chat_id = update["result"][0]["message"]["chat"]["id"]

method_name = "sendmessage"

req = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(req, "html.parser")
rank = soup.select_one("#KOSPI_now").text
# allim = ("코스피는 ")

msg = f"{rank}"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"
print(msg_url)
print(requests.get(msg_url))