CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONFIG.lstrip('switchport trunk allowed vlan ').split(',')
