parola = "casa"
word=list(parola)

out=["-"]*len(parola)

vite = 5

while out != word and vite > 0:
    print("\u2764"*vite)
    print(out)
    guess = input("Indovina una lettera: ")

    if guess in word:
        for i in range (len(word)):
            if guess == word[i]:
                out[i] = guess    
    else:
        vite -= 1
        print("Hai sbagliato, sono rimaste ancora", vite, "vite")
        
    if vite == 0:
        print("Hai finito le vite!")
        break

