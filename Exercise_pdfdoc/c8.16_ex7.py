# Schreiben Sie das Programm um, das den Benutzer zur Eingabe einer Liste von Zahlen auffordert 
# und am Ende das Maximum und Minimum der Zahlen ausgibt, wenn der Benutzer „done“ eingibt. 
# Schreiben Sie das Programm so, dass es die Zahlen in einer Liste speichert 
# und die Funktionen max() und min() verwendet, 
# um die größte und kleinste Zahl nach Abschluss der Schleife zu ermitteln.
# Bitte eine Zahl eingeben: 6
# Bitte eine Zahl eingeben: 2
# Bitte eine Zahl eingeben: 9
# Bitte eine Zahl eingeben: 3
# Bitte eine Zahl eingeben: 5
# Bitte eine Zahl eingeben: done
# Maximum: 9.0
# Minimum: 2.0

lst = list()
while True:
    inp_number = input('Bitte eine Zahl eingeben: ')
    if inp_number == 'done':
        break
    try: 
        inp_float = float(inp_number)
    except:
        print('Bitte ganze Zahlen verwenden.')
        continue
    lst.append(inp_float)
print(f'Maximum: {max(lst)}, Minimum: {min(lst)}')