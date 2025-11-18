def tel(lst):
    teller = {}
    for getal in lst:
        if getal in teller:
            teller[getal] += 1
        else:
            teller[getal] = 1
    return teller


def dubbel(lst):
    gezien = set()
    for getal in lst:
        if getal in gezien:
            return getal
        gezien.add(getal)
    return None

# for key in teller:
    # telling[teller.get(key)] = key


def dubbels(lst):
    teller = tel(lst)
    enkel= set()
    meerdere = set()
    for getal, aantal in teller.items():
        if aantal == 1:
            enkel.add(getal)
        else:
            meerdere.add(getal)
    return enkel, meerdere

#lijst = list(teller.items())
    # for i in range(len(lijst)):
        # if lijst[i][1] == 1:
            # enkel.add(lijst[i][0])
        # else:
            # meerdere.add(lijst[i][0])