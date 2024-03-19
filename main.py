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
from selenium.webdriver.common.action_chains import ActionChains
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

    def insert_text(self, index, type):
        answer = chat_gpt.gpt_query(worker.get_card_text(index + 1, type))
        answer_russian = GoogleTranslator(source='en', target='ru').translate(text=answer)
        worker.insert_text(index + 1, answer_russian, type)

    def any_choose(self, fixed=None):
        branch = worker.get_buttons_1(True)
        if fixed is None:
            l_branch = len(branch)
        else:
            l_branch = fixed
        choose = random.randint(1, l_branch)
        for i in range(choose):
            rnd = random.choice(branch)
            branch.remove(rnd)
            worker.set_button_1(rnd)
        worker.confirm()
        return choose

    def second_step(self):
        try:
            choose = self.any_choose()
            for i in range(11):
                match i:
                    case 0:
                        if choose != 19:
                            for g in range(19 - choose):
                                self.insert_text(g, 0)
                            worker.confirm()
                    case 1:
                        buttons = worker.get_buttons_1(True)
                        choise = random.choice(buttons)
                        worker.set_button_1(choise)
                        worker.confirm()
                    case 2:
                        self.insert_text(0, 1)
                        worker.confirm()
                    case 3:
                        if choose == 1:
                            type = 1
                        else:
                            type = 0
                        for g in range(choose):
                            choise = random.randint(1, 8)
                            worker.set_button_2(links.cards_buttons_query(type, g+1, choise))
                        worker.confirm()
                    case 4:
                        self.any_choose(3)
                    case 5:
                        self.any_choose(3)
                    case 6:
                        for g in range(choose):
                            choise = random.randint(1, 11)
                            worker.set_button_2(links.circles(0, choise))
                            worker.confirm()
                            time.sleep(1)
                            if worker.checker(0):
                                worker.confirm()
                            else:
                                self.any_choose()
                            choise = random.randint(1, 5)
                            worker.set_button_2(links.circles(0, choise))
                            worker.confirm()
                    case 7:
                        worker.confirm()
                    case 8:
                        for g in range(11):
                            choise = random.randint(1, 5)
                            worker.set_button_2(links.circles(1, choise, g + 1))
                        worker.confirm()
                    case 9:
                        buttons = worker.get_buttons_1()
                        choise = random.choice(buttons)
                        worker.set_button_1(choise)
                        worker.confirm()
                    case 10:
                        worker.insert_text(1, str(random.randint(18, 99)), 1)
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
            'Другое:',
            'Менее 1 тыс. подписчиков',
            'Собственный сайт, приложение',
            'VK Видео'
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
        #chrome_options.add_argument("--headless=new")
        self.__driver = webdriver.Firefox(service=service, options=chrome_options)

    def start(self):
        self.__driver.get(args.get_config()['url'])
        time.sleep(5)
        self.__driver.find_element(By.XPATH, f"//div[contains(text(), 'Начать опрос')]").click()
        time.sleep(1)

    def string_cleaner(self, text):
        for i in self.__delete_list:
            if i in text:
                return i

    def get_buttons_1(self, use_delete=False):
        output = list()
        while True:
            try:
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
            except Exception as e:
                print(e)

    def set_button_1(self, text):
        while True:
            try:
                time.sleep(1)
                element = self.__driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]")
                self.__driver.execute_script("arguments[0].scrollIntoView(true);", element)
                ActionChains(self.__driver).move_to_element(element).click().perform()
                time.sleep(1)
                break
            except Exception as e:
                print(e)

    def set_button_2(self, text):
        while True:
            try:
                time.sleep(1)
                element = self.__driver.find_element(By.XPATH, text)
                self.__driver.execute_script("arguments[0].scrollIntoView(true);", element)
                ActionChains(self.__driver).move_to_element(element).click().perform()
                time.sleep(1)
                break
            except Exception as e:
                print(e)

    def confirm(self):
        while True:
            try:
                time.sleep(1)
                element = self.__driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div/a/span")
                self.__driver.execute_script("arguments[0].scrollIntoView(true);", element)
                ActionChains(self.__driver).move_to_element(element).click().perform()
                time.sleep(1)
                break
            except Exception as e:
                print(e)

    def checker(self, type):
        try:
            time.sleep(1)
            element = self.__driver.find_element(By.XPATH, links.checker(type))
            answer_russian = GoogleTranslator(source='en', target='ru').translate(
                text=chat_gpt.gpt_query('Поясните, почему Вы выбрали такой ответ'))
            self.__driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.find_element(By.TAG_NAME, 'textarea').send_keys(answer_russian)
            time.sleep(1)
            return True
        except Exception as e:
            print(e)

    def insert_text(self, index, text, type):
        while True:
            try:
                time.sleep(1)
                container = self.__driver.find_element(By.XPATH, links.cards_input_query(type, index))
                self.__driver.execute_script("arguments[0].scrollIntoView(true);", container)
                container.find_element(By.TAG_NAME, 'input').send_keys(text)
                time.sleep(1)
                break
            except Exception as e:
                print(e)

    def get_card_text(self, index, type):
        while True:
            try:
                time.sleep(1)
                text = self.__driver.find_element(By.XPATH, links.cards_input_query(type, index)).text
                time.sleep(1)
                return text
            except Exception as e:
                print(e)


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


