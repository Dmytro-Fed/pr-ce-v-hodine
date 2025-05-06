cisla = [8,11,3,5,4]
hodnota = int(input("Zadejte číslo které chcete výbrat"))
nalezeno = False
for i in range(len(cisla)):
    if cisla[i] == hodnota:
        print(f"Je hodnota na pozici {i}")
        nalezeno = True
        break
    if not nalezeno:
        print("Hodnota neexistuje")
