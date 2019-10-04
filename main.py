import json

import dictionary
import compare

while True:
    command = input("EduBot > ")

    if command == "exit":
        dictionary.done()

        print("Exited. Have a nice day!")

        break
    elif command == "init":
        givenLabel = input("EduBot / Label to give training data? > ")

        trainingDataFile = open("db/training/" + givenLabel + ".json", "w")

        trainingDataFile.write(json.dumps({
            "statements": [],
            "qa": []
        }))

        trainingDataFile.close()
    elif command == "import":
        importingFile = open(input("EduBot / File to import? > "), "r")
        importingFileData = importingFile.read()

        importingFile.close()

        givenLabel = input("EduBot / Label to give final training data? > ")

        print("Processing file...")

        trainingDataFile = open("db/training/" + givenLabel + ".json", "r")

        for word in importingFileData.split():
            if word != "[S]" and word != "[Q]" and word != "[A]":
                dictionary.add(word)
        
        mode = "statements"
        
        trainingData = json.loads(trainingDataFile.read())
        
        for word in importingFileData.split():
            if word == "[S]":
                mode = "statements"
            elif word == "[Q]":
                mode = "q"

                trainingData["qa"].append({
                    "question": [],
                    "answer": []
                })
            elif word == "[A]":
                mode = "a"
            elif mode == "statements":
                trainingData["statements"].append(dictionary.get(word))
            elif mode == "q":
                trainingData["qa"][-1]["question"].append(dictionary.get(word))
            elif mode == "a":
                trainingData["qa"][-1]["answer"].append(dictionary.get(word))
        
        trainingDataFile.close()

        trainingDataFile = open("db/training/" + givenLabel + ".json", "w")

        trainingDataFile.write(json.dumps({
            "data": trainingData
        }))
        trainingDataFile.close()

        print("Processed file!")
    elif command == "ask":
        givenLabel = input("EduBot / Label of training data to use in answer? > ")

        trainingDataFile = open("db/training/" + givenLabel + ".json", "r")
        trainingData = json.loads(trainingDataFile.read())

        question = dictionary.makeSentenceFromWords(input("EduBot / Question to ask? > "))
        highestQAScore = -10000
        highestQAQuestion = []
        highestQAAnswer = []

        for qa in trainingData["data"]["qa"]:
            QAScore = compare.getConfidence(qa["question"], question)
            QAQuestion = qa["question"]
            QAAnswer = qa["answer"]

            if QAScore > highestQAScore:
                highestQAScore = QAScore
                highestQAQuestion = QAQuestion
                highestQAAnswer = QAAnswer
        
        print("Found nearest question: " + dictionary.makeSentenceFromDictionary(highestQAQuestion))
        print("Trained answer: " + dictionary.makeSentenceFromDictionary(highestQAAnswer))

        compare.getInSource(trainingData["data"]["statements"], highestQAAnswer)