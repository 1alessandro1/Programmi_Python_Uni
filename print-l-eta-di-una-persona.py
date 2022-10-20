nome = (input("Inserisci il tuo nome: "))
anno_di_nascita = float(input("Dimmi in che anno sei nato/a: "))
anno_corrente = float(input("Inserisci in che anno siamo: "))

eta_persona = anno_corrente - anno_di_nascita

print ( "Ciao", (nome), "la tua età è", (eta_persona))