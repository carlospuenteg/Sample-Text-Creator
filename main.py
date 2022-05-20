from googletrans import Translator
import json

# Create the translator
translator = Translator()

# Import languages
languages = json.load(open('languages.json'))

# Import sample text
sample = open("sample.txt", "r").read()
sampleArr = sample.splitlines()


for lang in languages.keys():
    for line in sampleArr:
        print(lang)
        f = open(lang + ".txt", "a")
        f.write(translator.translate(sample, dest=lang).text)
        f.close()