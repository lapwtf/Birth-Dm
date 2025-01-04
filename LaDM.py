import discord
import asyncio
import aiohttp
from discord.ext import commands
from colorama import Fore
from pystyle import *
import ctypes
import os
import random

w = Fore.WHITE
mkk = Fore.BLUE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
psi = Fore.YELLOW
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
mll = Fore.LIGHTBLUE_EX
mjj = Fore.RED


def display_centered_lappy():
    lappy = f"""

{psi}▀█████████▄   ▄█     ▄████████     ███        ▄█    █▄    
{psi}  ███    ███ ███    ███    ███ ▀█████████▄   ███    ███   
{psi}  ███    ███ ███▌   ███    ███    ▀███▀▀██   ███    ███   
{y} ▄███▄▄▄██▀  ███▌  ▄███▄▄▄▄██▀     ███   ▀  ▄███▄▄▄▄███▄▄ 
{y}▀▀███▀▀▀██▄  ███▌ ▀▀███▀▀▀▀▀       ███     ▀▀███▀▀▀▀███▀  
{y}  ███    █▄ ███  ▀███████████     ███       ███    ███   
{w}  ███    ███ ███    ███    ███     ███       ███    ███   
{w}▄█████████▀  █▀     ███    ███    ▄████▀     ███    █▀    
                    ███    ███                            

                Made by {psi}Social {w}and {psi}Lap{w}
    """
    columns = os.get_terminal_size().columns
    for line in lappy.splitlines():
        print(line.center(columns))


ctypes.windll.kernel32.SetConsoleTitleW("/birth | Enter Token")

async def send_message_to_friend(client, token, friend_id, message):
    dm_url = "https://discord.com/api/v9/users/@me/channels"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': token,
        'Content-Type': 'application/json',
        'Origin': 'https://discord.com',
        'Referer': 'https://discord.com/channels/@me',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Debug-Options': 'bugReporterEnabled',
        'X-Discord-Locale': 'en-US',
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI0MDI0OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
    }


    payload = {
        "recipient_id": friend_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(dm_url, headers=headers, json=payload) as response:
            if response.status == 403:
                response_data = await response.json()
                if "captcha_key" in response_data or "captcha_sitekey" in response_data:
                    print(f"                {mkk}[ {mjj}X {mkk}] {w}CAPTCHA detected! Closing program...{w}")
                    os._exit(0)
                    
            if response.status == 200:
                dm_channel = await response.json()
                channel_id = dm_channel["id"]
                
                message_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
                message_payload = {
                    "content": message
                }

                async with session.post(message_url, headers=headers, json=message_payload) as message_response:
                    if message_response.status == 403:
                        response_data = await message_response.json()
                        if "captcha_key" in response_data or "captcha_sitekey" in response_data:
                            print(f"                {mkk}[ {mjj}X {mkk}] {w}CAPTCHA detected! Closing program...{w}")
                            os._exit(0)
                            
                    if message_response.status == 200:
                        print(f"                {mkk}[ {g}>.< {mkk}]{w} Sent 2 {friend_id}")
                        
                        # Add DM closing request
                        close_url = f"https://discord.com/api/v9/channels/{channel_id}"
                        async with session.delete(close_url, headers=headers) as close_response:
                            if close_response.status == 200:
                                print(f"                {mkk}[ {g}>.< {mkk}]{w} Closed DM with {friend_id}")
                            else:
                                print(f"                {mkk}[ {mjj}X {mkk}]{w} Failed to close DM with {friend_id}")
                    else:
                        None
            else:
                None


async def send_message_to_friends(client, token, friends, message):
    for friend in friends:
        friend_id = friend['id']
        friend_username = f"{friend['user']['username']}#{friend['user']['discriminator']}"
        try:
            print(f"{mkk}[ {g}>.< {mkk}] Sending to {mll}{friend_username}{w}...")
            await send_message_to_friend(client, token, friend_id, message)
            
            delay = random.uniform(8.0, 12.0)
            print(f"                {mkk}[ {y}>.< {mkk}] {w}Safety delay: {delay:.1f} seconds...")
            await asyncio.sleep(delay)
            
            if friends.index(friend) % 5 == 0 and friends.index(friend) != 0:
                extra_delay = random.uniform(30.0, 60.0)
                print(f"                {mkk}[  {y}!{mkk}  ] {w}Taking a longer break: {extra_delay:.1f} seconds...")
                await asyncio.sleep(extra_delay)
                
        except Exception as e:
            print(f"                {mkk}[ {mjj}>.< {mkk}] {w}Oops Retrying..{w} ")
            await asyncio.sleep(15)

async def fetch_friends(token):
    url = "https://discord.com/api/v9/users/@me/relationships"
    
    headers = {
        "authority": "discord.com",
        "method": "PATCH",
        "scheme": "https",
        "accept": "/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "authorization": token,
        "origin": "https://discord.com/",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9020 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "en-US",
        "X-Discord-Timezone": "Asia/Calcutta",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDIwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjAgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDAyMzcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM4NTE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                friends = await response.json()
                return friends
            else:
                print(f"Failed to fetch friends: {response.status}")
                return []


class MyClient(commands.Bot):
    def __init__(self, token):
        super().__init__(
            command_prefix=",",
            self_bot=True,
        )
        self.user_token = token 

    async def on_ready(self):
        print(f'Welcome back, {self.user}')
        os.system('cls')
        display_centered_lappy()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[{self.user}] | Enter Msg ")
        message = input(f'{mkk}[ {y}>.< {mkk}]{w} Message Please : ')
        os.system('cls')
        
        display_centered_lappy()
        friends = await fetch_friends(self.user_token)
        await send_message_to_friends(self, self.user_token, friends, message)
        print(f"{mkk}[ {y}>.<{mkk} ] {w}Finished! Press Enter to exit.")
        input()

def run_bot():
    display_centered_lappy()
    token = input(f"{mkk}[ {y}>.<{mkk} ] {w}Token Please  : ")
    os.system('cls')

    client = MyClient(token)  
    client.run(token, bot=False)

if __name__ == "__main__":
    run_bot()
