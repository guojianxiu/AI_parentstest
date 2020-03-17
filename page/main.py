from poium import Page, PageElement,PageElements
from page.evaluation import Evaluationpage
from page.result import Resultpage
from page.operation import Operationpage
from page.topay import Topaypage
from page.adjustplan import Adjustplanpage

class Mainpage(Page):
    #续费判断按钮
    continue_loc = PageElement(link_text = '您的服务已到期，请续费。')
    #乐学报告进入下一期
    nextplan_loc = PageElement(link_text = '进入下一期计划')
    changeplan_loc = PageElement(link_text = '调整计划')

    def continue_pay(self):
        Mainpage(self.driver)
        if self.continue_loc:
            Topaypage(self.driver).topay()

    def evaluation(self):
        #从介绍页进入智能测评
        self.get('http://webapp.leke.cn/leke-ai-h5/#/homePage?newtab=1&close=1')
        return Evaluationpage(self.driver)

    def result(self):
        #测评结果到支付
        self.get('http://webapp.leke.cn/leke-ai-h5/#/result?newtab=1&close=1')
        return Resultpage(self.driver)

    def operation(self):
        #操作页
        self.get('http://webapp.leke.cn/leke-ai-h5/#/operation?newtab=1&close=1')
        return Operationpage(self.driver)

    def report(self):
        Mainpage(self.driver)
        if self.nextplan_loc:
            self.changeplan_loc.click()
            Adjustplanpage(self.driver).adjust()
            self.nextplan_loc.click()

    '''
    家长端主要可以保留得页面有：
    介绍页：http://webapp.leke.cn/leke-ai-h5/#/homePage?newtab=1&close=1
    测评结果页：http://webapp.leke.cn/leke-ai-h5/#/result?newtab=1&close=1
    重新测评：http://webapp.leke.cn/leke-ai-h5/#/measurement/index
    调整计划：http://webapp.leke.cn/leke-ai-h5/#/plan
    续费页面：http://webapp.leke.cn/leke-ai-h5/#/order?newtab=1&close=1
    操作页：http://webapp.leke.cn/leke-ai-h5/#/operation?newtab=1&close=1
    乐学报告页：http://webapp.leke.cn/leke-ai-h5/#/report?newtab=1&close=1

    '''
