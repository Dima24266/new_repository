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
print('Введите имя устройства: ')
a = input()
if a == 'r1':
    print(london_co['r1'])
elif a == 'r2':
    print(london_co['r2'])
elif a == 'sw1':
    print(london_co['sw1'])