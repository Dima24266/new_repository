infiles = [
"sp_cdp_n_sw1.txt",
"sh_cdp_n_r1.txt",
"sh_cdp_n_r2.txt",
"sh_cdp_n_r3.txt",
]
d = []
with open("sh_cdp_n_sw1.txt") as text:
    ospf = text.readlines()[0]
    print(ospf)
    b_device = ospf[0:2]
d.append(b_device)
def parse_cdp_neighbors(command_output):
    with open("sh_cdp_n_sw1.txt") as text:
        ospf = text.readlines()
        if lines.find("Eth") != -1:
            device = lines[0:2]
            d.append(device)
        d.sort()
        for lines in ospf:
            if lines.find(d[d.index(b_device) +1]) != -1:
                port = (lines[-8:-1])
                local = " ".join(lines.split()[1:3])
                device = "".join(lines.split()[0])
                eth_list = {b_device : local, device : port}
                print(eth_list)
            if lines.find(d[d.index(b_device) - 1]) != -1:
                port = (lines[-8:-1])
                local = " ".join(lines.split()[1:3])
                device = "".join(lines.split()[0])
                eth_list = {b_device : local, device : port}
                print(eth_list)
parse_cdp_neighbors(ospf)
