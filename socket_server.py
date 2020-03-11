import socket
#import win32com.client
import time

PORT_NUMBER = 8080
SIZE = 1024
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('192.168.4.1', PORT_NUMBER))
mySocket.listen(1)
print("Listening for incoming connections")
conn, addr = mySocket.accept()
#app = win32com.client.Dispatch("PowerPoint.Application")
#presentation = app.Presentations.Open(FileName=r"C:\Users\LE00068\Desktop\Leonards\kest.pptx", ReadOnly=1)
#presentation.SlideShowSettings.Run()
while True:
    
    data = conn.recv(1024)
    decoded = data.decode()
    
    if data == b'next':
       
        print(decoded)
    elif data == b'prev':
       
        print(decoded)
    elif data == b'end':
      
        break
    else:
        
        print("shithappens")
        break




#app.Quit()
conn.close()
mySocket.close()