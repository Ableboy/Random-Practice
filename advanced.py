# The very class object: user
# class User():
#     def __init__(self, email):
#         self.email = email
#         """The email and sign_in function are showing the user availability"""
#     def sign_in(self):
#         print("logged in")
# class Wizard(User):
#     """The classes(wizard & witch) are subclasses that carries the parental class(User) and
#     functions shown the classes availability"""
#     def __init__(self, name, power, email):
#         User.__init__(self, email) # or super().__init__(email) meaning it's used to represent parent class.
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f"attacking strength of {self.name} is given as {self.power}")
#
#
# class Witch(User):
#     def __init__(self, name, arrow):
#         self.name = name
#         self.arrow = arrow
#
#     def attacks(self):
#         print(f"attacking arrow strength of {self.name} is {self.arrow}")
#
#     def danger(self):
#         print(f"The powerful arrow shoot wasn't effective on {self.name}")
#
#
# class HybridBorg(Wizard, Witch): # This class carries multiple class called multiple inherit.
#     def __init__(self, name, power, email, arrow):
#         Wizard.__init__(self, name, power, email)
#         Witch.__init__(self, name, arrow)
#
#
# # wizard1 = Wizard("merlin",50)
# # witch1 = Witch("robert", 100)
# # print(dir(wizard1.email)) # The dir() is an introspection that shows me what the given output have access to.
# hbg1 = HybridBorg("merlin", 50, "ebubemoses235@gmail.com", 52)
# print(hbg1.email)
#



# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# #1 Add nother Cat
# class Ebus(Cat):
#     def look(self, color):
#         return f"{color}"
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon("simon", 12), Sally("sally", 15), Ebus("ebus", 22)]
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)
#
# #4 Output all of the cats walking using the my_pets instance
# my_pets.walk()
#
#
# # class creation for a tech company
# class Company():
#     def __init__(self, name, year, owner, customer):
#         self.name = name
#         self.year = year
#         self.owner = owner
#         self.customer = customer
#
#     def appreciation(self): # Thanking users and give users input about the company
#         print(f"This is {self.name}, owned by {self.owner} and we do appreciate your contribution towards this company")
#         print(f"we're good at modifying intelligent into software and we've been in existent since {self.year}")
#         return 'cool to have you.'
#     def customers(self): # regular customers creation
#         regular = ["moses", "juwon", "ebube", "tunde", "taye"]
#         if self.customer in regular:
#             print("we checked into our database, seems you been our customer since decades")
#             print("we love to tell you that there will be new features in all our products. check them out!!")
#         else:
#             print("sorry, you're not part of our customer but we're glad to have you, do enjoy yourself!!")
#         return "check yourself in"
# class Player():
#     regular = "customer"
#     def __init__(self, password):
#         self.password = password
#     def product(self):
#         note = "All our product we use AI implementation as it bedrock, i hope you enjoy it."
#         notes = """Before you can access our product services,
# please input your password to help secure your account."""
#         add = note + notes
#         return add
#
# class Detail(Player):
#     def sign_in(self):
#         passway = input("Input your access key: ")
#         if passway == self.password:
#             print("correct key")
#         else:
#             print("sorry wrong key, try again.")
#             exit()
#         return "see products"
#
#
# run = Company("Tadpe industrial evolution", "2023", "Ebube.N.M", "juwon")
# runner = Detail("ableboy1")
# print(run.appreciation())
# print(run.customers())
# print(Player.product(self= Player))
# print(runner.sign_in())


class Product:
    def __init__(self, company_name, product_id, product_name, price, quantity_in_stock):
        self.company_name = company_name
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def product_info(self):
        print(f"Welcome to {self.company_name} Superstore.")
        print("Our products are highly standard")
        print("PRODUCT INGREDIENTS")
        recipe = "Wheat Flour, Sugar, Margarine, Salt, Yeast, Improver, Water, Preservatives."
        print(recipe)
        print("PRODUCED & PACKAGED BY:")
        print(f"{self.company_name} superstore")
        address = "7, Brentifield Estate, Oke-afa, Magboro, Ogun State, Nigeria"
        print(address)
        contact = "contact us: +234 905 914 6766, +234 902 227 3369"
        email = "Email: funkybeesuperstore@gmail.com"
        return contact + "\n" + email

    def more_info(self):
        print(
            f"{self.product_name} (ID: {self.product_id}) - Price: N{self.price} - Stock: {self.quantity_in_stock} units")


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def rm_product(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"{product.product_name} removed from the cart.")
        else:
            print("Product not found in the cart.")

    def display_cart(self):
        print("Shopping Cart:")
        for item in self.cart:
            item.more_info()


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def user_info(self):
        print(f"User ID: {self.user_id} - Name: {self.name} - Email: {self.email}")


class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total_price = sum([item.price for item in cart.cart])
        self.status = "Pending"

    def order_details(self):
        print("Order Details:")
        self.user.user_info()
        self.cart.display_cart()
        print(f"Total Price: N{self.total_price}")
        print(f"Order Status: {self.status}")


# Example usage:
company = Product("FUNKY-BEES", 1000231, "bread", 900, 1)
user1 = User(101, "Ebube", "ebubemoses@gmail.com")
shopping = ShoppingCart()
shopping.add_product(company)

order = Order(user1, shopping)

print(company.product_info())
print(company.more_info())
print(shopping.add_product(company))
print(shopping.rm_product(company))
print(shopping.display_cart())
print(user1.user_info())
print(order.order_details())
