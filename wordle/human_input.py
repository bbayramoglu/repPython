from pc_job import Listing, Split_word, Select_word
from colorama import Fore, Style

used_right=0
guess = []
right_p=["","","","",""]
falses=[]
main_w=Split_word.splittedWord
#print(main_w)
while True:
    false_p=["","","","",""]
    if main_w==right_p:
        print(f"{Fore.BLUE}Tebrikler kelimeyi buldunuz{Style.RESET_ALL}")
        break
    if used_right>=6:
        print(f"{Fore.RED}Hakkınız kalmadı günün kelimesi:{Style.RESET_ALL}{Fore.YELLOW} {Select_word.word} {Style.RESET_ALL}")
        break

    g2=input("5 harfli bir kelime giriniz: ")
    with open("C:/Users/Furkan/Desktop/docs/anna/wordle/words_entered.txt","a+",encoding="utf-8") as file:
        if len(g2)==5 and g2 not in file:
            file.write(f"{g2}\n")
    g1=g2.strip().lower()
    if g1 == "ok":
        break
    elif g1 not in Listing.words:
        print(f"{Fore.RED}Listede olmayan bir kelime girdiniz. Tekrar giriniz{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{used_right} hakkını kullandın{Style.RESET_ALL}".center(100,"*"))
        
    else:
        li=[]
        for i in g1:
            li.append(i)
        if li in guess:
            print(f"{Fore.YELLOW}{used_right} hakkını kullandın{Style.RESET_ALL}".center(100,"*"))
            print("Önceden girdiğiniz kelimeyi giremezsiniz.")
        else:
            used_right+=1
            print(f"{Fore.YELLOW}{used_right} hakkını kullandın{Style.RESET_ALL}".center(100,"*"))
            guess.append(li)
            for i in range(0,len(guess)):
                for j in range (0,len(main_w)):
                    if guess[i][j] in main_w:
                        if guess[i][j]==main_w[j]:
                            right_p[j]=guess[i][j]
                        elif guess[i][j] !=main_w:
                            false_p=["","","","",""]
                            false_p[j]=guess[i][j]
        falses.append(false_p)                    
    
    print(f"{Fore.GREEN}{right_p}{Style.RESET_ALL}")
    for i in falses:
        print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}")