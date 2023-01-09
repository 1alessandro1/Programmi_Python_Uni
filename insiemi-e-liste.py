
dizionario_vuoto = {}

semi = {"cuori", "quadri", "fiori", "picche"} # sono gli insiemi

ingegneri = set() # istruzione per creare un insieme vuoto

a = ["Lunedi", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"] # liste


# tonde sono le tuple

linguaggi = set(a)


# h[1] # solo se tupla o lista, ma non di un insieme


Satelliti = {"Io", "Europa", "Callisto", "Ganimede"}

for luna in Satelliti:
    print(luna)

###############

linguaggi = {"Ruby", "C#", "Javascript", "TypeScript", "Holy C", "C --", "Python"}

linguaggi.add("Pascal")
linguaggi.add("Python")

for i in linguaggi:
    print(i)
    
linguaggi.clear() # per pulire l'insieme

print(len(linguaggi))