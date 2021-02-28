from selenium import webdriver
import sys

user_id = sys.argv[1]
pw = sys.argv[2]

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

s = ""
x = 0

username = driver.find_element_by_id("username")
username.send_keys(user_id)

password = driver.find_element_by_id("password")
password.send_keys(pw)

capcha = driver.find_element_by_id("valuepkg3")
capcha.clear()

information = driver.find_element_by_id("login")
string = information.text


for i in range(len(string)):
    if x == 3:
        s += string[i]
    if string[i] == '\n':
        x += 1

ls = s.split()

if ls[2] == "second":
    capcha.send_keys(int(ls[6]))
elif ls[2] == "first":
    capcha.send_keys(int(ls[4]))
elif ls[1] == "subtract":
    capcha.send_keys(int(ls[2]) - int(ls[4]))
elif ls[1] == "add":
    capcha.send_keys(int(ls[2]) + int(ls[4]))

login = driver.find_element_by_id("loginbtn")
login.click()

