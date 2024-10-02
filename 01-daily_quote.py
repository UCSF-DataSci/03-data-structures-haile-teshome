#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    # Create a list of quotes here
    "Ill get it next time",
    "Geez louise",
    "Gosh darn it",
    "Well golllly",
    "Dang nab it",
    "Shucks",
    "I'm feeling a little goofy"
]

def get_quote_of_the_day(quotes):
    todays_quote = quotes
    random.seed(int(date.today().strftime('%m%d%Y')))
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# # Cron job (add this to your crontab):
# # 0 8 * * * /usr/bin/python3 /Users/hteshome/Desktop/Pytools_Class/03-data-structures-haile-teshome/quote_generator.py >> /Users/hteshome/Desktop/Pytools_Class/03-data-structures-haile-teshome/daily_quote.txt