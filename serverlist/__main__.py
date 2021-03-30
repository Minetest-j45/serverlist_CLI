import sys
import requests
import json
def main():
    commandswithparam = {'address', 'clients', 'clients_list', 'clients_max', 'creative', 'damage', 'description', 'game_time', 'gameid', 'lag', 'name', 'password', 'port',
                         'proto_max', 'proto_min', 'pvp', 'server_id', 'uptime', 'version', 'ip', 'update_time', 'start', 'clients_top', 'dedicated', 'rollback', 'mapgen',
                         'privs', 'can_see_far_names', 'mods', 'updates', 'total_clients', 'pop_v', 'geo_continent', 'ping'}
    
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
        servers = jsonserverlistinfo['list']
        for command in commandswithparam:
            if arg == command:
                for server in servers:
                    if server['name'] == arg2.replace('//', ' '):
                        print(server[command])
        #if arg == 'users':
        #    for server in servers:
        #        if server['name'] == arg2.replace('//', ' '):
        #           print(server['clients_list'])
                    
        #if arg == 'ip':
        #    for server in servers:
        #        if server['name'] == arg2.replace('//', ' '):
        #            print(server['ip'])

    if len(args) > 2:
        arg = sys.argv[1]
        if arg == 'users':
            print('If you are trying to get the players of a server with a space in its name, replace the space with "//"')
        for command in commandswithparam:
            if arg == command:
                print('If you are trying to get the ',command,'of a server with a space in its name, replace the space with "//"')

if __name__ == '__main__':
    main()
