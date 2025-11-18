def sorteer(rij):
    n = len(rij)
    grootte = 1   # begin met sublists van grootte 1

    # helperfunctie om twee gesorteerde delen van rij te mergen
    def merge(left, middle, right):
        # maak kopieën van de linkse en rechtse deelrij
        L = rij[left:middle]
        R = rij[middle:right]

        i = j = 0
        k = left

        # merge totdat een van de twee lijsten op is
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                rij[k] = L[i]
                i += 1
            else:
                rij[k] = R[j]
                j += 1
            k += 1

        # reststukken toevoegen
        while i < len(L):
            rij[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            rij[k] = R[j]
            j += 1
            k += 1

    # iteratieve fases: 1, 2, 4, 8, 16, ...
    while grootte < n:
        for left in range(0, n, 2 * grootte):
            middle = min(left + grootte, n)
            right = min(left + 2 * grootte, n)
            merge(left, middle, right)

        grootte *= 2
