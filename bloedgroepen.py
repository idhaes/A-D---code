allelen = {'A': [('A', 'A'), ('A', 'O')], 'B': [('B', 'B'), ('B', 'O')], 'AB': [('A', 'B')], 'O': [('O', 'O')],
           '+': [('+', '+'), ('+', '-')], '-': [('-', '-')]}


def split_bloedgroep(bg):
    return bg[:-1], bg[-1]


def combinatie(ABOs, rhesusfactor):
    bloedgroepen = set()
    for ABO in ABOs:
        for rhesus in rhesusfactor:
            bloedgroepen.add(ABO + rhesus)
    return bloedgroepen


def bloedgroep(a1, a2):
    allelen = {a1, a2}
    if allelen == {'O'}:
        return 'O'
    if 'A' in allelen and 'B' in allelen:
        return 'AB'
    if 'A' in allelen:
        return 'A'
    if 'B' in allelen:
        return 'B'
    if allelen == {'-'}: #Moet de set vergeljken, {} noodzakelijk !!!
        return '-'
    else:
        return '+'


def bloedgroep_kind(vader: str, moeder: str):
    ABO_vader, rhesus_vader = split_bloedgroep(vader)
    ABO_moeder, rhesus_moeder = split_bloedgroep(moeder)

    def kind(vader, moeder):
        lijst = set()
        for alellen_vader in allelen[vader]:
            for allelen_moeder in allelen[moeder]:
                for allel_vader in alellen_vader:
                    for allel_moeder in allelen_moeder:
                        lijst.add(bloedgroep(allel_vader, allel_moeder))
        return lijst

    ABO_kind = kind(ABO_vader, ABO_moeder)
    rhesus_kind = kind(rhesus_vader, rhesus_moeder)

    bloedgroepen_kind = combinatie(ABO_kind, rhesus_kind)
    return bloedgroepen_kind


def bloedgroep_ouder(ouder: str, kind: str):
    ABOs = ['O', 'A', 'B', 'AB']
    rhesusfactor = ['-', '+']

    bloedgroep_ouder = set()

    for ABO in ABOs:
        for rhesus in rhesusfactor:
            kandidaat = ABO + rhesus  # gaat elke mogelijke combo af
            # als het kind mogelijk is uit (ouder, kandidaat), dan is dit een geldige bloedgroep voor de andere ouder
            if kind in bloedgroep_kind(ouder, kandidaat):
                bloedgroep_ouder.add(kandidaat)
    return bloedgroep_ouder