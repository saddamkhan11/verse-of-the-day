# Verse of the Day

A small Python program that shows a random verse (ayah) of the Quran in Arabic,
with an English or Urdu translation of your choice.

It gets live data from the free [AlQuran Cloud API](https://alquran.cloud/api).
No API key is needed.

## How to install

1. Install Python 3 from https://www.python.org
2. Download this project:
   ```
   git clone https://github.com/YOUR-USERNAME/verse-of-the-day.git
   cd verse-of-the-day
   ```
3. Create and turn on a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Mac / Linux
   ```
4. Install the library it needs:
   ```
   pip install -r requirements.txt
   ```

## How to run

```
python verse.py
```

Choose `1` for English or `2` for Urdu.

## Sample output

```
Choose a translation:
  1. English
  2. Urdu
Enter 1 or 2: 1

============================================================
  Verse of the Day - Surah Al-Baqara (The Cow) 2:286
============================================================

لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا وُسْعَهَا ...

English:
Allah does not charge a soul except [with that within] its capacity. ...
```

## How it works

- Picks a random number from 1 to 6236 (the total verses in the Quran).
- Calls `https://api.alquran.cloud/v1/ayah/{number}/editions/quran-uthmani,en.sahih`
  to get the Arabic text and the translation in one request.
- Uses `timeout=10`, checks the status code, and shows a friendly message
  instead of crashing if the internet or the API is down.
