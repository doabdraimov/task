IP = '192.168.3.1'

IP=IP.split('.')



 ip_template = '''
...: {:<8}  {:<8}  {:<8}  {:<8}
...: {:08b}  {:08b}  {:08b}  {:08b}
...: '''

print(ip_template.format(int(IP[0]),int(IP[1]),int(IP[2]),int(IP[3]),int(IP[0]),int(IP[1]),int(IP[2]),int(IP[3])))




a=int(IP[0])
b=int(IP[1])
c=int(IP[2])
d=int(IP[3])

print(ip_template.format(a,b,c,d,a,b,c,d))
