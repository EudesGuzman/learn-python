def number_of_bottles():
    fraseUno = " bottles of milk on the wall "
    fraseDos = " bottles of milk "
    fraseTres = "Take one down, pass it around. "
    fraseCuatro = "No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more"

    for i in range(99,-1,-1):
        if i >= 1:
            print( str(i) + fraseUno + str(i) + fraseDos + fraseTres)
        elif i == 0:
            print( str(i) + fraseUno.replace("bottles","bottle") + str(i) + fraseDos.replace("bottles","bottle") + fraseTres + fraseCuatro)



number_of_bottles()