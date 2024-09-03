def spellcheck(green, black, yellow, word):
    for t in range (5):
        if word[t] in black and word[t] not in green: return False
        for u in range (5):
            if word[t] in yellow[u][t]: return False
            if yellow[u][t] != "!":
                if yellow[u][t] not in word: return False
        if green[t] != "!":
            if word[t] != green[t]: return False
    return True

wrdlreader = open('wordle.txt', 'r')

wrdl = []
for line in wrdlreader:
    wrdl.append(line.strip())
wrdlreader.close()

black = "" #black letters
yellow = [""] * 5
yellow[0] = "!!!!!" #replace ! with yellow letters from first row, leave the rest
yellow[1] = "!!!!!" #yellow letters from second row
yellow[2] = "!!!!!" #yellow letters from third row
yellow[3] = "!!!!!" #yellow letters from fourth row
yellow[4] = "!!!!!" #yellow letters from fifth row
green = "!!!!!" #replace ! with green letters, leave the rest

for y in range(0, 5):
    black += input("Black letters?\n")
    green = input("Green letters?\n")
    if green == "": green = "!!!!!"
    yellow[y] = input("Yellow letters?\n")
    if yellow[y] == "": yellow[y] = "!!!!!"
    for x in range (0, len(wrdl)):
        if spellcheck(green, black, yellow, wrdl[x]) == False: continue
        print(wrdl[x])
