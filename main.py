# copyright 2023 © Xron Trix | https://github.com/Xrontrix10


# @title 🖥️ Main  Leecher

# @title Main Code
# @markdown <div><center><img src="https://user-images.githubusercontent.com/125879861/255391401-371f3a64-732d-4954-ac0f-4f093a6605e1.png" height=80></center></div>
# @markdown <center><h4><a href="https://github.com/XronTrix10/Telegram-Leecher/wiki/INSTRUCTIONS">READ</a> How to use</h4></center>

# @markdown <br>

API_ID = 0  # @param {type: "integer"}
API_HASH = ""  # @param {type: "string"}
BOT_TOKEN = ""  # @param {type: "string"}
USER_ID = 0  # @param {type: "integer"}
DUMP_ID = 0  # @param {type: "integer"}


import subprocess, time, json, shutil, os
from IPython.display import clear_output
from threading import Thread

Working = True

banner = '''

/"       )("     _   ") /""\      /"      \("     _   ")|" \  (\"   \|"  \  /" _   "|     
(:   \___/  )__/  \\__/ /    \    |:        |)__/  \\__/ ||  | |.\\   \    |(: ( \___)     
 \___  \       \\_ /   /' /\  \   |_____/   )   \\_ /    |:  | |: \.   \\  | \/ \          
  __/  \\      |.  |  //  __'  \   //      /    |.  |    |.  | |.  \    \. | //  \ ___     
 /" \   :)     \:  | /   /  \\  \ |:  __   \    \:  |    /\  |\|    \    \ |(:   _(  _|    
(_______/       \__|(___/    \___)|__|  \___)    \__|   (__\_|_)\___|\____\) \_______)     
                                                                                           
  _______  _____  ___    _______   __    _____  ___    _______   ________                  
 /"     "|(\"   \|"  \  /" _   "| |" \  (\"   \|"  \  /"     "| /"       )                 
(: ______)|.\\   \    |(: ( \___) ||  | |.\\   \    |(: ______)(:   \___/                  
 \/    |  |: \.   \\  | \/ \      |:  | |: \.   \\  | \/    |   \___  \                    
 // ___)_ |.  \    \. | //  \ ___ |.  | |.  \    \. | // ___)_   __/  \\                   
(:      "||    \    \ |(:   _(  _|/\  |\|    \    \ |(:      "| /" \   :)                  
 \_______) \___|\____\) \_______)(__\_|_)\___|\____\) \_______)(_______/  

                                                

'''

print(banner)

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(2)
    clear_output()


_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    n_dump = "-100" + str(DUMP_ID)
    DUMP_ID = int(n_dump)

if os.path.exists("/content/sample_data"):
    shutil.rmtree("/content/sample_data")

cmd = "git clone https://github.com/olarwe3/Telegram-Leecher"
proc = subprocess.run(cmd, shell=True)
cmd = "apt update && apt install ffmpeg aria2"
proc = subprocess.run(cmd, shell=True)
cmd = "pip3 install -r /content/Telegram-Leecher/requirements.txt"
proc = subprocess.run(cmd, shell=True)

credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

with open('/content/Telegram-Leecher/credentials.json', 'w') as file:
    file.write(json.dumps(credentials))

Working = False

if os.path.exists("/content/Telegram-Leecher/my_bot.session"):
    os.remove("/content/Telegram-Leecher/my_bot.session") # Remove previous bot session
    
print("\rStarting Bot....")

!cd /content/Telegram-Leecher/ && python3 -m colab_leecher #type:ignore
