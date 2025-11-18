def samenvoegen(lijst1, lijst2):
    lijst3 = []
    kortste = min(len(lijst1,), len(lijst2))
    for i in range(kortste):
        lijst3.append(lijst1[i])
        lijst3.append(lijst2[i])
    return lijst3

def weven(lijst1, lijst2):
    lijst3 = []
    len1 = len(lijst1)
    len2 = len(lijst2)
    langste = max(len1, len2)

    for i in range(langste):
        lijst3.append(lijst1[i % len1])
        lijst3.append(lijst2[i % len2])

    return lijst3


def ritsen(lijst1, lijst2):
    lijst3 = []
    len1 = len(lijst1)
    len2 = len(lijst2)
    kortste = min(len1, len2)
    for i in range(kortste):
        lijst3.append(lijst1[i])
        lijst3.append(lijst2[i])

    for i in range(kortste, len1):
        lijst3.append(lijst1[i])

    for i in range(kortste, len2):
        lijst3.append(lijst2[i])
    return lijst3