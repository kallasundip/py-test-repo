with open("details.txt") as f:
    txt = []

    for line in f:
        txt.append(line)
    print("-----")
    # print(txt[0])
    size = len(txt)
    count = 0
    while True:
        x = txt[count]
        print(x)
        count += 1
        if count>=size:
            break


    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line)
f.close()
