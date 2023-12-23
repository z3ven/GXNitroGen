import requests
import json
from discord import app_commands, Intents, Client, Interaction, Embed, Colour, Game
import webbrowser
import colorama
import pyfiglet

LOGO = [f"{colorama.Fore.RED}{pyfiglet.figlet_format('GX')}{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.MAGENTA}{pyfiglet.figlet_format('NITRO')}{colorama.Style.RESET_ALL}",
        f"{colorama.Fore.GREEN}{pyfiglet.figlet_format('GEN')}{colorama.Style.RESET_ALL}",
        ]


class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = Bot(intents=Intents.none())
config = json.load(open("config_copy.json", "r"))

@client.event
async def on_ready():
    print(f"{colorama.Fore.GREEN}Bot is running!{colorama.Style.RESET_ALL}")
    await client.change_presence(activity=Game(name="/help"))
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
    if config["proxies"] != {}: response = requests.post(url, headers=headers, json=data, proxies=config["proxies"])
    else: response = requests.post(url, headers=headers, json=data)

    try:
        if response.status_code == 200:
            json_out = json.loads(response.text)
            return json_out["token"]
        else:
            return "Something went wrong:" + response.status_code + response.text
    except Exception as e:
        return "Something went wrong: " + str(e)

@client.tree.command(name="help", description="Help. ")
async def helper(interaction: Interaction):
    await interaction.response.send_message(config["help_message"])

@client.tree.command(name="generate", description="Generate Discord Nitro gifts via GXNitroGen. ")
@app_commands.describe(amount="How much gifts do you need")
async def generate(interaction: Interaction, amount: int):
    await interaction.response.send_message("Working...")
    for i in range(1, amount + 1):
        token = get_token()
        if "Something went wrong" in token:
            error_embed = Embed(
                colour=Colour.red(),
                title="Something went wrong",
                description=token
            )
            error_embed.set_image(url=config['embed_images']['error_embed'])
            await interaction.followup.send(embed=error_embed,)

        link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"

        embed = Embed(
            colour=Colour.blurple(),
            title="Nitro Gift",
            description="Claim your nitro by clicking on the title",
            url=link
        )
        embed.set_image(url=config['embed_images']['embed'])
        await interaction.followup.send(embed=embed)


if __name__ == "__main__":
    colorama.init()
    print(f"{LOGO[0]}{LOGO[1]}{LOGO[2]}")
    print('\033[1m' + "Made by: z3ven" + '\033[0m')
    print('\033[1m' + "GitHub: https://github.com/z3ven/GXNitroGen/" + '\033[0m')
    print('\033[1m' + "Inviting bot....." + '\033[0m')
    webbrowser.open(
        f"https://discord.com/api/oauth2/authorize?client_id={config['client_id']}&permissions=277025441792&scope=bot")
    print('\033[1m' + "Running bot...." + '\033[0m')
    client.run(token=config['token'])
