import speedtest
import csv
import os.path
import numpy as np
from datetime import datetime

headers = []
#ListAttributes = []
#ReqAttributes = []
_Mbps = []
_header = []

def app():
    with open(fileName, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(_Mbps)

def new():
    with open(fileName, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(_header)
        csvwriter.writerow(_Mbps)

if __name__ == "__main__":
    date = datetime.date(datetime.now())
    fileName = "D:\\SpeedTest\\output\\{0}.csv".format(date)
    
    servers = []
    threads = None

    try:
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
    except Exception as e:
        print("No Speed")
    else:
        headers = s.results.csv_header().split(',')
        ListAttributes = s.results.csv().splitlines()
        ReqAttributes = ListAttributes[0].split(',')
        narray = np.asarray(ReqAttributes)
        harray = np.asarray(headers)

    for y in range(10):
        print(harry[y] + '  :  ' + narry[y])

    for x in range(10):
        if(x==3):
            time = datetime.time(datetime.now())
            _Mbps.append(time)
        if(x==6):
            d = int(float(narray[x])//1000000)
            _Mbps.append(d)
            _header.append(harray[x])
        elif(x==7):
            u = int(float(narray[x])//1000000)
            _Mbps.append(u)
            _header.append(harray[x])
        elif(x==9):
            pass
        else:
            _Mbps.append(narray[x])
            _header.append(harray[x])

    print(_Mbps)
    print(_header)

    if os.path.isfile(fileName):
        app()
    else:
        new()
