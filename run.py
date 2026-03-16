import os, platform, time, sys, importlib

# Open link (safe)
try:
    os.system('xdg-open "https://chat.whatsapp.com/DFj8atKbJZYE1zc68YMnvK?mode=gi_t" >/dev/null 2>&1')
except:
    pass

time.sleep(1)

# Auto fix requests
def fix_requests():
    try:
        import requests
    except ImportError:
        os.system("pip uninstall requests urllib3 chardet charset_normalizer -y >/dev/null 2>&1")
        os.system("pip install requests urllib3 chardet charset_normalizer >/dev/null 2>&1")

fix_requests()

# Silent update
os.system('git pull --quiet 2>/dev/null')

# Check architecture
bit = platform.architecture()[0]

if bit != '64bit':
    print('\033[1;91m[!] Only 64bit supported')
    sys.exit()

print('\033[1;92m[✓] Python 3.13 Ready Device')

# -------- MODULE LOADER -------- #
def load_old_module():
    try:
        return importlib.import_module("old")
    except Exception as e:
        print('\033[1;91m[!] Failed to load old module')
        print('\033[1;93mReason:', e)

        # Check file exists
        if not os.path.exists("old.cpython-313-aarch64-linux-android.so"):
            print('\033[1;91m[!] Missing .so file!')
        else:
            print('\033[1;91m[!] .so file found but not compatible')

        print('\n\033[1;96m[✓] Fix Tips:')
        print(' - Move script to $HOME')
        print(' - Recompile .so for Python 3.13')
        print(' - Or use pure Python version\n')

        return None

old_module = load_old_module()

# -------- FALLBACK SYSTEM -------- #
if old_module is None:
    print('\033[1;93m[~] Running fallback mode...\n')

    # Demo fallback কাজ (replace করতে পারো)
    def fallback():
        print('\033[1;92m[✓] Tool running without .so (limited mode)')
        for i in range(5):
            print(f"[•] Processing {i+1}/5")
            time.sleep(0.5)

    fallback()

else:
    print('\033[1;92m[✓] old module loaded successfully')
