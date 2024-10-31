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
        characterDictionary[i] = numberList[temporalIndex]
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
    method variable should contain the method used to create the dictionary, for example:
    alfaalfa: {chr(i): i for i in range(32, 127)}
    """
    password = codeGenerator()
#TODO: DELETE AFTER
print(maper(*codeGenerator()))