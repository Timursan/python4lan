# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('O','OSPF')
ospf_route = ospf_route.replace(',',' ')
ospf_route = ospf_route.replace('[',' ')
ospf_route = ospf_route.replace(']',' ')
ospf_route = ospf_route.replace('via',' ')
ospf_route = ospf_route.split()
print(ospf_route)
template='''{0:*<23}{1:<23}
{2:*<23}{3:<23}
{4:*<23}{5:<23}
{6:*<23}{7:<23}
{8:*<23}{9:<23}
{10:*<23}{11:<23}'''
print("Вариант с шаблоном оформления:")
print(template.format('Protocol: ',ospf_route[0], 'Prefix: ',ospf_route[1],'AD/Metric: ',ospf_route[2],'Next-Hop: ',ospf_route[3],'Last update: ',ospf_route[4],'Outbound Interface: ',ospf_route[5]))
print()
print("Вариант с построчными принтами:")
print("{0:<23}{1:<23}".format('Protocol: ',ospf_route[0]))
print("{0:<23}{1:<23}".format('Prefix: ',ospf_route[1]))
print("{0:<23}{1:<23}".format('AD/Metric: ',ospf_route[2]))
print("{0:<23}{1:<23}".format('Next-Hop: ',ospf_route[3]))
print("{0:<23}{1:<23}".format('Last update: ',ospf_route[4]))
print("{0:<23}{1:<23}".format('Outbound Interface: ',ospf_route[5]))