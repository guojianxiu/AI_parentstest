from poium import Page, PageElement, PageElements
import random
import time

class Evaluationpage(Page):
    #介绍页
    join_loc = PageElement(xpath='//*[@id="root"]/div/div/div[2]/div[3]/a/span')
    #选择年级
    grades = PageElements(xpath = '//*[@id="root"]/div/div/ul/li')
    #下一步
    next_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[3]/a/span')
    #测评题目的数量
    count = PageElement(xpath = '//*[@id="root"]/div/div/div[1]/div[2]/span[2]/span')
    #题目选项
    selects_loc = PageElements(xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div')
    #提交按钮
    commit_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a/span')


    def start(self):
        self.join_loc.click()

    def first_step(self):
        grade = random.choice(self.grades)
        grade.click()
        time.sleep(1)
        self.next_loc.click()

    def second_step(self):
        for i in range(int(self.count.text)):
            select = random.choice(self.selects_loc)
            select.click()
            time.sleep(3)
        self.commit_loc.click()