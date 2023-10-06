import serial
import time
import json
import requests
ser = serial.Serial("/dev/ttyUSB0",9600) #9600是GPS的波特率
while True:
    line = str(str(ser.readline()))
    # #打印所有串口数据
    # print(line)
    GNRMC_line = line
    # GNGLL_line = line
    # GNGLL_line = line
    if GNRMC_line.startswith("b\'$GNRMC"):
        print(GNRMC_line)
        GNRMC_line = str(GNRMC_line).split(',')  # 将line以“，”为分隔符
        #GNRMC_line格式为：["b'$GNRMC", '132558.000',    'A',    '3412.93903',  'N',  '11708.08969',  'E',      '0.00',            '0.00',             '081221',                '', '', "A*75\\r\\n'"]
        #GNRMC_line格式为：["b'$GNRMC", '当天UTC时间', 'A表示数据有效', '纬度',    'N-北', '精度',        'E-东', '对地速度，单位为节', '对地真航向，单位为度', '日期(dd 为日,mm为月,yy为年)', '', '', "A*75\\r\\n'"]
        print(GNRMC_line)  #查看数据类型
        # 时间转化省略（需要把UTC转化为北京时间）
        # Lat ddmm.mmmm 纬度，前2字符表示度，后面的字符表示分,需要转化为小数形式
        latitude = float(GNRMC_line[3][:2]) + float(GNRMC_line[3][2:])/60
        # Lon dddmm.mmmm 经度，前3字符表示度，后面的字符表示分,需要转化为小数形式
        longitude = float(GNRMC_line[5][:3]) + float(GNRMC_line[5][3:])/60
        print("纬度：  " + GNRMC_line[4] + " " + str(latitude))
        print("经度：  " + GNRMC_line[6] + " " + str(longitude))
        # time.sleep(1)
        
        rqs_headers={'content-Type':'application/json'}
        requrl='http://124.221.239.172:8080/location'
        new_data={"longitude":longitude,"latitude":latitude}
        test_data = json.dumps(new_data)
        response = requests.post(url=requrl,headers=rqs_headers,data=test_data)
  
 