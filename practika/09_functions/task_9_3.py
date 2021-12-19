def get_int_vlan_map(config_filename):
    with open(config_filename):
        for i in access_config.keys():
            restr = access_template[2]
            access_template[2] += ' ' + str(access_config[i]).strip("[]")
            print(i+": ", end='')
            print(*access_template, sep = ', ')
            access_template[2] = restr
            print()
    with open(config_filename):

get_int_vlan_map('config_sw1.txt')
