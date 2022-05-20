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
txtLen = 0
for i in range(len(sampleArr)):
    txt = sampleArr[i] + "\n"

    if txtLen + len(txt) < 5000:
        toAppend += txt
        txtLen += len(txt)
    else:
        divSample.append(toAppend)
        toAppend = txt
        txtLen = len(txt)

"""
for lang in languages.keys():
    for lines in divSample:
        if (lines != ""):
            print(lang)
            f = open(lang + ".txt", "a")
            f.write(translator.translate(lines, dest=lang).text + "\n")
            f.close()
"""