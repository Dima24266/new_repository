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
access_config_2 = {
"FastEthernet0/03": 100,
"FastEthernet0/07": 101,
"FastEthernet0/09": 107,
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
