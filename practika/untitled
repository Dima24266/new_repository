with open('config_sw1.txt') as f:
    ignore = ["duplex", "alias", "configuration", "!"]
    for line in f:
        flag = True
        for ig in ignore:
            if ig in line:
                flag = False
        if flag:
            print(line.strip())
