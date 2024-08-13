# WhatsApp AI Text-to-Image Chatbot

**Description:**

This project implements a captivating WhatsApp chatbot that empowers users to generate unique images based on their textual descriptions. It seamlessly integrates the following powerful technologies:

- **Vonage Messaging API:** Facilitates seamless communication between the chatbot and users via WhatsApp, enabling a familiar and convenient interaction channel.
- **OpenAI DALL-E 2 API:** Leverages the cutting-edge capabilities of DALL-E 2, a state-of-the-art generative AI model, to craft stunning and diverse images from user-provided prompts.

**Key Features:**

- **Prompt-driven Image Generation:** Utilizes user-submitted text prompts to guide the creation of captivating images through DALL-E 2, fostering creativity and exploration.
- **Intuitive WhatsApp Interface:** Leverages WhatsApp, a widely used messaging platform, to provide a user-friendly and accessible interaction channel.
- **Seamless Integration:** Efficiently integrates Vonage and OpenAI APIs, ensuring a smooth and streamlined user experience.

**Getting Started:**

1. **Prerequisites:**
   - A Vonage account and API credentials (API key and API secret)
   - An OpenAI account and API key
   - Python 3.x and required libraries (e.g., `vonage`, `openai`)
2. **Installation:**
   - Clone the repository: `git clone https://github.com/adejumoridwan/WhatsApp-AI-Text-To-Image-Chatbot.git`
   - Navigate to the project directory: `cd whatsapp-ai-text-to-image-generator`
   - Install dependencies: `pip install -r requirements.txt`
3. **Configuration:**
   - Create a `.env` file at the root of the project.
   - Add environment variables:
      - `OPENAI_API_KEY="<your-open-ai-api-key>"`
      - `VONAGE_API_KEY="<your-vonage-api-key>"`
      - `VONAGE_API_SECRET="<your-vonage-api-secret>"`
      - `VONAGE_NUMBER="<your-vonage-number>"`
      - `WHATSAPP_NUMBER="<your-whatsapp-number>"` (replace with your Vonage WhatsApp sandbox number)
4. **Run the application:**
   - Execute the script: `uvicorn main:app --reload`