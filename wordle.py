def spellcheck(green, black, yellow, word): #function to evaluate a candidate word
    for t in range (5):
        if word[t] in black: return False #if a letter is in black return false
        if green[t] != "!": if word[t] != green[t]: return False #if a green letter isn't in the word return false
        for u in range (5):
            if word[t] in yellow[u][t]: return False #if a letter is in an indicated wrong position return false
            if yellow[u][t] != "!": if yellow[u][t] not in word: return False #if a yellow letter isn't in the word return false
    return True

wrdlreader = open('wordle.txt', 'r') #open list of candidate words

wrdl = []
for line in wrdlreader:
    wrdl.append(line.strip()) #read in candidate words
wrdlreader.close()

black = ""
yellow = [""] * 5
yellow[0] = "!!!!!" 
yellow[1] = "!!!!!" 
yellow[2] = "!!!!!" 
yellow[3] = "!!!!!" 
yellow[4] = "!!!!!" 
green = "!!!!!"

for y in range(0, 5):
    black += input("Black letters?\n") #take input for black letters
    green = input("Green letters?\n") #take input for green letters
    if green == "": green = "!!!!!"
    yellow[y] = input("Yellow letters?\n") #take input for yellow letters
    if yellow[y] == "": yellow[y] = "!!!!!"
    for x in range (0, len(wrdl)):
        if spellcheck(green, black, yellow, wrdl[x]) == False: continue #skip invalid candidate words
        print(wrdl[x]) #print valid candidate words
