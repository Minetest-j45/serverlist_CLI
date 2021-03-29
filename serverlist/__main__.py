import sys
import requests
import json
def main():
    print('in main')
    args = sys.argv[1:]
    if len(args) == 0:
        print('You must have an argument')
        return
    serverlist =requests.get('https://servers.minetest.net/list')
    serverlistinfo = serverlist.text
    jsonserverlistinfo = json.loads(serverlistinfo)
    #print(serverlistinfo)
    #print('count of args :: {}'.format(len(args)))
    for arg in args:
        if arg == 'totalclients':
            total = jsonserverlistinfo['total']
            print(total['clients'])
    #    print('passed argument :: {}'.format(arg))
if __name__ == '__main__':
    main()
