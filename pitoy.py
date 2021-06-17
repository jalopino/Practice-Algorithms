while True:
    size = int(input())
    if size == -1:
        break
    counter =0
    spaceSize = size
    while counter < size:
        spaceSize -= 1
        spacePrint = 0
        space = ""
        while spacePrint < spaceSize:
            space += " "
            spacePrint += 1
        bodyCounter = 0
        bodySize = 2 * counter+1
        body = "*"
        while bodyCounter < bodySize:
            body += "*"
            bodyCounter += 1
        print(space+body)
        counter += 1
    counter -= 1
    while counter > 0:
        spaceSize += 1
        spacePrint = 0
        space = ""
        while spacePrint < spaceSize:
            space += ""
            spacePrint += 1
        bodyCounter = 0
        bodySize = 2 * counter
        body = " "
        while bodyCounter<bodySize:
            body += "*"
            bodyCounter += 1

        print(space+body)
        counter -=1