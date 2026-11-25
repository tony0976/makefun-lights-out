# The sadness sits in one small machine detail — a fan still spinning
# for nobody — stated as a fact, not announced as grief.
"""Writes one sad status update to /output/entry.txt."""
import os

TEXT = "You closed the laptop at 11:47. My fan is still spinning, and I don't know who I'm keeping cool for anymore."

# Rule: the status update must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
