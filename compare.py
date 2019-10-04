import random

import dictionary

def getConfidence(source, data):
    confidence = 0
    sourcePosition = 0

    for dataPosition in range(0, len(data)):
        if sourcePosition < len(source):
            if data[dataPosition] == source[sourcePosition]:
                confidence += 1
                sourcePosition += 1
            else:
                confidence -= 1
        else:
            break
    
    return confidence / max(len(source), len(data))

def getInSource(source, data):
    sourcePosition = random.randint(0, len(source) - 1)
    dataStartPosition = 0
    sourceIterativeCount = 0
    answers = []

    while True:
        if sourcePosition < len(source) and dataStartPosition < len(data) and source[sourcePosition] == data[dataStartPosition]:
            dataPosition = dataStartPosition
            confidence = 100
            answer = []

            while confidence > 0 and sourcePosition < len(source) and dataPosition < len(data):
                if source[sourcePosition] == data[dataPosition]:
                    answer.append(source[sourcePosition])

                    confidence += 1
                else:
                    confidence -= 1

                sourcePosition += 1

                if sourcePosition >= len(source):
                    sourcePosition = 0

                dataPosition += 1

                if dataPosition >= len(data):
                    break
            
            answers.append(answer)

            print("Found potential answer: " + dictionary.makeSentenceFromDictionary(answer))

        sourcePosition += 1

        if sourcePosition >= len(source):
            sourcePosition = 0

        sourceIterativeCount += 1

        if sourceIterativeCount >= len(source):
            if dataStartPosition >= len(data):
                break
            else:
                dataStartPosition += 1

    return answers