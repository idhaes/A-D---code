def woorden_splitsen(filename):
    woorden = []
    file = open(filename, 'r')
    #line = file.read()  # (1)
    for line in file: #(2)
        nieuw = ""
        for ch in line:
            if ch.isalpha():      # letter → behouden
                nieuw += ch
            else:                 # geen letter → scheiding
                nieuw += " "
        woorden.extend(nieuw.split())
    file.close()
    return woorden


def woorden_tellen(filename):
    woorden = woorden_splitsen(filename)
    telling = {}
    for woord in woorden:
        woord = woord.lower()
        if woord in telling:
            telling[woord] += 1
        else:
            telling[woord] = 1
    return telling