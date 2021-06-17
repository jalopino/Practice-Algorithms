size = 0
while size >= 0:
    size = int(input())
    second = size
    lines = 0
    append = 0
    while size >= 1:
        string = ''
        number = 0
        while True:
            number = number + 1
            if (size == number):
                lines = lines + 1
                while True:
                    string = string + '*'
                    append = append + 1
                    if ((lines * 2) - 1 == append):
                        print(string)
                        append = 0
                        break
                break
            string = string + ' '
        size = size - 1
    limit = 0
    while True:
        if (second == 1):
            break
        string = ''
        limit = limit + 1
        while limit <= second - 1:
            append = append + 1
            string = string + ' '
            if (append == limit):
                while True:
                    size = size + 1
                    string = string + '*'
                    if ((second * 2) - ((limit * 2) + 1)  == size):
                        print(string)
                        size = 0
                        append = 0
                        break
                break
        if (limit == second - 1):
            break