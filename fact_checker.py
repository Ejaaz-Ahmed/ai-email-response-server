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

import wikipediaapi
from googlesearch import search  

def fact_check(statement):
    """Check if a fact is accurate using Wikipedia & Google Search."""
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="MyFactChecker/1.0 (email)",  # 🔹 Set User-Agent
        language="en"
    )
    
    page = wiki_wiki.page(statement)

    # 🔹 First, Try Wikipedia
    if page.exists():
        return f"✅ Verified Fact (Wikipedia): {page.summary[:200]}..."  # Limit output length

    # 🔹 If Wikipedia fails, Try Google Search
    search_results = []
    for result in search(statement, num_results=3):  # Get top 3 search results
        search_results.append(f"🔎 Fact check this link: {result}")

    # 🔹 If Google found links, return them
    if search_results:
        return "\n".join(search_results)

    # 🔹 If Wikipedia & Google fail, return a message
    return "⚠️ No relevant information found online."
