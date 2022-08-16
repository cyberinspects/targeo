import requests
from bs4 import BeautifulSoup as soup 
import urllib3
urllib3.disable_warnings()
import argparse
from colorama import Fore
from argparse import RawTextHelpFormatter



parser = argparse.ArgumentParser(description=Fore.YELLOW+'Target range calculator and ip geo lookup tool.', formatter_class=RawTextHelpFormatter)

parser.add_argument('-t','--type', type=str,
                    help='Range type (Allowed types are continent,nation and region)')

parser.add_argument('-l','--ip', type=str,
                    help='Ip address to find geo-location')

parser.add_argument('-i','--input', type=str,
                    help='Input to specify the targeted range')

parser.add_argument('-o','--output',type=str,
                    help='Output path and name')


print(Fore.RED+"""
⣿⠚ ⠐⠒⠀⠀  ⠀⠀⢀⣠⣴⣶⣶⣿⣿⣿⣿⣷⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈
⣿⠀⠀ ⠤⠀  ⠀⣠⣶⣿⣿⣿⠿⠛⠛⠉⠉⠛⠛⠿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀
⡧⠀⠀⠀   ⢀⣼⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣧⡀⠀⠀⠀⠀
⡇ ⠀⠀  ⢠⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⡄⠀⠀⠀
⡏⠀ ⠀  ⣾⣿⡿⠁⠀⠀⠀⠀⢀⡴⠛⠙⡏⠙⢷⣄⠀⠀⠀⠀⠈⢿⣿⣷⠀⠀⠀
⡧ ⠀  ⢰⣿⣿⡇⠀⠀⠀⠀⢀⣟⠀⢀⣴⣧⡀⠀⢸⣆⠀⠀⠀⠀⢸⣿⣿⡆⠀⠀
⡇⠀   ⢸⣿⣿⡇⠀⠀⠀⠈⠉⣯⠉⠉⠻⡿⠋⠉⢹⡏⠉⠀⠀⠀⢸⣿⣿⡇⠀⠀
⡏⠀   ⠈⣿⣿⣧⠀⠀⠀⠀⠀⠘⢷⣄⣀⣇⣀⡴⠏⠀⠀⠀⠀⠀⣼⣿⣿⠁⠀⠀
⡧⠀   ⠀⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠉⡏⠁⠀⠀⠀⠀⠀⠀⣰⣿⣿⠇⠀⠀⠀
⡇ ⠀⠀ ⠀ ⠹⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠏⠀⠀⠀⠀
⡏⠀⠀⠀   ⠀⠙⢿⣿⣿⣷⣤⣀⣀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⡿⠋⠀⠀⠀⠀⠀
⡧⠀⠀ ⠀⠀  ⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⡇⠀ ⠀⠀ ⠀⠀ ⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀
⡏⠀⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠧⠀ ⠀⠀⠀⠀⠀ ⠀ ⠀⠀⠀⠀⠀⠛⢿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡏ 
⡏⠀ ⠀⠀⠀⠀   ⠀Target Any Thing
⠧ [@cyberinspects] [ @kaleemibnawar]
    """)

args = parser.parse_args()
request=''
types=str(args.type)
types.lower()
ip=str(args.ip)
inputs=str(args.input)
inputs.lower()
if args.output:
    output=args.output
if args.type:
    if types in ('nation','n','na','nat','nati','natio'):
        request=f'https://cyberinspects-targeo.herokuapp.com/nation/{inputs}'
    elif types in ('continent','c','co','con','conti','contin','contine','continen'):
        request=f'https://cyberinspects-targeo.herokuapp.com/continent/{inputs}'
    elif types in ('region','r','re','reg','regi','regio'):
        request=f'https://cyberinspects-targeo.herokuapp.com/region/{inputs}'
    else:
        print("Unknown target type was chosen!")
        exit()
elif args.ip:
    request=f'https://cyberinspects-targeo.herokuapp.com/geoip/{args.ip}'
else:
    print(Fore.RED+'Invalid or no target selected to be ranged. [use -h parameter to learn about targeo]')

if request!='':
    response = requests.post(request,verify=False)
    page=response.content
    page_soup = soup(page, "html.parser") 
    content=page_soup
    if args.output is not None:
        with open(output,'a+') as file:
            file.write(content)
    if str(content).strip()!="":
        print(Fore.GREEN+str(content))
    else:
        print('No data returned, Possibly you have asked a quey unknown to our system.')
else:
    pass






