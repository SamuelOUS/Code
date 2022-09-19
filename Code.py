import selenium
from selenium import webdriver
import webbrowser
from webbrowser import Chrome
from selenium.webdriver.common.by import By

class user():
    def __int__(self):
        self.name = int(input("Input your username:"))
        self.password = int(input("Input your password:"))

Student_1 = user()
class page():
    options = webdriver.ChromeOptions()
    Driver = webdriver.Chrome()
    Driver.get("https://uvirtual.udem.edu.co/")

    ShowButton = Driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/h5').click()
    UserBox = Driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/form/div[1]/input')
    UserBox.send_keys(Student_1.name)
    UserPassword = Driver.find_element("xpath",'/html/body/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/form/div[2]/input' )
    UserPassword.send_keys(Student_1.password)
    EnterButton = Driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/form/div[3]/button').click()

class Personal_Information():
    curse_1 = page.Driver.find_element(By)
    curse_2 =
    curse_3 =
    curse_4 =
    curse_5 =
    curse_6 =
    curse_7 =
    curse_8 =




class Compend():







