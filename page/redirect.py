
from poium import Page, PageElement,PageElements
from page.evaluation import Evaluationpage
import time

class Redirectpage(Page):
    #引导页
    join_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[2]/div[3]/a/span')
    #续费页面：前往支付、已拥有
    pay_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a/span')
    confirm_loc = PageElement(xpath = '//*[@id="am-modal-container-1579412815830"]/div/div[2]/div/div/div[3]/div/a[2]')

    '''
    Ai乐学主要可以保留得页面有：
    介绍页：http://webapp.leke.cn/leke-ai-h5/#/homePage?newtab=1&close=1
    测评结果页：http://webapp.leke.cn/leke-ai-h5/#/result
    续费页面：http://webapp.leke.cn/leke-ai-h5/#/order?newtab=1&close=1
    操作页：http://webapp.leke.cn/leke-ai-h5/#/operation?newtab=1&close=1
    乐学报告页：
    '''

    # def redirect(self):
    #     if self.join_loc:
    #         self.join_loc.click()
    #         time.sleep(2)
    #         return Evaluationpage(self.driver)
    #     if self.pay_loc:
    #         self.pay_loc.click()
    #         self.confirm_loc.click()
    #         time.sleep(10)

    def evaluation(self):
        #从介绍页进入完成智能测评
        self.get('http://webapp.leke.cn/leke-ai-h5/#/homePage?newtab=1&close=1')
        return Evaluationpage(self.driver)





