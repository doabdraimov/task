#!/usr/bin/env python3

int_mode = input('Enter interface mode (access/trunk):\n')
int_type = input('Enter interface type and number:\n')
vlans = input('Enter vlan(s):\n')


access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
# создаю пустой словарь 
a={} 
# записываю в словарь данные из темплейтов
a['access']=access_template
a['trunk']=trunk_template
#вытаскиваю из словоря access или trunk(что вводил пользователь) и пишем в перенеую b 
b=list(a[int_mode]) 
# это просто линия 
print('\n' + '-' * 30)
print('interface', int_type)
# форматирую b  и распечатываю 
print('\n'.join(b).format(vlans))
