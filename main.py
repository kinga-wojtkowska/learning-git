shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for k, v in shopping_list.items():
    print(f"Idę do: {k.capitalize()}, kupuję tu następujące rzeczy:", [i.capitalize() for i in v], ".")

length = 0
for k, v in shopping_list.items():
    length = length + len(shopping_list[k])
print("W sumie kupuję", length, "produktów")

print("\nCiekawe co mi z tego wyjdzie")

print("\nGotuję właśnie bób")
print("\nMniam, mniam, będzie pyszny obiadek!")

print("co tam, co tam co tam")