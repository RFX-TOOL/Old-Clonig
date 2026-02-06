import os, platform, time, sys

os.system('xdg-open https://t.me/dark_xploit_rfx')
time.sleep(2)
os.system('xdg-open https://www.facebook.com/r.a.z.a.x.r.tsu')
time.sleep(2)


try:
    import requests
except:
    os.system("pip uninstall requests -y;pip install requests")

print('\033[1;97m[*] \033[1;92mLoading Checking Update...')
os.system('git pull --quiet 2>/dev/null')

bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;97m[✓] \033[1;92mFound 64 Bit Device')
    import old_up
elif bit == '32bit':
    print('\033[1;97m[✓] \033[1;91mSORRY BRO YOUR DEVICE IS 32 BIT')
    print('\033[1;97m[✓] \033[1;91mPLEASE USE 64 BIT DEVICE')
