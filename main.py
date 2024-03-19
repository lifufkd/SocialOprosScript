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
from deep_translator import GoogleTranslator
####################################################################
config_name = 'config.json'
####################################################################


class Solver:
    def __init__(self):
        super(Solver, self).__init__()


    def first_step(self):
        default = {0: True, 1: False, 2: True, 3: False, 4: True, 5: False}
        advanced = {0: False, 1: True, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False}
        try:
            worker.init()
            worker.start()
            main_branch = random.choice(worker.get_buttons_1())
            worker.set_button_1(main_branch)
            worker.confirm()
            if main_branch == 'Да, я блогер/автор и самостоятельно веду авторскую деятельность ' or main_branch == 'Да, я блогер/автор и часть задач берет на себя команда':
                for i in range(6):
                    btns = worker.get_buttons_1()
                    if default[i]:
                        try:
                            choose = random.randint(1, len(btns))
                            for g in range(choose):
                                rnd = random.choice(btns)
                                btns.remove(rnd)
                                worker.set_button_1(rnd)
                        except:
                            print('Ошибка выбора')
                    else:
                        rnd = random.choice(btns)
                        btns.remove(rnd)
                        worker.set_button_1(rnd)
                    worker.confirm()
            else:
                for i in range(8):
                    btns = worker.get_buttons_1()
                    if advanced[i]:
                        try:
                            choose = random.randint(1, len(btns))
                            for g in range(choose):
                                rnd = random.choice(btns)
                                btns.remove(rnd)
                                worker.set_button_1(rnd)
                        except:
                            print('Ошибка выбора')
                    else:
                        rnd = random.choice(btns)
                        btns.remove(rnd)
                        worker.set_button_1(rnd)
                    worker.confirm()
            print(4234234242)
        except:
            sys.exit('Произошла ошибка в загрузке сайта, необходим перезапуск')

    def insert_text(self, index):
        answer = chat_gpt.gpt_query(worker.get_card_text(index + 1))
        answer_russian = GoogleTranslator(source='en', target='ru').translate(text=answer)
        worker.insert_text(index + 1, answer_russian)

    def second_step(self):
        try:
            main_branch = worker.get_buttons_1(True)
            choose = random.randint(1, len(main_branch))
            for i in range(choose):
                rnd = random.choice(main_branch)
                main_branch.remove(rnd)
                worker.set_button_1(rnd)
            worker.confirm()
            for i in range(6):
                match i:
                    case 0:
                        for g in range(19 - choose):
                            self.insert_text(g)
                    case 1:
                        buttons = worker.get_buttons_1(True)
                        choise = random.choice(buttons)
                        worker.set_button_1(choise)
                        worker.confirm()
                    case 2:
                        self.insert_text(1)
                        worker.confirm()

        except Exception as e:
            print(e)
            sys.exit('Произошла ошибка в загрузке сайта, необходим перезапуск')


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
        self.__delete_list = [
            '*Instagram ',
            '*Facebook '
        ]

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

    def string_cleaner(self, text):
        for i in self.__delete_list:
            if i in text:
                return i

    def get_buttons_1(self, use_delete=False):
        output = list()
        data = self.__driver.find_element(By.XPATH, "/html[@class=' json csscalc no-touchevents cssvhunit cssvwunit cssanimations flexbox']/body/div[@id='panel2_mainContainer']/div/div[@class='oprosso-poll']/div[@class='oprosso-poll__wrapper']/div[@class='oprosso-poll__horizontallContainer']/span/div/div[1]/div/div/div[@class='oprosso-poll__question-wrapper']/div[@class='oprosso-poll__question-wrapper-inner oprosso-poll__question-wrapper-inner_substrate']/div/div[@class='oprosso-poll__question-body']/div[@class='oprosso-poll-type__closed-wrapper']").text.split('\n')
        for i in data:
            if i not in self.__denied:
                if use_delete:
                    data = self.string_cleaner(i)
                    if data is not None:
                        output.append(data)
                    else:
                        output.append(i)
                else:
                    output.append(i)
        return output

    def set_button_1(self, text):
        time.sleep(0.5)
        self.__driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]").click()

    def confirm(self):
        time.sleep(0.5)
        self.__driver.find_element(By.XPATH, f"//span[contains(text(), 'Далее')]").click()
        time.sleep(0.5)

    def insert_text(self, index, text):
        time.sleep(0.5)
        container = self.__driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[1]/div[1]/span/div/div[1]/div[{index}]/div/div")
        container.find_element(By.TAG_NAME, 'input').send_keys(text)
        time.sleep(0.5)

    def get_card_text(self, index):
        time.sleep(0.5)
        text = self.__driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[1]/div[1]/span/div/div[1]/div[{index}]/div/div").text
        time.sleep(0.5)
        return text


class ChatGpt:
    def __init__(self):
        super(ChatGpt, self).__init__()

    def gpt_query(self, query):
        try:
            answer = Client.create_completion("gpt3", query)
        except:
            pass
        return answer


if '__main__' == __name__:
    logging.basicConfig(handlers=[logging.FileHandler("log.txt"), logging.StreamHandler(sys.stdout)],
                        level=logging.INFO)
    args = ConfigParser(config_name)
    worker = Driver()
    links = Variants()
    chat_gpt = ChatGpt()
    tasks = Solver()
    tasks.first_step()
    tasks.second_step()


