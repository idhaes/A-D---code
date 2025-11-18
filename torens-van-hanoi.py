#Tail recursion NIET mogelijk, door de structuur van het probleem.

def hanoi(n):
    aantal = helper_hanoi(n, 'A', 'B', 'C', 1)
    print(aantal, 'stappen gedaan')

def helper_hanoi(n, origin, hulp, doel, aantal):
    if n == 1:
        print('Schijf', n, 'van', origin, 'naar', doel)
        return 1
    else:
        aantal = helper_hanoi(n - 1, origin, doel, hulp, aantal + 1) #aantal definieren / return aantal (einde) opvangen
        print('Schijf', n, 'van', origin, 'naar', doel)
        aantal += 1
        aantal += helper_hanoi(n - 1, hulp, origin, doel, aantal + 1)
        return aantal
