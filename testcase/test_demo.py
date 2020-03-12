import pytest
from page.login import Loginpage

class TestDemo:

    def test_login(self,browser):
        """登录"""
        self.login_page = Loginpage(browser).login('955194', 'jia1234567@')

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_demo.py"])