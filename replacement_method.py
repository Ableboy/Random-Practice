# create function of replacement

def replace():
    quote = "hey precilar, i love the way you speak to me"
    print(quote)
    what_to_replace = input("Enter what to replace: ")
    replacement = input("Enter your replace: ")
    correct = quote.replace(what_to_replace, replacement)
    print(correct)

replace()