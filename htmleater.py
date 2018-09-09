def htmleater(file):
    '''
    Program that eats superfluous HTML and produces a list of option codes for use in another program
    '''

    fileopen = open(file, 'r')
    pieces = []
    codes = []
    number = 0
    
    for line in fileopen:
        pieces.extend(line.split('"'))
    
    for piece in pieces:
        if len(piece) < 5:
            codes.append(piece)
        else:
            pass

    listopen = open('list.txt', 'a')
    for code in codes:
        number += 1
        listopen.write(code)
        listopen.write("\n")
        
    fileopen.close()
    listopen.close()

    print(number)

# Main

file = "classcodes.txt"
htmleater(file)
