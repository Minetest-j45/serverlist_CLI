import sys
import requests
import json
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('You must have an argument')
        return
    
    
    serverlist =requests.get('https://servers.minetest.net/list')
    serverlistinfo = serverlist.text
    jsonserverlistinfo = json.loads(serverlistinfo)
    
    
    if len(args) == 1:
        arg = sys.argv[1]
        if arg == 'total_clients':
            total = jsonserverlistinfo['total']
            print(total['clients'])
            
        if arg == 'total_servers':
            total = jsonserverlistinfo['total']
            print(total['servers'])
        
        if arg == 'total_max_clients':
            total_max = jsonserverlistinfo['total_max']
            print(total_max['clients'])
            
        if arg == 'total_max_servers':
            total_max = jsonserverlistinfo['total_max']
            print(total_max['servers'])
        
        if arg == 'serverlist':
            print(serverlistinfo)
            
        if arg == 'users':
            print('You must put a servername after you say users')
            
    #for arg in args:
    if len(args) == 2:
        arg = sys.argv[1]
        arg2 = sys.argv[2]
        if arg == 'users':
            servers = jsonserverlistinfo['list']
            print(arg2)
            print(arg2.replace('\\', ' '))
            for server in servers:
                if server['name'] == arg2.replace('\\', ' '):
                    print(server['clients_list'])


if __name__ == '__main__':
    main()
