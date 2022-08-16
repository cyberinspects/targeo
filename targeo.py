import requests
from bs4 import BeautifulSoup as soup 
import urllib3
urllib3.disable_warnings()
import argparse
from colorama import Fore
parser = argparse.ArgumentParser(description='Target range calculator and ip geo lookup tool.')
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
print(Fore.YELLOW+"Results are being loaded:")

args = parser.parse_args()
cookies = {}
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
        print("Unknown range type was chosen!")
        exit()

elif args.ip:
    request=f'https://cyberinspects-targeo.herokuapp.com/geoip/{args.ip}'
else:
    print('none')


response = requests.post(request,verify=False)
page=response.content
page_soup = soup(page, "html.parser") 
content=page_soup

if args.output is not None:
    with open(output,'a+') as file:
        file.write(content)
print(Fore.GREEN+str(content))








