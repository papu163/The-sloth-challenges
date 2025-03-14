#English is not my main language so uhh, idk

Letters = {
    1 : "I",
    2 : "Z",
    3 : "E",
    4 : "H",
    5 : "S",
    6 : "G",
    7 : "L",
    8 : "B",
    9 : "-",
    0 : "O"
}
def turnCalc(num: int):
    turn_around=str(num).replace('.', '')
    turn_around=list(reversed(str(num)))
    numbers=list(turn_around)
    idk=numbers
    resultado="".join(Letters[int(n)] for n in idk)
    print(resultado)
turnCalc('07734')
turnCalc(5508)
turnCalc(3045)
