def is_geldig_isbn13(code):
    if len(code) != 13:
        return False
    if code[:3] not in ("978", "979"):
        return False
    o = e = 0
    for i in range(12):  # eerste 12 cijfers
        cijfer = int(code[i])
        if i % 2 == 0:       # posities 0,2,4,... -> factor 1
            o += cijfer
        else:                # posities 1,3,5,... -> factor 3
            e += cijfer
    controle = (10 - ((o + 3*e) % 10)) % 10
    return controle == int(code[12])


def overzicht(isbn_lijst):
    telling = {"Engelstalige landen": 0,"Franstalige landen": 0,"Duitstalige landen": 0,"Japan": 0,"Russischtalige landen": 0,"China": 0,"Overige landen": 0,"Fouten": 0}
    for code in isbn_lijst:
        if not is_geldig_isbn13(code):
            telling["Fouten"] += 1
        else:
            groepcijfer = code[3]  # vierde cijfer (index 3)
            
            if groepcijfer in ("0", "1"):
                telling["Engelstalige landen"] += 1
            elif groepcijfer == "2":
                telling["Franstalige landen"] += 1
            elif groepcijfer == "3":
                telling["Duitstalige landen"] += 1
            elif groepcijfer == "4":
                telling["Japan"] += 1
            elif groepcijfer == "5":
                telling["Russischtalige landen"] += 1
            elif groepcijfer == "7":
                telling["China"] += 1
            else:  # 6, 8, 9
                telling["Overige landen"] += 1
                
    for naam in telling:
        print(naam + ": " + str(telling[naam]))