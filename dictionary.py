import string
import json

jsonFile = open("db/dictionary.json", "r")
jsonData = json.loads(jsonFile.read())

def add(word):
    word = word.lower().translate(str.maketrans("", "", string.punctuation))

    if word not in jsonData["words"]:
        jsonData["words"].append(word)
    
    return len(jsonData["words"]) - 1

def get(word):
    word = word.lower().translate(str.maketrans("", "", string.punctuation))

    if word in jsonData["words"]:
        return jsonData["words"].index(word)
    else:
        return -1

def makeSentenceFromWords(sentence):
    sentence = sentence.split()
    finalSentence = []

    for word in sentence:
        finalSentence.append(get(word))

    return finalSentence

def makeSentenceFromDictionary(sentence):
    finalSentence = []

    for word in sentence:
        if word < len(jsonData["words"]):
            finalSentence.append(jsonData["words"][word])
        else:
            finalSentence.append("???")

    return " ".join(finalSentence)

def done():
    global jsonFile

    jsonFile.close()

    jsonFile = open("db/dictionary.json", "w")

    jsonFile.write(json.dumps(jsonData))
    jsonFile.close()