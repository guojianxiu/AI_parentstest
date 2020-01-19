from poium import Page, PageElement,PageElements

class Resultpage(Page):
    #重新测评
    reevaluation = PageElement(xpath = '//*[@id="root"]/div/div/div[1]/a')
    pass