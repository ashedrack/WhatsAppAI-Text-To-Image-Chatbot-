import requests
import logging
import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(image):
    try:
        url = "https://messages-sandbox.nexmo.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        auth = (os.environ.get("API_KEY"), 
                os.environ.get("API_SECRET"))
        payload = {
            "message_type": "image",
            "image": {
                "url": image
            },
            "to": os.environ.get("WHATSAPP_NUMBER"),
            "from": os.environ.get("VONAGE_NUMBER"),
            "channel": "whatsapp"
        }
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        logger.info("Message sent")
    except Exception as e:
        logger.error("Error sending message")

def create_image(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='512x512'
    )
    image_url = response['data'][0]['url']
    return image_url
 

