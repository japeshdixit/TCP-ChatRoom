'Chat Room Connection Client to Client'
import threading
import socket
host= '127.0.0.1'
port = 59000
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
aliases=[]
def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle_client(client):
    while True: 
        try:
            message=client.recv(1024) #maximum number of bytes of message
            broadcast(message)
        except:
            index= clients.index(client)
            clients.remove(client)
            client.close()
            alias=aliases[index]
            broadcast(f'{alias}Left the Chat '.encode)
            aliases.remove(alias)
            break
# Main function to recieve client's connections
def recieve():
    while True:
        print('Server is running and listening for connections ...')
        client,address=server.accept() #this method returns a nrew socket representing the connection and address of the client
        print(f'connection is established with address: {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias=client.recv(1024) #alias created with buffer size 1024
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this Client is {str(alias)}'.encode('utf-8'))
        broadcast(f'{alias} has connected to The Chat Room'.encode('utf-8'))
        client.send('You are now Connected to the Chat Room !!'.encode('utf-8'))
#Create and start a thread  to invoke handle_client
# python supports multi threading here
# individual thread for each connected client
#we want to recieve and send a message in same time  
# client should reieve the messaage instantaneously
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
if __name__ == "__main__":
    recieve()