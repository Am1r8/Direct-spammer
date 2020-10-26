from time import sleep
print("Welcome to direct spammer\nDon't forget to use this on your friends not anyone else\nPUBLISHER: ALPHA:) "
      "\nVERSION: 1.3.1 \you have to follow you friends or you get error")
sleep(3)
try:

    from selenium import webdriver
    import random
    import pynput

    print("Opening modules please wait ...")
    sleep(5)
except:
    print("Unable to open modules")
    exit()

try:
    browser = webdriver.Chrome()
    print("opening browser ...")
except:
    print("Can't open browser")


def start():
    print("Getting online ...")
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
    for i in range(0,3):
        sleep(1)

    sleep(1)
    notNow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    notNow.click()
    sleep(3)
    notNow_not = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notNow_not.click()
    sleep(3)


def enteringDirect():
    username_client = input("Please enter your victim username\n")
    browser.get('https://www.instagram.com/' + username_client + '/')
    sleep(2)
    massage1 = browser.find_element_by_css_selector(
        '#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div._862NM > div > button')
    massage1.click()
    sleep(1)


lyrics = open("lyrics.txt", "r")
open1 = (f.read())


def send_massage():
    print("you can change the lyrics in script path")
    sleep(5)
    for i in range(1,6):
        sleep(1)
        print("starting attack in " , i)
    for i in range(0, 5):
        send = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        send.send_keys(open1)

        sleep(2)

        send_button = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send_button.click()


def close():
    browser.close()
    print("See you later :)")
    print("Closing ...")
    print("PUBLISHER: ALPHA:)\n VERSION: 1.3.1")

try:
    start()
    enteringDirect()
    send_massage()
    close()
except:
    print("There is an error in script please check the code!!")
    exit()




