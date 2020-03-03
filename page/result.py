from poium import Page, PageElement
from page.evaluation import Evaluationpage
from page.adjustplan import Adjustplanpage

class Resultpage(Page):
    #测试结果页
    #重新测评
    re_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[1]/a')
    #调整计划
    adjust_loc= PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a/text()')
    #开通AI乐学
    open = PageElement(xpath = '//*[@id="root"]/div/div/div[6]/a')

    def reevaluation(self):
        self.re_loc.click()
        return Evaluationpage(self.driver)

    def adjustplan(self):
        self.adjust_loc.click()
        return Adjustplanpage(self.driver)

    def open(self):
        self.open.click()
