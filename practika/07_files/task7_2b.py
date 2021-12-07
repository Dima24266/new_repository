with open('config_sw1.txt', 'r') as f, open('results2.txt', 'w') as g:
    ignore = ["duplex", "alias", "configuration", "!"]
    for line in f:
        flag = True
        for ig in ignore:
            if ig in line:
                flag = False
        if flag:
            print(line.strip())
            g.write(line)
