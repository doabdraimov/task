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
a={} 

a['access']=access_template
a['trunk']=trunk_template

b=list(a[int_mode]) 

print('\n' + '-' * 30)
print('interface', int_type)
print('\n'.join(b).format(vlans))
