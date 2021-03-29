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
    #print(serverlistinfo)
    for arg in args:
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
if __name__ == '__main__':
    main()
