def maper(numberList: list):
    characterDictionary = {chr(i): i for i in range(32, 127)}
    temporalIndex = 0
    for i in characterDictionary:
        characterDictionary[i] = numberList[temporalIndex]
        temporalIndex += 1
    return characterDictionary
def codeGenerator():
    from random import randint
    normalList = [i for i in range(32, 127)]
    randomList = []
    for i in range(0, len(normalList)):
        randomList.append(normalList.pop(randint(0, len(normalList) - 1)))
    return randomList

#TODO: DELETE AFTER
print(maper(codeGenerator()))