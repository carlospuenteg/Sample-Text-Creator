from googletrans import Translator
import json

# Create the translator
translator = Translator()

# Import languages
languages = json.load(open('data.json'))

# Import sample text
sample = open("sample.txt", "r").read()

for lang in languages.items():
    f = open(lang + ".txt", "a").write(translator.translate(sample, dest=lang))