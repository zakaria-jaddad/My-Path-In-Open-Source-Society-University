# Searches CSV for popularity of a title

# import csv

# from cs50 import SQL

# # Open database
# db = SQL("sqlite:///favorites.db")

# # Prompt user for title
# title = input("Title: ").strip()

# # Search for title
# rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", "%" + title + "%")

# # Get first (and only) row
# row = rows[0]

# # Print popularity
# print(row["counter"])
import csv

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

title = input("title :").strip()

rows = db.execute("SELECT title AS walo FROM favorites WHERE title LIKE ?", "%" + title + "%")

    # for printing one thing from th e table
row = rows[0]
print(row["walo"])



    # for printong multiple things in table
for row in rows:
    print(row["walo"])