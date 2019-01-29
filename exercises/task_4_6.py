ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route=ospf_route.split()

protocol=ospf_route[0].replace('O','OSPF')
ip=ospf_route[1]
metric=ospf_route[2].strip('[]') 
next_hop=ospf_route[4].rstrip(',')
last_update=ospf_route[5].rstrip(',')
outbound_interface=ospf_route[6]

sh_ip_route='''
Protocol:           {}
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''

 print(sh_ip_route.format(protocol,ip,metric,next_hop,last_update,outbound_interface)) 

#Пояснения
#разбиваем строку на части и присваиваем ее к тойже переменной и получаем 
#['O',
# '10.0.24.0/24',
# '[110/41]',
# 'via',
# '10.0.13.3,',
# '3d18h,',
# 'FastEthernet0/0'#]
#
# Обращаемся к [0] части и меняем там O на OSPF если есть
#ospf_route[0].replace('O','OSPF')
#Обращаемся к [1] части и достаем от туда Ip
#ip=ospf_route[1]
#Обращаемся к [2] части и достаем от туда метрику и срезаем лишнии скобки
#metric=ospf_route[2].strip('[]') 
#Обращаемся к [4] части и достаем от туда next hop и срезаем лишнию запятую
#next_hop=ospf_route[4].rstrip(',')
#Обращаемся к [6] части и достаем от туда интерфейс
#outbound_interface=ospf_route[6]
#
#Создаем переменую sh_ip_route и оставляем там места для форматирования {}
#sh_ip_route
#
#выводим на экран с форматированием
#print(sh_ip_route.format(protocol,ip,metric,next_hop,last_update,outbound_interface)) 
#
#
