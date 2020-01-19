'''
@Time    : 2019/12/21 16:03
@Author  : fzj
@Desc    : 登录页
'''
from poium import Page, PageElement
from page.redirect import Redirectpage

class Loginpage(Page):
    loginname_loc = PageElement(name='loginName')
    password_loc = PageElement(name='password')
    login_loc = PageElement(id_='jLogin')

    def login(self,loginname,password):
        self.get("https://cas.leke.cn/login?service=")
        self.loginname_loc = loginname
        self.password_loc = password
        self.login_loc.click()
        self.get("http://webapp.leke.cn/leke-ai-h5/#/redirect?studentId=850818")
        #self.get("http://webapp.leke.cn/leke-ai-pad/#/redirect")
        return Redirectpage(self.driver)

