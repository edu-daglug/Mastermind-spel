import random

# Huvudloop gör att hela spelet kan startas om efter en avslutad omgång
while True:
    val = ["1", "2", "3", "4", "5", "6"]

    #Den här utmatningen skriver ut reglerna på skärmen och hur man spelar
    print('''
    Datorn komer slumpa fram en kod på fyra sifror mellan 1 och 6.
    Du ska försöka gissa denna kods sifror på max 12 drag.
    Efter respektive gisning så kommer du att få en respons:
    För varje gissad korrekt siffra på korekt plats i koden: ✅
    För varje gissad korrekt siffra på fel plats i koden: ⬜
    För de sifror som inte finns med i koden ges ingen markering.

    Exempel: om den slumpade koden är 2315
    och du gissar 3165
    så blir responsen: ✅⬜⬜

    Du får välja mellan två svårighetsnivåer:¨
    Lättare nivå: Alla sifror är garanterat olika 
    Svårare nivå: Det kan finnas upprepade av en eller flera siffror
    ''')

    #Den här lopen frågar användaren om önskad svårighetsnivå och genererar en slumpad kod baserat på det valet
    while True:
        svårighetsnivå = input("Ange önskad nivå: lättare (1), svårare (2) ->")
        
        if svårighetsnivå == "1":
            #Slumpar fram fyra olika siffror mellan 1 och 6
            gissatal = random.sample(val, 4)
            break
        
        elif svårighetsnivå == "2":
            #Slumpar fram fyra siffror mellan 1 och 6, med möjlighet till upprepning
            gissatal = [random.choice(val) for _ in range(4)]
            break
        
        else:
            print("Ogiltigt val. Försök igen.")
   # Räknare för hur många siffror som är på exakt rätt plats
    drag = []

# Spelomgången pågår så länge spelaren har gjort färre än 12 drag
    while len(drag) < 12:
        gissning = input("Ange en gissning som följd af fyra siffror -> ")
# Kontrollerar att gissningen är exakt 4 tecken lång och bara innehåller siffrorna 1–6

        if len(gissning) != 4 or any(char not in val for char in gissning):
            print("Ogiltig gissning. Ange fyra siffror mellan 1 och 6.")
            continue

# På lättare nivå kontrolleras att inga siffror upprepas (set tar bort dubbletter)
        if svårighetsnivå == "1" and len(set(gissning)) != 4:
            print("Ogiltig gissning. På lättare nivå får inga siffror upprepas.")
            continue

# Skapar kopior av koden och gissningen som listor så vi kan bocka av träffar
        kod_kopia = list(gissatal)
        gissning_kopia = list(gissning)

# Nollställer räknarna inför kontrollen av den nya gissningen
        rätt_plats = 0
        rätt_siffra = 0

# Steg 1: Letar efter siffror som står på exakt rätt plats
        for i in range(4):
            if kod_kopia[i] == gissning_kopia[i]:
                rätt_plats += 1
                # Markerar siffrorna som förbrukade (None) så de inte dubbelräknas i steg 2
                kod_kopia[i] = None
                gissning_kopia[i] = None

# Steg 2: Letar efter siffror som finns med i koden men står på fel plats
        for i in range(4):
            if gissning_kopia[i] is not None:
                if gissning_kopia[i] in kod_kopia:
                    rätt_siffra += 1
                    # Markerar den hittade siffran i koden som förbrukad
                    kod_kopia[kod_kopia.index(gissning_kopia[i])] = None

# Bygger ihop feedback-strängen med bockar och rutor
        feedback = "✔" * rätt_plats + "□" * rätt_siffra

# Sparar gissningen och feedbacken som en tupel i historiklistan
        drag.append((gissning, feedback))

# Skriver ut tabellhuvudet för spelplanen med jämn kolumnbredd
        print()
        print(f"{'Drag #':<15}{'Drag':<25}Feedback")
        print("-" * 50)

# Ritar ut alla 12 rader uppifrån och ner (från drag 12 ner till drag 1)
        for nummer in range(12, 0, -1):
            if nummer <= len(drag):
                # Hämtar och skriver ut tidigare gjorda drag och deras feedback
                g, f = drag[nummer - 1]
                print(f"{nummer:<15}{' '.join(g):<25}{f}")
            else:
                # Skriver bara ut radnumret för drag som ännu inte har gjorts
                print(nummer)

# Om alla 4 siffror är på rätt plats har spelaren vunnit och loopen avbryts
        if rätt_plats == 4:
            print("\nGrattis! Du har knäckt koden!")
            break

# Om alla 12 drag är förbrukade och sista gissningen inte var helt rätt avslöjas koden
    if len(drag) == 12 and drag[-1][1] != "✔✔✔✔":
        print("\nDu har slut på dina drag!")
        print("Den rätta koden var:", "".join(gissatal))

        # Frågar om spelaren vill spela en ny omgång eller avsluta
    while True:
        spela_igen = input("Vill du spela igen? (j/n) -> ")
        if spela_igen == "j":
            # Avbryter denna inre loop så att den yttre huvudloopen startar ett nytt spel
            break
        elif spela_igen == "n":
            print("Tack för att du spelade!")
            # Avslutar hela programmet omedelbart
            exit()
        else:
            print("Ogiltigt val. Försök igen.")
# Denna rad nås aldrig eftersom exit() stänger programmet ovan
print("Programmet avslutas.")