print("""\n\n
  _____           _                                     _____                                           
 |_   _|         | |                                   / ____|                                          
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \   \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | |  ____) | |_) | (_| | | | | | | | | | | |  __/ |   
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                            __/ |                            | |                                        
                           |___/                             |_|                                        
\n\n\n\n\n""")

from time import sleep
print("Welcome to direct spammer\nDon't forget to use this on your friends not anyone else\nPUBLISHER: ALPHA:) "
      "\nVERSION: 2.3.1 \nYou have to follow your friends or you get error\n\n")
sleep(3)
try:

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import random

    print("Opening modules please wait ...\n\n")
    sleep(5)
except:
    print("Unable to open modules")
    exit()

# Getting ready to send the lyrics 
lyrics = open("lyrics.txt", "r")
open1 = (lyrics.read())
print("Opening lyrics.txt\n\n")

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    print("opening browser ...\n\n")
except:
    print("Can't open browser\n\n")


def start():
    print("Getting online ...\n")
    print("Please Do Not Click Anything In The Browser, Everything Is Automated.\n\n\n")
    browser.get('https://www.instagram.com/')
    sleep(3)
    username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    username1 = input("Please enter you Username:\n")
    password1 = input("Please enter your password:\n")
    username.send_keys(username1)
    password.send_keys(password1)
    login_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    login_button.click()
    sleep(5)


def enteringDirect():
    username_client = input("Please enter your victim username\n")
    browser.get('https://www.instagram.com/' + username_client + '/')
    sleep(3)
    massage1 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
    massage1.click()
    sleep(1)




def send_massage():
    notNow_not = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
    notNow_not.click()
    sleep(2)
    print("you can change the lyrics in script path\n\n\n")
    sleep(5)
    for i in range(1,6):
        sleep(1)
        print("starting attack in " , i)
    for i in range(0, 10):
        send = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        send.send_keys(open1)

        sleep(0.5)

        send_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send_button.click()


def close():
    browser.close()
    print("See you later :)\n")
    print("Closing ...\n\n")
    print("PUBLISHER: ALPHA:)\nVERSION: 2.3.1")

try:
    start()
    enteringDirect()
    send_massage()
    close()
except:
    print("Thanks for Using My App :) \n\n")
    print("There is an error in script please check the code!!")





