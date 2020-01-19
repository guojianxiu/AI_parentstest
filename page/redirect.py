
from poium import Page, PageElement,PageElements
from page.evaluation import Evaluationpage
import time

class Redirectpage(Page):
    #引导页
    join_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[2]/div[3]/a/span')
    #续费页面：前往支付、已拥有
    pay_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a/span')
    confirm_loc = PageElement(xpath = '//*[@id="am-modal-container-1579412815830"]/div/div[2]/div/div/div[3]/div/a[2]')

    def redirect(self):
        if self.join_loc:
            self.join_loc.click()
            time.sleep(2)
            return Evaluationpage(self.driver)
        if self.pay_loc:
            self.pay_loc.click()
            self.confirm_loc.click()
            time.sleep(10)





