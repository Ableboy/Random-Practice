# This module is an onsite that changes a language to other languages, detect.

# A module that change a language to other languages, detect.
import goslate
	
gs = goslate.Goslate()  # get the instances to work.

# about to change to another language.

try:
	with open("app\money.txt", mode = "r") as test:
		text = test.read()
		print(gs.translate(text, "fr"))  # about to change to another language.
		# text = "i love the fact that i am a programmer."   # written in en to be changed to france.
		# gs = goslate.Goslate()  # get the instances to work.
		# print(gs.translate(text, "fr"))   # about to change to another language.
except FileNotFoundError as err:
	print("File not found, please check in your data")
	raise err
except IOError as err:
	print("IO Error")
	raise err

# Another short way!!!!
import goslate
text = "i love the fact that i am a programmer."   # written in en to be changed to france.
gs = goslate.Goslate()  # get the instances to work.
print(gs.translate(text, "fr"))   # about to change to another language.
translate = gs.get_languages() # To get full form of the language to be changed to.
print(translate["fr"])




''' But working with offline py translated module '''
import translate
text = "i love the fact that i am a programmer."   # written in english to be changed to spanish.
translator = translate.Translator(to_lang="ja")
translation = translator.translate(text)
print(translation)


# Another Form of Translated Module
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