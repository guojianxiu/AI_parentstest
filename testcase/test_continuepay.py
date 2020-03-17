import pytest
from page.login import Loginpage

class TestContinuepay():

    def test_continuepay(self,browser):
        '''
        继续支付
        :param browser:
        :return:
        '''
        self.other_page = Loginpage(browser).login('955194', 'jia1234567@')
        self.other_page.continue_pay()
        self.other_page.report()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_continuepay.py"])