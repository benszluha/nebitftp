from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import json

def server(ip_address, port, directory, user, password):
    auth = DummyAuthorizer()
    auth.add_user(user, password, directory, perm="elradfmw")

    handle = FTPHandler
    handle.authorizer = auth
    handle.banner = "Connected to NebitFTP"

    address = (str(ip_address), port)
    ftpServer = FTPServer(address, handle)

    return ftpServer

def loadConfig(configPath):
    with open(configPath, 'r') as file:
        config = json.load(file)

    return config

if __name__ == '__main__':
    ftpConfig = loadConfig("config.json")
    
    server_0 = ftpConfig['address']
    port_0 = ftpConfig['port']            
    directory_0 = ftpConfig['directory']
    user_0 = ftpConfig['username']      
    password_0 = ftpConfig['password']

    myServer = server(server_0, port_0, directory_0, user_0, password_0)
    myServer.serve_forever()