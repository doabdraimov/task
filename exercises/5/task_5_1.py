#!/usr/bin/env python3
#Просим вести ip адрес сети и маску в формате х.х.х.х/х. Сразу же разделяем по "/" 
ip_subnet = input('Type ip address and mask\n').split('/')
#Вытаскиваю сеть
ip_octets = ip_subnet[0].split('.')
#Вытаскиваю короткую маску
short_mask = int(ip_subnet[1])
#Создаем список в формате 111111111111111111111111
bits = '1' * 32

#Преобразовываю биты в битовую маску. Пример последний октет 11110000
bit_mask = "{:0<32}".format(bits[:short_mask])
#Калькулятор из битовой маски (11110000) в десятичню формата 255.255.255.0
octet_a = ((int(bit_mask[0]) * 2 ** 7) +
           (int(bit_mask[1]) * 2 ** 6) +
           (int(bit_mask[2]) * 2 ** 5) +
           (int(bit_mask[3]) * 2 ** 4) +
           (int(bit_mask[4]) * 2 ** 3) +
           (int(bit_mask[5]) * 2 ** 2) +
           (int(bit_mask[6]) * 2 ** 1) +
           (int(bit_mask[7]) * 2 ** 0))

octet_b = ((int(bit_mask[8]) * 2 **  7) +
           (int(bit_mask[9]) * 2 **  6) +
           (int(bit_mask[10]) * 2 ** 5) +
           (int(bit_mask[11]) * 2 ** 4) +
           (int(bit_mask[12]) * 2 ** 3) +
           (int(bit_mask[13]) * 2 ** 2) +
           (int(bit_mask[14]) * 2 ** 1) +
           (int(bit_mask[15]) * 2 ** 0))

octet_c = ((int(bit_mask[16]) * 2 ** 7) +
           (int(bit_mask[17]) * 2 ** 6) +
           (int(bit_mask[18]) * 2 ** 5) +
           (int(bit_mask[19]) * 2 ** 4) +
           (int(bit_mask[20]) * 2 ** 3) +
           (int(bit_mask[21]) * 2 ** 2) +
           (int(bit_mask[22]) * 2 ** 1) +
           (int(bit_mask[23]) * 2 ** 0))

octet_d = ((int(bit_mask[24]) * 2 ** 7) +
           (int(bit_mask[25]) * 2 ** 6) +
           (int(bit_mask[26]) * 2 ** 5) +
           (int(bit_mask[27]) * 2 ** 4) +
           (int(bit_mask[28]) * 2 ** 3) +
           (int(bit_mask[29]) * 2 ** 2) +
           (int(bit_mask[30]) * 2 ** 1) +
           (int(bit_mask[31]) * 2 ** 0))
#Ну тут просто темплейт для вывода
ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
Mask:
/{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}
'''
#Ну и форматирую полученные данные и распечатываю
print(ip_template.format(int(ip_octets[0]), int(ip_octets[1]), int(ip_octets[2]), int(ip_octets[3]), (short_mask), octet_a, octet_b, octet_c, octet_d))
