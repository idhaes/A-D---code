def mergesort(lijst):
    if len(lijst) > 1:  # wanneer len(lijst) = 1, krijgen links en rechts geen nieuwe waarden
        links = lijst[:len(lijst) // 2]
        mergesort(links)
        rechts = lijst[len(lijst) // 2:]
        mergesort(rechts)

        merge(links, rechts, lijst)

    return lijst # krijgt finaal de allerlaatste waarde (na de laatste merge)


def merge(links, rechts, lijst):  # lijst waarvan we nu de links en rechts hebben
    teller_links = 0
    teller_rechts = 0
    teller_lijst = 0

    while teller_links < len(links) and teller_rechts < len(rechts):  # while want 2 condities (en tellers)
        if links[teller_links] < rechts[teller_rechts]:
            lijst[teller_lijst] = links[teller_links]
            teller_lijst += 1
            teller_links += 1
        else:
            lijst[teller_lijst] = rechts[teller_rechts]
            teller_lijst += 1
            teller_rechts += 1

    while teller_links < len(links):
        lijst[teller_lijst] = links[teller_links]
        teller_lijst += 1
        teller_links += 1

    while teller_rechts < len(rechts):
        lijst[teller_lijst] = rechts[teller_rechts]
        teller_lijst += 1
        teller_rechts += 1