import pytest
from page.login import Loginpage

class TestResult():

    def test_result(self,browser):
        self.result_page = Loginpage(browser).login('955194', 'jia1234567@').result()
        self.test_page = self.result_page.reevaluation()
        self.test_page.first_step()
        self.test_page.second_step()

        self.result_page.adjustplan().adjust()
        self.result_page.open()



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_result.py"])