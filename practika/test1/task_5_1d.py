london_co = {
"r1":{
	"location": "21 New Globe Walk",
	"vendor": "Cisco",
	"model": "4451",
	"ios": "15.4",
	"ip": "10.255.0.1"
},
"r2":{
	"location": "21 New Globe Walk",
	"vendor": "Cisco",
	"model": "4451",
	"ios": "15.4",
	"ip": "10.255.0.2"
},
"sw1":{
	"location": "21 New Globe Walk",
	"vendor": "Cisco",
	"model": "3850",
	"ios": "3.6.XE",
	"ip": "10.255.0.101",
	"vlans": "10,20,30",
	"routing": True
}}
print('Введите имя устройства: ', end='')
a = input()

if a == 'sw1':
    print('Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ', end='')
elif a == 'r2' or a == 'r1':
    print('Введите имя параметра (location, vendor, model, ios, ip): ', end='')
b = input()
b = b.lower()

if b not in london_co[a]:
    print('Такого параметра нет')

elif a == 'r1':
    print(london_co['r1'][b])
elif a == 'r2':
    print(london_co['r2'][b])
elif a == 'sw1':
    print(london_co['sw1'][b])
