## Montante (M) = capitale investito + interesse
# C= Capitale investito inizialmente
# I= Interesse applicato
# T= Tempo di investimento

C = float(input("Inserisci il capitale invesito: "))
I = float(input("Inserisci il tasso di interesse applicato: "))
T = float(input("Inserisci il tempo di investimento: "))

Montante = float(C*(1+I/100)**T)

print ("Il montante risultante dagli investimenti iniziali è di circa:", round(Montante), "euro")
