import random

import requests

BASE_URL = "https://api.alquran.cloud/v1"
TOTAL_AYAHS = 6236  # the Quran has 6236 verses in total


def main():
    ayah_number = random.randint(1, TOTAL_AYAHS)
    url = f"{BASE_URL}/ayah/{ayah_number}/quran-uthmani"
    response = requests.get(url, timeout=10)
    data = response.json()

    verse = data["data"]
    print("Verse of the Day:")
    print(verse["text"])


if __name__ == "__main__":
    main()
