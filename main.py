#####################################
#            Created by             #
#                SBR                #
#####################################
import random
import time
import sys
import logging
from freeGPT import Client
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from config_parser import ConfigParser
from data import Variants
####################################################################
config_name = 'config.json'
####################################################################


def main():
    default = {0: True, 1: False, 2: True, 3: False, 4: True, 5: False}
    advanced = {0: False, 1: True, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False}
    worker.init()
    worker.start()
    main_branch = random.randint(1, 3)
    worker.set_button_1(random.choice(worker.get_buttons_1()))
    worker.confirm()
    if main_branch == 1 or main_branch == 2:
        for i in range(6):
            btns = worker.get_buttons_1()
            if default[i]:
                choose = random.randint(1, len(btns))
                for g in range(choose):
                    rnd = random.choice(btns)
                    btns.remove(rnd)
                    worker.set_button_1(rnd)
            else:
                rnd = random.choice(btns)
                btns.remove(rnd)
                worker.set_button_1(rnd)
            worker.confirm()
    else:
        for i in range(7):
            btns = worker.get_buttons_1()
            if advanced[i]:
                choose = random.randint(1, len(btns))
                for g in range(choose):
                    rnd = random.choice(btns)
                    btns.remove(rnd)
                    worker.set_button_1(rnd)
            else:
                rnd = random.choice(btns)
                btns.remove(rnd)
                worker.set_button_1(rnd)
            worker.confirm()
    print(4234234242)


class Driver:
    def __init__(self):
        super(Driver, self).__init__()
        self.__driver = None
        self.__denied = [
            'Нет',
            'Я не веду страницу, блог или сообщество в Интернете',
            'Это решают другие люди',
            'Ничего из перечисленного',
            'Другое:'
        ] # 1. 1(A), 2(S), 3(A), 4(S), 5(A), 6(S), 7()
          # 2. 1(A), 2(S), 3(A), 4(S), 5(A), 6(S), 7()
          # 3. 1(S), 2(A), 3(A), 4(S), 5(A), 6(S), 7(A), 9()

    def init(self):
        service = Service(executable_path=args.get_config()['chrome_driver_path'])
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")  # linux only
        chrome_options.add_argument("--headless=new")
        self.__driver = webdriver.Firefox(service=service, options=chrome_options)

    def start(self):
        self.__driver.get(args.get_config()['url'])
        time.sleep(7)
        self.__driver.find_element(By.XPATH, f"//div[contains(text(), 'Начать опрос')]").click()
        time.sleep(1)

    def get_buttons_1(self):
        output = list()
        data = self.__driver.find_element(By.XPATH, "/html[@class=' json csscalc no-touchevents cssvhunit cssvwunit cssanimations flexbox']/body/div[@id='panel2_mainContainer']/div/div[@class='oprosso-poll']/div[@class='oprosso-poll__wrapper']/div[@class='oprosso-poll__horizontallContainer']/span/div/div[1]/div/div/div[@class='oprosso-poll__question-wrapper']/div[@class='oprosso-poll__question-wrapper-inner oprosso-poll__question-wrapper-inner_substrate']/div/div[@class='oprosso-poll__question-body']/div[@class='oprosso-poll-type__closed-wrapper']").text.split('\n')
        for i in data:
            if i not in self.__denied:
                output.append(i)
        return output

    def set_button_1(self, text):
        time.sleep(1)
        self.__driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]").click()

    def confirm(self):
        time.sleep(1)
        self.__driver.find_element(By.XPATH, f"//span[contains(text(), 'Далее')]").click()
        time.sleep(1)


class ChatGpt:
    def __init__(self):
        super(ChatGpt, self).__init__()

    def gpt_query(self, query):
        try:
            answer = Client.create_completion("gpt3", f'determine the price of a used car {query} In the USA. In the response, specify the Traid In and Private Price in json format without any another information')
            print(answer)
        except:
            pass
        return answer


if '__main__' == __name__:
    logging.basicConfig(handlers=[logging.FileHandler("log.txt"), logging.StreamHandler(sys.stdout)],
                        level=logging.INFO)
    args = ConfigParser(config_name)
    worker = Driver()
    links = Variants()
    main()


