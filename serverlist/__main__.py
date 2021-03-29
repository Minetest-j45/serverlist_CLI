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
        if arg == 'totalclients':
            total = jsonserverlistinfo['total']
            print(total['clients'])
        if arg == 'totalservers':
            total = jsonserverlistinfo['total']
            print(total['servers'])
if __name__ == '__main__':
    main()
