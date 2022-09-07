alphabeth = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z", " "]

def func(key:str=""):
    if len(key) != 1 or key not in alphabeth:
        key = "a"
    def fun(letter:str):
        if len(letter) == 1 and letter in alphabeth:
            let = alphabeth.index(key)
            num = alphabeth.index(letter) - let
            lon = len(alphabeth)
            return num - lon * (num//lon) + 1
        else:
            return -1
    return fun
numify = func("x")


def score(input:str):
    if isinstance(input, str):
        n = 1
        point = 0
        for letter in input:
            point += n*numify(letter)
            n *= 1/(len(alphabeth)+1)
        return point
    else:
        return -1


def sort_list_of_strings(oldList:list=[]):
    newList = []
    for a in range(len(oldList)):
        if len(newList) == 0:
            newList.append(oldList[a])
        else:
            for b in range(len(newList)):
                if score(oldList[a][0]) < score(newList[b][0]):
                    newList.insert(b, oldList[a])
                    break
            if score(oldList[a][0]) >= score(newList[len(newList) - 1][0]):
                newList.append(oldList[a])
    return newList


def termify(facc):
    factors = []
    var = deg = ""
    mode = "str"
    for i in facc:
        # print(i, i.isnumeric(), mode)
        if i.isnumeric():     # if the current part is a number
            if mode == "num":       # and the previous one was also a number
                deg += str(i)
            elif mode == "str":     # and the previous one was a letter
                mode = "num"
                deg = str(i)
        elif not i.isnumeric():   # if the current part is a letter
            if mode == "str":       # and the previous one was also a letter
                var += str(i)
            elif mode == "num":     # and the previous one was a number
                mode = "str"
                factors.append((var, int(deg)))
                deg = ""
                var = i
    factors.append((var, int(deg)))
    return factors
