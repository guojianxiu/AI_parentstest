import random

from poium import Page, PageElement, PageElements
import time

class Operationpage(Page):
    #表扬
    praise_loc = PageElement(class_name = 'praise_btn')
    #任务列表
    tasks_list_loc = PageElements(class_name = 'unfinished_item')
    #历史表现
    history_loc = PageElement(link_text = '历史表现')

    def todayplan(self):
        self.praise_loc.click()

    def taskslen(self):
        return len(self.tasks_list_loc)

    def history(self):
        self.history_loc.click()