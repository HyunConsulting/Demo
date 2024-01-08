import psutil
import time
import sys
import pypyodbc as odbc

import datetime

def getTimeNow(variant):
    if variant=='YMD':
        time=datetime.datetime.now().strftime("%Y-%m-%d")
    else:
        time=datetime.datetime.now().strftime("%y-%m-%d")
    return time

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'HYUNCONSULTING'
DATABASE_NAME = 'DEMODB'
username = 'DEMODB_ADMIN'
password = 'jons00580*'

conn_string = f"""
    Driver={{{DRIVER_NAME}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    uid={username};
    pwd={password};
"""

try:
    conn = odbc.connect(conn_string)
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    cursor=conn.cursor()

while 1==1:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]
    sql=f"INSERT INTO dbo.Python_Performance (time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage  ) \
         VALUES ({getTimeNow('YMD')}, {str(cpu_usage)}, {str(memory_usage)}, {str(cpu_interrupts)}, {str(cpu_calls)}, {str(memory_used)}, {str(memory_free)}, {str(bytes_sent)}, {str(bytes_received)},{str(disk_usage)} )"
    # sql='INSERT INTO dbo.Python_Performance  VALUES (GETDATE(),' + str(cpu_usage) +',' + str(cpu_interrupts) + ','  + str(memory_usage) + ','  + str(cpu_calls) + ',' + str(memory_free) + ',' + str(bytes_sent) + ',' + str(bytes_received) + ',' + str(disk_usage) + ')'
    cursor.execute(sql)
    conn.commit()
   
    print(cpu_usage)
    time.sleep(1)
conn.close()   
