import sys
import logging
from pyzabbix import ZabbixAPI


# stream = logging.StreamHandler(sys.stdout)
# stream.setLevel(logging.DEBUG)
# log = logging.getLogger('pyzabbix')
# log.addHandler(stream)
# log.setLevel(logging.DEBUG)

def get_avg_cpuusedpercent(hostgroupname, itemname):    # 获取某主机组的cpu使用率
    # 获取token
    zapi = ZabbixAPI("http://zabbix.tqsys.cn/zabbix")
    zapi.login('Admin', 'zabbix@Tqls')

    # 获取ccs-prd主机组id，得到的格式为[{'groupid': '21'}]
    ccs_prd = zapi.hostgroup.get(output='groupid', filter={'name':hostgroupname})


    # 获取主机id，得到的格式为[{'hostid': '10400'}, {'hostid': '10403'}, {'hostid': '10404'}, {'hostid': '10405'}, {'hostid': '10406'}, {'hostid': '10407'}, {'hostid': '10408'}, {'hostid': '10409'}, {'hostid': '10411'}, {'hostid': '10412'}, {'hostid': '10413'}, {'hostid': '10414'}, {'hostid': '10415'}, {'hostid': '10416'}, {'hostid': '10417'}, {'hostid': '10418'}, {'hostid': '10419'}, {'hostid': '10420'}, {'hostid': '10421'}, {'hostid': '10422'}, {'hostid': '10424'}, {'hostid': '10425'}, {'hostid': '10426'}, {'hostid': '10427'}, {'hostid': '10430'}, {'hostid': '10431'}]
    hosts = zapi.host.get(output=('hostid',), groupids=(ccs_prd[0]['groupid'],))


    # 获取主机组所有主机的cpu使用率的itemid，得到格式为['40134', '40195', '40270', '40329', '40488', '40549', '40624', '40683', '40880', '40943', '41004', '41063', '41124', '41183', '41244', '41303', '41396', '41487', '41546', '41611', '41876', '41955', '42052', '42111', '42376', '42465']
    list_of_itemid = []         # 用来存储itemids
    for host in hosts:
        item = zapi.item.get(output='itemid', hostids=host['hostid'],filter={'name':itemname})
        list_of_itemid.append(item[0]['itemid'])


    # 获取ccs-prd主机的cpu使用率
    list_of_itemvalue = []
    for itemid in list_of_itemid:
        cpu_used_percent = zapi.history.get(history=0, itemids=itemid, limit=1)
        list_of_itemvalue.append(cpu_used_percent[0]['value'])

    # 求平均值
    print((list(map(float,list_of_itemvalue))))
    avg = sum((list(map(float,list_of_itemvalue))))/len((list(map(float,list_of_itemvalue))))
    # print(avg)
    return avg

avg_cpuusd_percent = get_avg_cpuusedpercent('ccs-prd','CPU utilization')
print(avg_cpuusd_percent)
