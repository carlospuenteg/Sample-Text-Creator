from googletrans import Translator
import os
import json

def create_texts():
    # Create folder if it doesn't exist
    if not os.path.exists("texts_by_name"):
        os.mkdir("texts_by_name")
    if not os.path.exists("texts_by_code"):
        os.mkdir("texts_by_code")
        

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

    # Iterate through (keys and values) in languages object 


    # Write the translation to the files
    for code, name in languages.items():
        toWrite = ""

        for lines in divSample:
            if (lines != ""):
                print(code)
                toWrite += (translator.translate(lines, dest=code).text + "\n")

        f = open("texts_by_name/" + name + ".txt", "a").write(toWrite[:-1])
        f = open("texts_by_code/" + code + ".txt", "a").write(toWrite[:-1])

create_texts()