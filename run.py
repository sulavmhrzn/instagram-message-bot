import getpass

from utils.app import Bot

username = input('Enter your username: ')
password = getpass.getpass(prompt='Enter your password: ')

if username and password:
    send_to = input('Enter friends username: ')
    b = Bot(username, password)
    b.login()
    b.message_to(send_to)
