import random
while True:
    val = ["1", "2", "3", "4", "5", "6"]
    drag = []

    
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
    while True:
        svårighetsnivå = input("Nnge önskad nivå: lättare (1), svårare (2) ->")
        if svårighetsnivå == "1":
            gissatal = random.sample(val, 4)
            break
        elif svårighetsnivå == "2":
            gissatal = [random.choice(val) for _ in range(4)]
            break
        else:
            print("Ogiltigt val. Försök igen.")

    drag = []
    
    rätt_plats = 0

    while len(drag) < 12:
        gissning = input("Ange en gissning som följd af fyra siffror -> ")

        if len(gissning) != 4 or any(char not in val for char in gissning):
            print("Ogiltig gissning. Ange fyra siffror mellan 1 och 6.")
            continue

        if svårighetsnivå == "1" and len(set(gissning)) != 4:
            print("Ogiltig gissning. På lättare nivå får inga siffror upprepas.")
            continue

        kod_kopia = list(gissatal)
        gissning_kopia = list(gissning)

        rätt_plats = 0
        rätt_siffra = 0

        for i in range(4):
            if kod_kopia[i] == gissning_kopia[i]:
                rätt_plats += 1
                kod_kopia[i] = None
                gissning_kopia[i] = None

        for i in range(4):
            if gissning_kopia[i] is not None:
                if gissning_kopia[i] in kod_kopia:
                    rätt_siffra += 1
                    kod_kopia[kod_kopia.index(gissning_kopia[i])] = None

        feedback = "✔" * rätt_plats + "□" * rätt_siffra

        drag.append((gissning, feedback))

        print()
        print(f"{'Drag #':<15}{'Drag':<25}Feedback")
        print("-" * 50)

        for nummer in range(12, 0, -1):
            if nummer <= len(drag):
                g, f = drag[nummer - 1]
                print(f"{nummer:<15}{' '.join(g):<25}{f}")
            else:
                print(nummer)

        if rätt_plats == 4:
            print("\nGrattis! Du har knäckt koden!")
            break

    if len(drag) == 12 and drag[-1][1] != "✔✔✔✔":
        print("\nDu har slut på dina drag!")
        print("Den rätta koden var:", "".join(kod))

    break