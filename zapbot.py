from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        self.mensagem = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
        self.grupos = ["anonymous zap"] #nao pergunta
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Teste de bot em Python" class="_1wjpf _3NFp9 _3FXB1">Teste de bot em Python</span>
        #<div tabindex="-1" class="_1Plpp">
        #<span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(12)     
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            button_send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            button_send.click()
            time.sleep(3)

bot = whatsappBot()
bot.EnviarMensagens()