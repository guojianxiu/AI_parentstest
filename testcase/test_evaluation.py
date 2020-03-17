import pytest
from page.login import Loginpage
from util.MysqlUtil import MysqlUtil

class TestEvaluation():
    def test_update_data(self):
        '''
        将目前已有计划数据逻辑删除
        :return:
        '''
        ai_order_info = 'update ai_order_info set is_deleted = 1 WHERE parent_id = 850826;'
        ai_member_info = 'update ai_member_info set is_deleted = 1 where parent_id = 850826;'
        ai_user_test_result = 'update ai_user_test_result set is_deleted = 1 where created_by = 850826;'
        ai_user_test_paper = 'update ai_user_test_paper set is_deleted = 1 where parent_id = 850826;'
        ai_user_test_report = 'update ai_user_test_report set is_deleted = 1 where parent_id = 850826;'
        ai_student_plan = 'update ai_student_plan set is_deleted = 1 where parent_id = 850826;'
        db = MysqlUtil.getConnect(self)
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
            db.close()
            print("数据库连接关闭！")

    def test_evaluation(self,browser):
        '''
        执行智能测评第一步第二步
        :param browser:
        :return:
        '''
        self.evaluation_page = Loginpage(browser).login('955194', 'jia1234567@').evaluation()
        self.evaluation_page.start()
        self.evaluation_page.first_step()
        self.evaluation_page.second_step()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_evaluation.py"])