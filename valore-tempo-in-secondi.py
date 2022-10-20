numero_di_ore = float(input("Dammi il numero di ore: "))
numero_di_minuti = float(input("Dammi il numero dei minuti: "))
numero_di_secondi = float(input("Dammil il numero dei secondi: "))

valore_tempo_in_secondi = numero_di_ore * 3600 + numero_di_minuti * 60 + numero_di_secondi

print ("Il valore del tempo che hai inserito in secondi è:", (valore_tempo_in_secondi))