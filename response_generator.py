"""
🚀 AI Email Response Server with Fact-Checking  
==========================================================
📌 Created by: Ejaz Ahmed  
📅 Year: 2025 
==========================================================

🔹 Description:
This file is part of the AI-powered email response server.  
It integrates AI email responses using Google Gemini AI  
and verifies responses with Wikipedia & Google Search.

🔹 License & Authorization:
This software is **licensed for educational and personal use only**.  
Unauthorized commercial use, reproduction, or distribution is prohibited.  
For permissions, contact the author.

🔹 Copyright Notice:
© 2025 Ejaz Ahmed. All Rights Reserved.
"""

import google.generativeai as genai

# Configure API key
genai.configure(api_key="key")  

def generate_response(email_content):
    """Generate a response using Google's Gemini AI."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(email_content)
    return response.text

# 🔹 Accept user input from the terminal
if __name__ == "__main__":
    email_content = input("📩 Enter your email content: ")
    print("🤖 Jazzy Response:", generate_response(email_content))
