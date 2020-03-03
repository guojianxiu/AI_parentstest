from poium import Page, PageElement, PageElements
import random
import time

class Evaluationpage(Page):
    #智能测评
    #介绍页
    join_loc = PageElement(xpath='//*[@id="root"]/div/div/div[2]/div[3]/a/span')
    #选择年级
    grades = PageElements(xpath = '//*[@id="root"]/div/div/ul/li')
    #下一步
    next_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[3]/a/span')
    #题目选项
    selects_loc = PageElements(xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div')
    #提交按钮
    commit_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a')

    def start(self):
        self.join_loc.click()

    def first_step(self):
        grade = random.choice(self.grades)
        grade.click()
        time.sleep(1)
        self.next_loc.click()

    def second_step(self):
        for i in range(20):
            time.sleep(1)
            select = random.choice(self.selects_loc)
            select.click()

        Evaluationpage(self.driver)
        self.commit_loc.click()