

import pytest
from page.login import Loginpage
from util.MysqlUtil import MysqlUtil

class TestEvaluation():
    def test_update_data(self):
        ai_order_info = 'update ai_order_info set is_deleted = 1 WHERE parent_id = 850826;'
        ai_member_info = 'update ai_member_info set is_deleted = 1 where parent_id = 850826;'
        ai_user_test_result = 'update ai_user_test_result set is_deleted = 1 where created_by = 850826;'
        ai_user_test_paper = 'update ai_user_test_paper set is_deleted = 1 where parent_id = 850826;'
        ai_user_test_report = 'update ai_user_test_report set is_deleted = 1 where parent_id = 850826;'
        ai_student_plan = 'update ai_student_plan set is_deleted = 1 where parent_id = 850826;'
        db = MysqlUtil.getConnect()
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(ai_order_info)
            cursor.execute(ai_member_info)
            cursor.execute(ai_user_test_result)
            cursor.execute(ai_user_test_paper)
            cursor.execute(ai_user_test_report)
            cursor.execute(ai_student_plan)
            db.commit()
            print('更新数据成功！')
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            print("数据库连接关闭！")
            db.close()

    def test_evaluation(self,browser):
        self.evaluation_page = Loginpage(browser).login('955194', 'jia1234567@').evaluation()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_evaluation.py"])