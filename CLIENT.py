"""
Authentication-Client
"""
import socket
with open('__.steller','r') as f:
    __data=f.read()
    __data=__data.split(',')
_setup=(__data[0],int(__data[1]))

def check(username,password):
    try:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = 'login?#'+username+'#'+password
        socketObject.sendall(byte.encode())
        while(True):
            data = socketObject.recv(1024)
            socketObject.close()
            return data.decode()
    except ConnectionRefusedError:
        import os
        os.system('python bs4check.py')
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = 'login?#'+username+'#'+password
        socketObject.sendall(byte.encode())
        while(True):
            data = socketObject.recv(1024)
            socketObject.close()
            return data.decode()
def createacc(data): #list
    try:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = 'CreateNewAccount?'
        for i in data:
            byte+='#'+str(i)
        socketObject.sendall(byte.encode())
        socketObject.close()
        return True
    except ConnectionRefusedError:
        import os
        os.system('python bs4check.py')
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = 'CreateNewAccount?'
        for i in data:
            byte+='#'+str(i)
        socketObject.sendall(byte.encode())
        socketObject.close()
        return True

def send(from_user,from_name,to_user,to_name,title,data):
	try:
		socketObject = socket.socket()
		socketObject.connect((_setup))
		byte      = f'from#{from_user}#{from_name}#send#{to_user}#{to_name}#'
		byte+=str(data)+'#'+str(title)
		socketObject.sendall(byte.encode())
		socketObject.close()
		return True
	except ConnectionRefusedError:
		import os
		os.system('python bs4check.py')
		socketObject = socket.socket()
		socketObject.connect((_setup))
		byte      = f'from#{from_user}#{from_name}#send#{to_user}#{to_name}#'
		byte+=str(data)+str(title)
		socketObject.sendall(byte.encode())
		socketObject.close()
		return True

def fetch_username_to_name(uname):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getfullname#{uname}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode()
        

def recieve_inbox(username):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getinbox#{username}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode().split('##')

def recieve_outbox(username):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getoutbox#{username}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode().split('##')

def recieve_all(username):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getall#{username}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode().split('##')
def instantchat():
    pass

def get_msg_recv(yourusername,filename):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getmsgrecv#{yourusername}#{filename}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode()

def get_msg_recvout(yourusername,filename):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getmsgrecvout#{yourusername}#{filename}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode()

def get_msg_recvall(yourusername,filename):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'getmsgrecvall#{yourusername}#{filename}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode()

def abletomakeaccount(username):
    if True:
        socketObject = socket.socket()
        socketObject.connect((_setup))
        byte      = f'isExist#{username}'
        socketObject.sendall(byte.encode())
        while(True):
                    data = socketObject.recv(1024)
                    socketObject.close()
                    return data.decode()
    


#send('nks@steller','nitinkumarsharma','archie','Aaradhya Gupta','wishes','HII archie how are you')
#print(check('durgesh.rwt','incorrect'))
#print(recieve('archie'))
#print(get_msg_recv('durgesh@steller','nitinkumarsharma#test#Sat Feb 26 00:08:41 2022'))
