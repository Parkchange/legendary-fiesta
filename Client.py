from socket import *
import time
#client
def main():
    message= input("data:")
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(("192.168.0.8", 88))
   ## for _ in range(10):
        #client.sendall(b"Hello Server")
    client.sendall(str.encode(message))
    data = client.recv(1024)
    print(data)
    client.close()
    time.sleep(2)
    main()

if __name__ == "__main__":
    main()