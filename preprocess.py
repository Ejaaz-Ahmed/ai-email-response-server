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

import pandas as pd
import spacy
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nlp = spacy.load("en_core_web_sm")

# Load dataset
df = pd.read_csv("synthetic_emails.csv")

# Preprocessing function
def preprocess_text(text):
    doc = nlp(text.lower())  # Lowercase and tokenize
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Apply preprocessing
df["clean_body"] = df["body"].apply(preprocess_text)

# 🔹 Add labels (Simple Binary Classification Example)
df["labels"] = df["subject"].apply(lambda x: 1 if "price" in str(x).lower() else 0)

# Save processed dataset
df.to_csv("processed_emails.csv", index=False)
print("✅ Preprocessing complete! Data saved to 'processed_emails.csv'.")
