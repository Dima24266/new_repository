access = {
"1": "switchport mode access",
"2": "switchport access vlan",
"3": "switchport nonegotiate",
"4": "spanning-tree portfast",
"5": "spanning-tree bpduguard enable"
}
trunk = {
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan "
}

print('Введите режим работы интерфейса (access/trunk): ', end = '')
mode = str(input())
print('Введите тип и номер интерфейса: ', end = '')
intr = str(input())
if mode == 'trunk':
    print('Введите разрешенные VLANы: ', end = '')
elif mode == 'access':
    print('Введите номер VLAN: ', end = '')
vlan = str(input())

print('interface ' + intr)
if mode == 'access':
    print(access["1"])
    print(access["2"], vlan)
    print(access["3"])
    print(access["4"])
    print(access["5"])
elif mode == 'trunk':
    print(trunk["1"])
    print(trunk["2"])
    print(trunk["3"], vlan)
