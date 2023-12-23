import requests
import json
import webbrowser
import colorama
import sys
import pyfiglet

LOGO = [f"{colorama.Fore.RED}{pyfiglet.figlet_format('GX')}{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.MAGENTA}{pyfiglet.figlet_format('NITRO')}{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.GREEN}{pyfiglet.figlet_format('GEN')}{colorama.Style.RESET_ALL}",
        ]
def exit_func(code: int):
    sys.exit(code)
def y_or_n(usrinp: str,y_func, n_func):
    inp = str(input(usrinp))
    if inp.lower() == "y":
        y_func.__call__()
    if inp.lower() == "n" and inp == "":
        n_func.__call__()
    else:
        exit_func(0)
    
def get_token() -> str:
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    }

    data = {
        'partnerUserId': '870aa19c5dcff83c25664d764f2040b3fd7109d0f2396992d1aa6e0cf2d56cb1',
    }

    response = requests.post(url, headers=headers, json=data)
    try: 
        if response.status_code == 200:
            json_out = json.loads(response.text)
            return json_out["token"]
        else:
            print('\033[1m' + colorama.Fore.RED + f"Something went wrong:" + '\033[0m' + colorama.Style.RESET_ALL + response.status_code + response.text)
    except Exception as e:
        print('\033[1m' + colorama.Fore.RED + f"Something went wrong:" + '\033[0m' + colorama.Style.RESET_ALL + str(e))
        exit_func(1)
if __name__ == "__main__":
    colorama.init()
    print(f"{LOGO[0]}{LOGO[1]}{LOGO[2]}")
    print('\033[1m' + "Made by: z3ven" + '\033[0m')
    print('\033[1m' + "GitHub: https://github.com/z3ven/GXNitroGen/" + '\033[0m')
    token = get_token()
    link = '\033[1m' + f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}" + '\033[0m'
    print("Link: " + link)
    def open_browser():
        webbrowser.open(link)
    y_or_n("Do you want to open link in the browser(Y for yes, N(also Enter key) for no): ", open_browser, exit)
