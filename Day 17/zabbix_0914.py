"""
获取2021-09-13 17：00 到 2021-09-14 05：00之间的TMI_APP_PRD01主机的内存使用率
"""


from pyzabbix import ZabbixAPI
import time
# import matplotlib.pyplot as plt


start_time = time.strptime('2021-09-13 17:00:00', '%Y-%m-%d %H:%M:%S')  # 获取时间（元组）
start_time = int(time.mktime(start_time))   # 获取开始时间戳
end_time = time.strptime('2021-09-14 05:00:00', '%Y-%m-%d %H:%M:%S')
end_time = int(time.mktime(end_time))       # 获取截至时间戳




zapi = ZabbixAPI("http://zabbix.tqsys.cn/zabbix")
zapi.login('Admin', 'zabbix@Tqls')


# 获取40488指标的值
   # print(values)
values_dic = dict()
for value in values:
    time_struct = time.localtime(int(value['clock']))
    # print(time_struct)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_struct)
    # print(time_str)
    values_dic[time_str] = value['value']

print(values_dic)

