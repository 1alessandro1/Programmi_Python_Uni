# Puoi votare oppure no?

anno_corrente, anno_nascita_persona = input("Inserire in che anno siamo separando con una virgola il tuo anno di nascita: ").split(',')

anno_corrente = int(anno_corrente)
anno_nascita_persona = int(anno_nascita_persona)


if (anno_corrente - anno_nascita_persona) >= 18: 
    print("Ok puoi votare")
else:
    print ("Mi spiace ma devi ancora aspettare", abs((anno_corrente - anno_nascita_persona)- 18), "anni")

# oppure importando datetime

# import datetime as dt
# annoNascita = int(input("Inserisci l'anno di nascita: "))
# annoCorrente = dt.datetime.now().year
# 
# if annoNascita - annoCorrente >= 18:
#     print("hai diritto di andare a cagare")
# else: 
#     print("no non hai diritto al voto")
