from googletrans import Translator
import json

# Create the translator
translator = Translator()

# Import languages
languages = json.load(open('languages.json'))

# Import sample text
sample = open("sample.txt", "r").read()
sampleArr = sample.splitlines()
divSample = []

toAppend = ""

# For each line in the sample
for line in sampleArr:

    if len(toAppend) + len(line) + 1 < 5000: # If the appended text would be < 5000 characters
        toAppend += (line + "\n")
    else:
        divSample.append(toAppend)
        toAppend = (line + "\n")


for lang in languages.keys():
    for lines in divSample:
        if (lines != ""):
            print(lang)
            f = open(lang + ".txt", "a")
            f.write(translator.translate(lines, dest=lang).text + "\n")
            f.close()