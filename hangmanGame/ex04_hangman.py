#EXERCICE NON TERMINE


import random

english_words = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze",
                 "able", "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent",
                 "absorbed", "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable",
                 "accessible", "accidental", "account", "accurate", "achiever", "acid", "acidic", "acoustic",
                 "axiomatic", "babies", "baby", "back", "bad", "badge", "bag", "bait", "bake", "balance", "ball", "ban",
                 "bang", "barbarous", "bare", "base", "baseball", "bashful", "basin", "basket", "basketball", "bat",
                 "bath", "bathe", "battle", "bawdy", "bead", "beam", "bear", "beautiful", "bed", "bedroom", "beds",
                 "bee", "beef", "befitting", "beg", "beginner", "behave", "behavior", "belief", "believe", "bell",
                 "cactus", "cagey", "cake", "cakes", "calculate", "calculating", "calculator", "calendar", "call",
                 "callous", "calm", "camera", "camp", "can", "cannon", "canvas", "cap", "capable", "capricious",
                 "caption", "car", "card", "care", "careful", "careless", "caring", "carpenter", "carriage", "carry",
                 "cars", "cart", "carve", "cast", "cat", "cats", "cattle", "cause", "cautious", "cave", "ceaseless"]

gword = random.choice("english_words")
size_gword=len(gword)
i=size_gword+2
result = ""
print("Welcome to the Hangman Game !\nA word to guess was chosen, let's start!!!!\nNumbers of chance:",i)
while i>0:
    ch_entered=input("Please enter a character:")
    if ch_entered not in gword:
       i-=1
       print("Wrong !!! Try again, please")
       print("Numbers of chance:",i)
       ch_entered=input("Please enter a character:")
    else:
        print("Yes!! That's it !!")
        for j in gword:
            if gword[j] == ch_entered:
                ind=j
        result[ind]=ch_entered
        print(result)
        ch_entered = input("Please enter a character:")
if i<0:
    print("You loose, you can cry...")
if result == gword:
    print("You win !! Good game!")