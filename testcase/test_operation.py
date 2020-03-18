import pytest
from page.login import Loginpage

class TestOperation():

    def test_operation(self,browser):
        """
        查看操作页
        """
        self.loperation_page = Loginpage(browser).login('955194', 'jia1234567@').operation()
        self.loperation_page.todayplan()
        self.loperation_page.history()
        assert 4 == self.loperation_page.taskslen()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_demo.py"])