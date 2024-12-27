import os
import json
import csv

# Define constants
JSON_FILE = "./metadata.json"  # JSON file with metadata
CSV_FILE = "./metadata_output.csv"  # Output CSV file
MAX_WORDS = 49  # Maximum number of words allowed in the keywords

# Load the JSON data
with open(JSON_FILE, "r") as file:
    metadata = json.load(file)

# Function to process keywords and ensure max word count
def process_keywords(keywords):
    total_words = sum(len(keyword.split()) for keyword in keywords)  # Calculate total word count
    # Keep removing the last keyword until total word count is <= MAX_WORDS
    while total_words > MAX_WORDS and keywords:
        keywords.pop()  # Remove the last keyword
        total_words = sum(len(keyword.split()) for keyword in keywords)  # Recalculate total word count
    return keywords

# Open the CSV file in write mode
with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Filename", "Title", "Keywords", "Category"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    # Write the header row
    writer.writeheader()

    # Loop through metadata and write each entry to the CSV file
    for entry in metadata:
        # Extract information from the entry
        filename = entry.get("imageFile", "Unknown")  # Default to "Unknown" if missing
        title = entry.get("title", "Untitled")  # Default title if missing
        keywords_list = entry.get("keywords", [])
        category = entry.get("category", "Uncategorized")  # Default category if missing

        # Process keywords to ensure max 49 words
        processed_keywords = process_keywords(keywords_list)

        # Convert processed keywords to lowercase and join into a comma-separated string
        keywords_str = ", ".join([keyword.lower() for keyword in processed_keywords])

        # Write the data to CSV
        writer.writerow({
            "Filename": filename,
            "Title":  title ,
            "Keywords": keywords_str,
            "Category": category
        })

print(f"CSV file '{CSV_FILE}' has been created!")
