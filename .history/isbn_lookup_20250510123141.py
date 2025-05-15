import pandas as pd
import re

# Load CSV
df = pd.read_csv("folder_contents_my_audio.csv")


def clean_title(title):
    # Remove file extensions (e.g., .m4b, .mp3, .abs)
    title = re.sub(r"\.(m4b|mp3|abs|jpg|png)$", "", title, flags=re.IGNORECASE)

    # Remove metadata tags (e.g., "Unabridged", "Chapterized")
    title = re.sub(r"\(Unabridged\)|Unabridged|Chapterized",
                   "", title, flags=re.IGNORECASE)

    # Remove extra whitespace and trailing hyphens/dashes
    title = re.sub(r"\s+", " ", title).strip()
    title = re.sub(r"[-–—]\s*$", "", title)  # Trailing dashes

    # Fix common issues (e.g., "Ali Hazelwood - Check & Mate" → "Check & Mate")
    if " - " in title:
        title = title.split(" - ")[-1]  # Keep text after " - "

    # Standardize capitalization (optional)
    title = title.title()  # Capitalize first letters

    return title


df["Title_Clean"] = df["Title"].apply(clean_title)

# Save cleaned data
df.to_csv("cleaned_books.csv", index=False)
