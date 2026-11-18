"""
Verse of the Day
Shows a random verse (ayah) of the Quran in Arabic, with an English
or Urdu translation, using the free AlQuran Cloud API.
API docs: https://alquran.cloud/api
"""

import random
import sys

import requests

BASE_URL = "https://api.alquran.cloud/v1"
TOTAL_AYAHS = 6236  # the Quran has 6236 verses in total

# Edition codes used by the API
ARABIC_EDITION = "quran-uthmani"
TRANSLATIONS = {
    "1": ("English", "en.sahih"),      # Saheeh International
    "2": ("Urdu", "ur.jalandhry"),     # Fateh Muhammad Jalandhry
}


def choose_language():
    """Ask the user which translation they want."""
    print("Choose a translation:")
    for key, (name, _) in TRANSLATIONS.items():
        print(f"  {key}. {name}")
    choice = input("Enter 1 or 2: ").strip()
    if choice not in TRANSLATIONS:
        print("Invalid choice, using English.")
        choice = "1"
    return TRANSLATIONS[choice]


def get_verse(ayah_number, translation_edition):
    """Fetch one verse in Arabic + the chosen translation.

    Returns a list of two ayah dictionaries, or None if something went wrong.
    """
    url = f"{BASE_URL}/ayah/{ayah_number}/editions/{ARABIC_EDITION},{translation_edition}"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        print("Error: the API took too long to answer. Try again later.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: could not connect. Check your internet connection.")
        return None

    if response.status_code != 200:
        print(f"Error: the API returned status code {response.status_code}.")
        return None

    data = response.json()
    if data.get("code") != 200 or "data" not in data:
        print("Error: unexpected answer from the API.")
        return None

    return data["data"]


def show_verse(arabic, translation, language_name):
    """Print the verse nicely."""
    surah = arabic["surah"]
    print()
    print("=" * 60)
    print(f"  Verse of the Day - Surah {surah['englishName']} "
          f"({surah['englishNameTranslation']}) {surah['number']}:{arabic['numberInSurah']}")
    print("=" * 60)
    print()
    print(arabic["text"])
    print()
    print(f"{language_name}:")
    print(translation["text"])
    print()


def main():
    language_name, edition = choose_language()
    ayah_number = random.randint(1, TOTAL_AYAHS)
    verses = get_verse(ayah_number, edition)
    if verses is None:
        sys.exit(1)
    arabic, translation = verses[0], verses[1]
    show_verse(arabic, translation, language_name)


if __name__ == "__main__":
    main()