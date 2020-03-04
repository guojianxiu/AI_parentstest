from poium import Page, PageElement
from page.evaluation import Evaluationpage
from page.adjustplan import Adjustplanpage
import time

class Resultpage(Page):
    #测试结果页
    #重新测评
    re_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[1]/a')
    #调整计划
    adjust_loc= PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a')
    #开通AI乐学
    open_loc = PageElement(css = '#root > div > div > div.btn_box > a')

    def reevaluation(self):
        self.re_loc.click()
        time.sleep(5)
        Evaluationpage(self.driver).first_step()
        Evaluationpage(self.driver).second_step()

    def adjustplan(self):
        Resultpage(self.driver)
        time.sleep(5)
        self.adjust_loc.click()
        time.sleep(5)
        Adjustplanpage(self.driver).adjust()

    def open(self):
        #Resultpage(self.driver)
        self.open_loc.click()
