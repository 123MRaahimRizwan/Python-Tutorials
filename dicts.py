# Dictionaries are key value pairs in python

# Plain dictionary
dict1 = {
    "Raahim": "Burger",
    "John": "Fish",
    "Smith": "Cucumber"
}

print(dict1)
print(dict1["John"])

dict1["Sarah"] = "Pizza"
dict1["David"] = "Buscuits"
print(dict1)

# Functions of dictionaries
print(dict1.get("John"))
print(dict1.items())

# Complex dictionary
dict2 = {
    "Kevin": "Chocolates",
    "Bruce": "Fish",
    "Lee": "Banana",
    "Kane": {
        "Morning": "Bread",
        "Afternoon": "Buscuits",
        "Evening": "Junk Food"
    }
}
print(dict2["Kane"]["Morning"])

# Example tuple code
# t1 = ()
