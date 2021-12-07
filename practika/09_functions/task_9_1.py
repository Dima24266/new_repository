access_mode_template = [
"switchport mode access", "switchport access vlan",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]
access_config = {
"FastEthernet0/12": 10,
"FastEthernet0/14": 11,
"FastEthernet0/16": 17
}

def generate_access_config(intf_vlan_mapping, access_template):
    for i in intf_vlan_mapping.keys():
        restr = access_template[1]
        access_template[1] += ' ' + str(intf_vlan_mapping[i])
        print('interface ', end = '')
        print(i, end = '\n')
        print(*access_template, sep = '\n')
        access_template[1] = restr
generate_access_config(access_config, access_mode_template)
