"""
some exercises about dictionaries in python as well as saving data
"""
# starting real simple, just taking data from a simple dictionary
# then putting the data in a json file and then using that data
import json

birthdates = {
"Ewa": "03/02/1983",
"Maciej": "06/12/1984",
"Ada" : "04/02/1989",
"Tomasz" : "05/05/1987",
"Milosz" : "25/09/2013"
}

with open("birthdates.json", "w") as f:
  json.dump(birthdates, f)

with open("birthdates.json", "r") as f:
  info = json.load(f)

def find_birthdays(dic):
  name = raw_input("Whose birthday do you want to know? Write name: ").capitalize()
  if name in dic:
    print dic[name]
  else:
   print "Sorry, no such person in my database"
find_birthdays(info)


groceries = {"plums": 5.20, "tomatoes": 2.45, "potatoes": 1.45, "apples": 2.35, "pears": 4.00, "onions": 1.50}

with open("groceries.json", "w") as g:
  json.dump(groceries, g)

with open("groceries.json", "r") as g:
  shopping = json.load(g)

def check_price(dic):
  article = raw_input("What do you need to buy? ")
  if article in dic:
    print dic[article]
  else:
    print "No such article"
check_price(shopping)

my_library = {"Musierowicz": ["Szosta klepka", "Opium w rosole"], 
"Rowling": ["Harry Potter and the Deathly Hallows", "Harry Potter and the Goblet of Fire"], 
"Herbert": "Poezja"}
print my_library["Musierowicz"]
print my_library["Rowling"]

with open("library.json", "w") as h:
  json.dump(my_library, h)
with open("library.json", "r") as h:
 books = json.load(h)

def find_books_by_author(lib):
  author = raw_input("Check if we have book of your favorite author ").capitalize()
  if author in lib:
    print "We have got these books by this author: %s "  % lib[author]
  else:
   print "No books by this author"

find_books_by_author(books)
  