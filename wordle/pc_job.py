class Listing:
    from random import shuffle
    import random
    words=[]
    file=open("C:/Users/Furkan/Desktop/docs/anna/wordle/words.txt","r",encoding="utf-8")
    for i in file:
        words.append(i[0:5].lower().strip())
    random.shuffle(words)     

class Select_word:
    import random
    word = random.choice(Listing.words)

class Split_word:
    splittedWord=[]
    for i in Select_word.word:
        splittedWord.append(i)





