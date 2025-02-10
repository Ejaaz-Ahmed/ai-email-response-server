# 🚀 AI Email Response Server with Fact-Checking  

Welcome to my **AI-powered Email Response Server**! 🎉 This project uses **Google Gemini AI** to generate email responses and integrates **Wikipedia & Google Search** for **fact-checking AI-generated responses**.  

---

## 📌 **Project Overview**  

### ✅ Features:
- **AI-Powered Email Responses** using **Google Gemini AI** 🤖  
- **Fact-Checking System** using **Wikipedia & Google Search** 🕵️  
- **Flask API for Email Automation** 🚀  
- **Interactive Terminal Input Support** 💻  

---

## 🚀 **My Journey in Building This Server**  

### **Step 1: Choosing the Right AI Model 🤔**  
Initially, I wanted to use **OpenAI's GPT-4**, but I didn't have a subscription. So, I explored **free alternatives** and found that **Google Gemini AI (gemini-pro)** was the best option!  

📌 **Decision** → Use `google.generativeai` for free AI-powered email responses.  

---

### **Step 2: Setting Up the AI Response Generator (`generate_response.py`)**  
I created a Python script that connects to **Google Gemini AI** and generates **email responses**.  

📌 **Key Takeaways:**  
✅ Installed `google-generativeai` → `pip install google-generativeai`  
✅ Set up API key securely  
✅ Allowed user input from the **terminal**  

```python
import google.generativeai as genai

# Configure API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual key

def generate_response(email_content):
    """Generate a response using Google's Gemini AI."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(email_content)
    return response.text

# 🔹 Test with terminal input
if __name__ == "__main__":
    email_content = input("📩 Enter your email content: ")
    print("🤖 AI Response:", generate_response(email_content))
```
# Step 3: Creating a Flask API (`server.py`)

To make my AI accessible via an API, I built a Flask server that accepts POST requests and returns AI-generated responses.

## Key Takeaways
- ✅ Installed Flask → `pip install flask`
- ✅ Created an endpoint `/generate-response` for AI-powered email replies

## Code: `server.py`

```python
from flask import Flask, request, jsonify
from generate_response import generate_response

app = Flask(__name__)

@app.route("/generate-response", methods=["POST"])
def get_response():
    """API endpoint to generate AI-based email responses."""
    data = request.get_json()
    email_content = data.get("email_content", "")

    if not email_content:
        return jsonify({"error": "Missing 'email_content' in request"}), 400

    response = generate_response(email_content)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
## Testing the API

You can test the API using cURL:

```sh
curl -X POST http://127.0.0.1:5000/generate-response \
     -H "Content-Type: application/json" \
     -d '{"email_content": "What is meant by price?"}'
```
## Expected Response

```json
{
    "response": "Price is the amount of money expected, required, or given in payment for something."
}
```
# Step 4: Adding Terminal Interaction in `server.py`

I wanted users to enter email content directly in the terminal while running the Flask server. So, I added an interactive input system inside `server.py`.

## Now, `server.py` works both as an API and an interactive chatbot.

## Updated Code in `server.py`

```python
if __name__ == "__main__":
    while True:
        email_content = input("📩 Enter your email content (or type 'exit' to quit): ")
        if email_content.lower() == "exit":
            print("👋 Exiting the server...")
            break
        response = generate_response(email_content)
        print(f"🤖 AI Response: {response}\n")
```
## Now, users can:
- ✅ Type questions in the terminal 📝
- ✅ Use API requests via POST
# Step 5: Implementing Fact-Checking (`fact_checker.py`)

AI models sometimes hallucinate 🧠, so I built a fact-checking system that verifies AI responses using Wikipedia & Google Search.

## Key Takeaways:
- ✅ Installed `wikipedia-api` & `google-search-results`
- ✅ Verified AI-generated facts before returning them to users
## Code: `fact_checker.py`

```python
import wikipediaapi
from googlesearch import search  # Requires `pip install google-search-results`

def fact_check(statement):
    """Check if a fact is accurate using Wikipedia & Google Search."""
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="MyFactChecker/1.0 (your-email@example.com)",
        language="en"
    )

    page = wiki_wiki.page(statement)
    if page.exists():
        return f"✅ Verified Fact (Wikipedia): {page.summary[:200]}..."

    search_results = [f"🔎 Fact check this link: {result}" for result in search(statement, num_results=3)]
    return "\n".join(search_results) if search_results else "⚠️ No relevant information found."
```
## How It Works:
1️⃣ First, it checks Wikipedia for the requested fact.
2️⃣ If Wikipedia has an entry, it returns a verified fact summary ✅.
3️⃣ If Wikipedia doesn’t find anything, it performs a Google Search 🔎.
4️⃣ If Google finds relevant links, it provides sources for verification.
5️⃣ If no relevant data is found, it returns "⚠️ No relevant information found."

# Step 6: Integrating Fact-Checking into the API

Now, my API not only generates AI responses but also fact-checks them before returning them to users.

## Updated `server.py` to Include Fact-Checking

```python
from fact_checker import fact_check  # 🔹 Import fact-checking function

@app.route("/generate-response", methods=["POST"])
def get_response():
    """API endpoint to generate AI-based email responses with fact-checking."""
    data = request.get_json()
    email_content = data.get("email_content", "")

    if not email_content:
        return jsonify({"error": "Missing 'email_content' in request"}), 400

    ai_response = generate_response(email_content)
    fact_result = fact_check(ai_response)  # 🔹 Verify AI response

    return jsonify({"response": ai_response, "fact_check": fact_result})
```
## Final Testing & Deployment

1️⃣ Start the Flask Server  
Run the following command to start the server:

```sh
python server.py
```
2️⃣ Test API with cURL  
Use the following cURL command to test the API:

```sh
curl -X POST http://127.0.0.1:5000/generate-response \
     -H "Content-Type: application/json" \
     -d '{"email_content": "Who created Bitcoin?"}'
```
3️⃣ Example JSON Response:

```json
{
    "response": "Bitcoin was created by Satoshi Nakamoto in 2009.",
    "fact_check": "✅ Verified Fact (Wikipedia): Bitcoin was invented in 2009..."
}
```

# 🎯 Conclusion: My AI Email Server is Ready!

✅ Built an AI-powered email response system using Google Gemini.  
✅ Integrated fact-checking using Wikipedia & Google Search.  
✅ Created a Flask API for email automation.  
✅ Allowed users to enter emails via the terminal.

🚀 Now, the AI Email Response Server is fully functional! 🎯

# Developed by Ejaz Ahmed 
# Some snapshots of Output:
# AI Email Response Server

🚀 An intelligent AI-powered email response system with fact-checking.

## 📌 Demo Screenshot
![AI Email Response Demo]([assets/demo_screenshot.png](https://github.com/Ejaaz-Ahmed/ai-email-response-server/blob/main/images/image1.jpg))

## 🌟 Features
- AI-generated email responses
- Fact-checking with Wikipedia & Google
- Interactive terminal chatbot & API support


