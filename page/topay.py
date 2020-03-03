from poium import Page, PageElement

class Resultpage(Page):
    # 前往支付
    topay_loc = PageElement('//*[@id="root"]/div/div/div[4]/a')
    #已拥有平板
    own_loc = PageElement('//*[@id="am-modal-container-1583215695812"]/div/div[2]/div/div/div[3]/div/a[2]')



    def topay(self):
        self.topay_loc.click()
        Resultpage(self.driver)
        self.own_loc.click()