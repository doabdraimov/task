command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

a=set(command1.lstrip('switchport trunk allowed vlan ').split(','))
b=set(command2.lstrip('switchport trunk allowed vlan ').split(','))

a & b  
or 
a.intersection(b)


