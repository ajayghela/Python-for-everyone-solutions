"""
Exercise 12.2: Change your socket program so that it counts the number of characters it has received 
and stops displaying any text after it has shown 3000 characters. 
The program should retrieve the entire document and count the total number of characters 
and display the count of the number of characters at the end of the document.

"""

import socket

try:
    url = input("Enter a URL:")
    host = url.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    print(cmd)
    cmd = cmd.encode()
    mysock.send(cmd)

    recieved = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        recieved += data
    
    recieved = recieved.decode()
    print(recieved[:3000])
    print(len(recieved))
    
    mysock.close()

except:
    print("improperly formatted or non-existent URL")