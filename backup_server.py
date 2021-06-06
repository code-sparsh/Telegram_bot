from bot import telegram_chatbot
import requests
import re

bot = telegram_chatbot("config.cfg")

update_id = 438579143
baseURL = "amazon.in/"
affiliate_tag = "Dheeraj21"

def newReferURL(pcode):
    return baseURL+pcode+"?tag="+affiliate_tag


def filterText(msg):
    pCode=""
    start = msg.find("amzn.to")

    start = msg.find(baseURL)
    if start != -1:
        #Regular expression to extract the product code. Adjust if different URL schemes are found.
        m = re.search(r'(?:dp\/[\w]*)|(?:gp\/product\/[\w]*)',msg[start:].split(" ")[0])
        if m != None:
            pCode = m.group(0)

    return newReferURL(pCode)


def make_reply(msg2):
    reply = None
    if msg2 is not None:
        reply = filterText(msg2)
    return reply



while True:

    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_photo(reply,message, from_)
