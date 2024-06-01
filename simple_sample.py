# see = open("money.txt")
# print(see.readline())
# # see.seek(21) # shows all content in file and chooses which content to start with
# print(see.readline())
# see.seek(0)
# print(see.readlines())
# see.close()

# # smart way to open and read through a file
# try:
# 	with open("money.txt", mode = "x") as my_file:
# 		print(my_file.read())

# except FileNotFoundError as err:
# 	print("File not found, please check in your data")
# 	raise err
# except IOError as err:
# 	print("IO Error")
# 	raise err


# # A module that change a language to other languages, detect.
# import goslate
	
# gs = goslate.Goslate()  # get the instances to work.

# # about to change to another language.

# try:
# 	with open("app\money.txt", mode = "r") as test:
# 		text = test.read()
# 		print(gs.translate(text, "fr"))  # about to change to another language.
# 		# text = "i love the fact that i am a programmer."   # written in en to be changed to france.
# 		# gs = goslate.Goslate()  # get the instances to work.
# 		# print(gs.translate(test, "fr"))   # about to change to another language.
# except FileNotFoundError as err:
# 	print("File not found, please check in your data")
# 	raise err
# except IOError as err:
# 	print("IO Error")
# 	raise err

# but working with offline py translated module
import translate

# text = "i love the fact that i am a programmer."   # written in en to be changed to japanese.
translator = translate.Translator(to_lang="fr")
try: 
	with open("app\money.txt", mode = "r") as my_translate:
		dude_translate = my_translate.read()
		translation = translator.translate(dude_translate)
		with open("app\money-fr.txt", mode = "w") as my_translate2:
			my_translate2.write(translation)

except FileNotFoundError as error:
	print("check check check, my bored file.")
	raise error




