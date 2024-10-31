def getPermutations(base: list) -> list:
    if len(base) == 1:
        return [base]
    permutations = []
    for i in range(len(base)):
        actualIndex = [base[i]]
        resto = base[:i] + base[i+1:]
        for p in getPermutations(resto):
            permutations.append(actualIndex + p)
    return permutations
def maper(method: str, numberList: list) -> dict:
    methodCodeName = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
    """COMBINATIONS:
    A: [32 - 47]
    B: [48 - 57]
    C: [58 - 64]
    D: [65 - 90]
    E: [91 - 96]
    F: [97 - 122]
    G: [123 - 126]
    """
    combinations = {
        "a": [chr(i) for i in range(32, 48)],
        "b": [chr(i) for i in range(48, 58)],
        "c": [chr(i) for i in range(58, 65)],
        "d": [chr(i) for i in range(65, 91)],
        "e": [chr(i) for i in range(91, 97)],
        "f": [chr(i) for i in range(97, 123)],
        "g": [chr(i) for i in range(123, 127)]
    }
    methods = {}
    permutations = getPermutations([combinations["a"], combinations["b"], combinations["c"], combinations["d"], combinations["e"], combinations["f"], combinations["g"]])
    for i in range(len(permutations)):
        permutations[i] = [item for sublist in permutations[i] for item in sublist]
    for i in range(0, len(methodCodeName) ** 2):
        methods[methodCodeName[i // len(methodCodeName)] + methodCodeName[i % len(methodCodeName)]] = permutations[i]
    characterDictionary = {i: None for i in methods[method]}
    temporalIndex = 0
    for i in characterDictionary:
        characterDictionary[i] = chr(numberList[temporalIndex]) #This will return: normalCharacter > encryptedCharacter
        temporalIndex += 1
    return characterDictionary
def codeGenerator() -> list:
    from random import randint
    methodCodeName = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
    normalList = [i for i in range(32, 127)]
    randomList = []
    for i in range(0, len(normalList)):
        randomList.append(normalList.pop(randint(0, len(normalList) - 1)))
    method = ""
    for i in range(0, 2):
        method += methodCodeName[randint(0, len(methodCodeName) - 1)]
    return method, randomList
def codifier(method: str, password: list, character: str) -> str:
    """
    method variable should contain the method used to create the dictionary
    password variable should contain the password given after creating a dictionary
    character variable should contain the character that is going to be encrypted
    """
    actualMaper = maper(method, password)
    return actualMaper[character]
def decodifier(method: str, password: list, character: str) -> str:
    """
    method variable should contain the method used to create the dictionary
    password variable should contain the password given after creating a dictionary
    character variable should contain the character that is going to be encrypted
    """
    actualMaper = maper(method, password)
    invertedMaper = {v : k for k, v in zip(actualMaper.keys(), actualMaper.values())}
    return invertedMaper[character]
while __name__=="__main__":
    print("Visual module.")
    print("Avaliable options:")
    print("1.- Generate password.")
    print("2.- Codify a message.")
    print("3.- Decodify a message.")
    choise = input("Enter the number choised: ")
    if choise == "1":
        method, password = codeGenerator()
        print(f"The method is: {method}\nThe password is: {password}")
    elif choise == "2":
        method = input("Enter the method used to create the dictionary: ")
        password = input("Enter the password used to create the dictionary(1, 2, 3, ...): ")
        password = password.split(", ")
        password = [int(i) for i in password]
        word = input("Enter the word to codify: ")
        finalWord = ""
        for i in range(len(word)):
            finalWord += codifier(method, password, word[i])
        print(f"Codified message: {finalWord}")
    elif choise == "3":
        method = input("Enter the method used to create the dictionary: ")
        password = input("Enter the password used to create the dictionary(1 2 3 ...): ")
        password = password.split(", ")
        password = [int(i) for i in password]
        word = input("Enter the word to decodify: ")
        finalWord = ""
        for i in range(len(word)):
            finalWord += decodifier(method, password, word[i])
        print(f"Decodified message: {finalWord}")