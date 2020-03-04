import pytest
from page.login import Loginpage
import time
class TestResult():

    def test_result(self,browser):
        self.result_page = Loginpage(browser).login('955194', 'jia1234567@').result()
        self.result_page.reevaluation()
        self.result_page.adjustplan()
        self.result_page.open()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_result.py"])