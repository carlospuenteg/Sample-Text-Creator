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

print(sampleArr)

for i in range(0,len(sampleArr),20):
    divSample.append("\n".join(sampleArr[i:i+10]))


for lang in languages.keys():
    for lines in divSample:
        if (lines != ""):
            print(lang)
            f = open(lang + ".txt", "a")
            f.write(translator.translate(lines, dest=lang).text + "\n")
            f.close()