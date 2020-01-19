

import pytest
from page.login import Loginpage

class TestEvaluation():
    def test_evaluation(self,browser):
        self.evaluation_page = Loginpage(browser).login('955194', 'jia1234567@').evaluation()
        self.evaluation_page.start()
        self.evaluation_page.first_step()
        self.evaluation_page.second_step()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_evaluation.py"])