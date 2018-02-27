import gzip
import os
import socket

path = 'logs/'
outputFile = open('output_2.txt', 'w')
host_array = []

for file in os.listdir(path):
    file_path = path + file
    print(file_path)
    with gzip.open(file_path, 'r') as f:
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


print(len(host_array))

for i in range(len(host_array)):
    outputFile.write(host_array[i] + '\n')
