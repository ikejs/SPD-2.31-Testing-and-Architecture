# by Kami Bigdely
# Remove control flag
# Reference: https://searchcode.com/file/92870153/frameworkconsole/framework.py/

def prompt_for_apk():
    while True:
        print( "Puts the Android Agent inside an Android App APK. The application runs normally, with extra functionality.")
        inputfile = input('APK to Backdoor: ').strip()
        if inputfile == '':
            break
        else:
            continue
            print('doing other stuff.') 

prompt_for_apk()