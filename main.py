import random
while True:
    val = ["1", "2", "3", "4", "5", "6"]
    gissatal = []

    
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

    print(' '.join(gissatal))
    
    
    
    break