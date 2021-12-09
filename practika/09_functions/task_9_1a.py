access_mode_template = [
"switchport mode access", "switchport access vlan",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]
port_security_template = [
"switchport port-security maximum 2",
"switchport port-security violation restrict",
"switchport port-security"
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11,
"FastEthernet0/16": 17}

def generate_access_config(access_config, access_template, *port_security_template):
    for i in access_config.keys():
        restr = access_template[1]
        access_template[1] += ' ' + str(access_config[i])
        print('interface ', end = '')
        print(i, end = '\n')
        print(*access_template, sep = '\n')
        print(*port_security_template, sep = '\n')
        access_template[1] = restr
        print()
generate_access_config(access_config, access_mode_template, *port_security_template)
