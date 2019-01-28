все в одной строке 

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

set(command1.lstrip('switchport trunk allowed vlan ').split(',')) & set(command2.lstrip('switchport trunk allowed vlan ').split(',')) 

#пояснения
#или так, по строчно, чуть понятней  
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

a=set(command1.lstrip('switchport trunk allowed vlan ').split(','))
b=set(command2.lstrip('switchport trunk allowed vlan ').split(','))

a & b  
or 
a.intersection(b)


###########
#пояснения по строчно
#удалеяем левую часть списка
command1.lstrip('switchport trunk allowed vlan ') 
#разбиваем список на части по разделителю (,)
command1.split(','))
#преобразуем список в множества
a=set(command1.lstrip('switchport trunk allowed vlan ').split(','))
#получаем пересения множества 
a & b  или еще можно a.intersection(b)
