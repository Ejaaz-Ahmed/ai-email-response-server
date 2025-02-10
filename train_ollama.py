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

from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split
import os


os.environ["OMP_NUM_THREADS"] = "1"  
os.environ["MKL_NUM_THREADS"] = "1"

# Load dataset
df = pd.read_csv("processed_emails.csv")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenization function (Ensures 'labels' are included)
def tokenize_function(example):
    return {
        **tokenizer(example["clean_body"], truncation=True, padding="max_length", max_length=64),
        "labels": example["labels"],  
    }

# 🔹 Split dataset into training (80%) and evaluation (20%)
train_df, eval_df = train_test_split(df, test_size=0.2, random_state=42)

# Convert to Hugging Face Dataset format
train_dataset = Dataset.from_pandas(train_df)
eval_dataset = Dataset.from_pandas(eval_df)

# Apply tokenization
train_dataset = train_dataset.map(tokenize_function, batched=True)
eval_dataset = eval_dataset.map(tokenize_function, batched=True)

# Force CPU mode
device = torch.device("cpu")

# Load model
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2).to(device)


# 🔹 Optimize training for low RAM usage
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,  # 🔹 Keep batch size small
    per_device_eval_batch_size=1,
    num_train_epochs=1,  # 🔹 Reduce epochs to prevent long training
    eval_strategy="no",  # 🔹 Disable evaluation to save memory
    save_strategy="no",  # 🔹 Disable saving to prevent slow disk writes
    logging_steps=200,  # 🔹 Log less frequently
    disable_tqdm=True,  # 🔹 Hide progress bar
    gradient_accumulation_steps=4,  # 🔹 Reduce CPU load by updating weights every 4 steps
)


# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Train model
print("🚀 Training started...")
trainer.train()
print("✅ Training complete!")

# Save trained model
trainer.save_model("./results/trained_model")
print("✅ Model saved in './results/trained_model'")
