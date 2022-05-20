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

    # If the appended text would be < 5000 characters
    if len(toAppend) + len(line) + 1 < 5000:
        toAppend += (line + "\n")
    else:
        divSample.append(toAppend)
        toAppend = (line + "\n")

# Add the last text to append (without the \n)
divSample.append(toAppend)



# Write the translation to the files
for lang in languages.keys():
    toWrite = ""

    for lines in divSample:
        if (lines != ""):
            print(lang)
            toWrite += (translator.translate(lines, dest=lang).text + "\n")

    f = open(lang + ".txt", "a")
    f.write(toWrite[:-1])
    f.close()