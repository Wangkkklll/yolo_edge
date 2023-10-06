import time
while True:
    time.sleep(1)
    with open('/home/ty/Desktop/gps_data.txt','r+')as f:
        content=f.read()
        #lines=f.readlines()
        num_lines=len(content.splitlines())/2
        f.seek(0)
        f.truncate()
        print("--------------------------")
        print(num_lines,"ftps")
        print(content)

