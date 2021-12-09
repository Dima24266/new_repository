trunk_mode_template = [
"switchport mode trunk", "switchport trunk native vlan 999",
"switchport trunk allowed vlan"
]
trunk_config = {
"FastEthernet0/1": [10, 20, 30],
"FastEthernet0/2": [11, 30],
"FastEthernet0/4": [17]
}

def generate_access_config(access_config, access_template):
    for i in access_config.keys():
        restr = access_template[2]
        access_template[2] += ' ' + str(access_config[i]).strip("[]")
        print(i+": ", end='')
        print(*access_template, sep = ', ')
        access_template[2] = restr
        print()
generate_access_config(trunk_config, trunk_mode_template)
