from fastapi import FastAPI, Request,Form
from utilis import send_message, create_image
from dotenv import load_dotenv
import logging


load_dotenv()

app = FastAPI(debug=True)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/message")
async def message(request: Request):
    try:
        form_data = await request.json()
        message = form_data["text"]

        url_image = create_image(message)
        send_message(url_image)
        logger.info("Message sent")
    except Exception as e:
        logger.error("Error sending message")

    return ""
