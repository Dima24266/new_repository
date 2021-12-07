with open('ospf.txt') as f:
    for line in f:
        s2 = line.split()[2]
        s3 = line.split()[4]
        s4 = line.split()[5]
        print('Prefix                ', line.split()[1])
        print('AD/Metric             ', s2[1:7])
        print('Next-Hop              ', s3[0:9])
        print('Last update           ', s4[0:5])
        print('Outbound Interface    ', line.split()[6])
        print()
