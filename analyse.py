import gzip
import os
import socket

path = 'logs/'
outputFile = open('output.txt', 'w')
host_array = []
host_ip_array = []

file_path = os.listdir(path)[0]

with gzip.open(path + file_path, 'r') as f:
  for line in f:
    if('#' in line):
      continue
    splitted_line = line.split()
    # not ervery host is on position 15 ... and I dont know why
    host_1 = splitted_line[14]
    host_2 = splitted_line[15]
    host_3 = splitted_line[16]

    if host_1 not in host_array:
      host_array.append(host_1)
    if host_2 not in host_array:
      host_array.append(host_2)
    if host_3 not in host_array:
      host_array.append(host_3)


for host in host_array:
  try:
    ip_address = socket.gethostbyname(host)
    if(ip_address not in host_ip_array):
      host_ip_array.append(ip_address)
  except socket.gaierror, err:
    print("cannot resolve hostname: ", host, err)


for i in range(len(host_array)):
  outputFile.write(host_array[i] + " " + host_ip_array[i] + "\n")
