import os, platform, time, sys
os.system('xdg-open https://chat.whatsapp.com/DFj8atKbJZYE1zc68YMnvK?mode=gi_t')
time.sleep(2)
bit = platform.architecture()[0]
if bit == '64bit':
    import old
elif bit == '32bit':
    print('\033[1;97m[✓] \033[1;91mSORRY BRO YOUR DEVICE IS 32 BIT')
    print('\033[1;97m[✓] \033[1;91mPLEASE USE 64 BIT DEVICE')
    sys.exit()
else:
    print('\033[1;97m[!] \033[1;91mUnknown Architecture')
    sys.exit()
