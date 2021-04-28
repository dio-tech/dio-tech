from cmd import Cmd
from selenium import webdriver
import os
import time
import sys
import datetime
from time import ctime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

'''
python create_projects.py
'''

# GOAL
# Create a program that creates a project and automatically adds it to github and to my sublime's text folder

browser = "https://github.com"

class Bot:
	def __init__(self, username, password):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.username = username
		self.password = password
		self.get_to_path()

	def get_to_path(self):
		self.bot.get(browser)
		self.login()

	def login(self):
		self.bot.find_element_by_xpath("//html/body/div[4]/main/div/div[1]/div[1]/div[1]/div/div/div[1]/form[1]/div/button").click()
		time.sleep(2)
		self.bot.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a").click()
		time.sleep(2)
		user = self.bot.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]")
		user.send_keys(self.username)
		time.sleep(2)
		passw = self.bot.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]")
		passw.send_keys(self.password)
		time.sleep(1)
		self.bot.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()

class MyPrompt(Cmd):
	def do_exit(self, inp):
		print("Bye")
		return True

	def do_create(self, inp):
		print(f"Creating '{inp}'")
		add_to_git(inp)
		print("Repository Created")

	def do_delete(self, inp):
		print(f"Deleting {inp}")

def add_to_git(inp):
	Bot("diogo.alexmendes5@gmail.com", "didi$mendes!2005")

MyPrompt().cmdloop()

# FOLDER PATH
# C:\Users\diogo\Sublime text

# git init
# git add .
# git commit -m "first commit"