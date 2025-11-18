def sort(lijst):
    sorthelper(lijst, 0, len(lijst) - 1) #moeten low en high kunnen definieren


def sorthelper(lijst, eerste, high):
    if eerste < high:
        index = pivotindex(lijst, eerste, high)     #GEEFT INDEX
        sorthelper(lijst, eerste, index - 1)    #SPLITST LIJST (= APARTE FUNCTIE)
        sorthelper(lijst, index + 1, high)


def pivotindex(lijst, eerste, high):
    pivot = lijst[eerste]
    low = eerste + 1

    while low < high:
        while low <= high and lijst[low] <= pivot: 
            low += 1
        while low <= high and lijst[high] > pivot:
            high -= 1
        if low < high:
            lijst[low], lijst[high] = lijst[high], lijst[low]
    while lijst[high] == pivot and eerste < high:  #
        high -= 1

    if pivot > lijst[high]:
        lijst[eerste] = lijst[high]
        lijst[high] = pivot
        return high
    else:
        return eerste