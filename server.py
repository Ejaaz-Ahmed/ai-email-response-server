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

from flask import Flask, request, jsonify
from response_generator import generate_response
from fact_checker import fact_check  # 🔹 Import fact-checking function

app = Flask(__name__)

@app.route("/generate-response", methods=["POST"])
def get_response():
    """API endpoint to generate AI-based email responses with fact-checking."""
    data = request.get_json()
    email_content = data.get("email_content", "")

    if not email_content:
        return jsonify({"error": "Missing 'email_content' in request"}), 400

    ai_response = generate_response(email_content)  # 🔹 Get AI-generated response
    fact_result = fact_check(ai_response)  # 🔹 Verify AI response with fact-checking

    return jsonify({
        "response": ai_response,
        "fact_check": fact_result  # 🔹 Include fact-checking result
    })

if __name__ == "__main__":
    while True:
        email_content = input("📩 Enter your email content (or type 'exit' to quit) and be patient: ")
        if email_content.lower() == "exit":
            print("👋 Exiting the server...")
            break
        ai_response = generate_response(email_content)
        fact_result = fact_check(ai_response)  # 🔹 Fact-check AI response
        print(f"🤖 Jazzy Response: {ai_response}")
        print(f"🕵️ Jazzy Fact Check: {fact_result}\n")
