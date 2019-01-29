ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route=ospf_route.split()

ospf_route[0].replace('O','OSPF')
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

