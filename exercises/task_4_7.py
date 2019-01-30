MAC = 'AAAA:BBBB:CCCC'
MAC=MAC.replace('A','10:').replace('B','11:').replace('C','12:').replace('D','13:').replace('E','14:').replace('F','15:').replace(':',' ').split()

mac_template = '''{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}'''

print(mac_template.format(
 bin(int(MAC[0]))
,bin(int(MAC[1]))
,bin(int(MAC[2]))
,bin(int(MAC[3]))

,bin(int(MAC[4]))
,bin(int(MAC[5]))
,bin(int(MAC[6]))
,bin(int(MAC[7]))

,bin(int(MAC[8]))
,bin(int(MAC[9]))
,bin(int(MAC[10]))
,bin(int(MAC[11])))
)

