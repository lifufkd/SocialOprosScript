import json
import random
import time
import sys
import logging
import undetected_chromedriver as uc
from freeGPT import Client
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
    parser = Parser(args)
    get_prices()

