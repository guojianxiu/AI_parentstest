from poium import Page, PageElement, PageElements
import random

class Adjustplanpage(Page):
    #年级
    grades = PageElements(class_name = 'grades_list')
    #已选能力
    active = PageElements(class_name = 'aspiration_li_active')
    #能力
    abilities = PageElements(xpath = '//*[@id="root"]/div/div/div[3]/ul/li')
    #确认调整
    confirm_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a')

    def adjust(self):
        grade = random.choice(self.grades)
        grade.click()
        for i in range(len(self.active)):
            self.active[0].click()
        random.sample(self.abilities, 2)
        self.confirm_loc.click()
