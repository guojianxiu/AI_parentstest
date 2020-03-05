from poium import Page, PageElement
import time

class Topaypage(Page):
    # 前往支付
    topay_loc = PageElement(xpath = '//*[@id="root"]/div/div/div[4]/a')
    #已拥有平板
    own_loc = PageElement(link_text = '已拥有')

    def topay(self):
        self.topay_loc.click()
        time.sleep(3)
        Topaypage(self.driver)
        self.own_loc.click()