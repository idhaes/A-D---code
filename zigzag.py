def iszigzag(reeks):
    n = len(reeks)
    for i in range(0, n, 2):  # 0 NIET VERGETEN!, alleen even indices
        if i - 1 >= 0 and reeks[i] < reeks[i - 1]: # eerste element heeft geen links
            return False
        if i + 1 < n and reeks[i] < reeks[i + 1]: # laatste index (=n-1) heeft geen rechts
            return False
    return True

def zigzag_traag(lijst):
    #if iszigzag(lijst) is False:
        lijst.sort()
        for i in range(0,len(lijst)-1,2):
            lijst[i], lijst[i+1] = lijst[i+1], lijst[i]

def zigzag_snel(lijst):
    #if iszigzag(lijst) is False:
    n = len(lijst)
    for i in range(0, n, 2):  # alle even posities overlopen
        if i - 1 >= 0 and lijst[i] < lijst[i - 1]:
            lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]
        if i + 1 < n and lijst[i] < lijst[i + 1]:
            lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]


#def zigzag_snel(lijst):
#    if iszigzag(lijst) is False:
#        if lijst[0] < lijst[1]:
#            lijst[0], lijst[1] = lijst[1], lijst[0]
#        for i in range(2,len(lijst) - 1,2):
#            if lijst[i] < lijst[i-1]:
#                lijst[i], lijst[i-1] = lijst[i-1], lijst[i]
#            if lijst[i] < lijst[i+1]:
#                lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
#        if len(lijst) % 2 == 1:
#            if lijst[-1] < lijst[-2]:
#                lijst[-1], lijst[-2] = lijst[-2], lijst[-1]