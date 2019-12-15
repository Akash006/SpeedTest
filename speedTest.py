import speedtest
import csv
import os.path

fileName = "E:\\Python\\output_01.csv"

def app():
    with open(fileName, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(ReqAttributes)

def new():
    with open(fileName, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerow(ReqAttributes)

if __name__ == "__main__":
    servers = []
    threads = None

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)

    headers = s.results.csv_header().split(',')
    ListAttributes = s.results.csv().splitlines()
    ReqAttributes = ListAttributes[0].split(',')
    
    if os.path.isfile(fileName):
        app()
    else:
        new()
