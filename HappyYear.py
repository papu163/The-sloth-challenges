def isHappyYear(year: int):
    lista=list(str(year))
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return False
    return True

def happyYear(a: int):
    if isHappyYear(a+1):
        return a+1
    else:
        while True:
            a += 1
            if isHappyYear(a):
                return a

print(happyYear(2017))
print(happyYear(1990))
print(happyYear(2021))
