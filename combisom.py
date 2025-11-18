def combisom(lijst, getal : int):

    for i in range(len(lijst)-1):
        for j in range(i+1,len(lijst)):
            if getal == lijst[i] + lijst[j]:
                return True

    return False