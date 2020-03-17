import pytest
from page.login import Loginpage
from util.MysqlUtil import MysqlUtil
class TestResult():

    def test_result(self,browser):
        '''
        测试结果页、重新测评、调整计划、开启乐学
        :param browser:
        :return:
        '''
        self.result_page = Loginpage(browser).login('955194', 'jia1234567@').result()
        self.result_page.reevaluation()
        self.result_page.adjustplan()
        self.result_page.open()

    def test_revertdata(self):
        '''
        数据更新，将此次测试用例得执行数据物理删除
        :return:
        '''
        d_ai_order_info = 'delete from ai_order_info where parent_id = 850826 and is_deleted = 0;'
        d_ai_member_info = 'delete from ai_member_info where parent_id = 850826 and is_deleted = 0;'
        d_ai_user_test_result = 'DELETE FROM ai_user_test_result WHERE created_by = 850826 and is_deleted = 0;'
        d_ai_user_test_paper = 'DELETE from ai_user_test_paper WHERE parent_id = 850826 and is_deleted = 0;'
        d_ai_user_test_report = 'DELETE from ai_user_test_report WHERE parent_id = 850826 and is_deleted = 0;'
        d_ai_student_plan = 'DELETE from ai_student_plan WHERE parent_id = 850826 and is_deleted = 0;'
        ai_order_info = 'update ai_order_info set is_deleted = 0 WHERE parent_id = 850826;'
        ai_member_info = 'update ai_member_info set is_deleted = 0 where parent_id = 850826;'
        ai_user_test_result = 'update ai_user_test_result set is_deleted = 0 where created_by = 850826;'
        ai_user_test_paper = 'update ai_user_test_paper set is_deleted = 0 where parent_id = 850826;'
        ai_user_test_report = 'update ai_user_test_report set is_deleted = 0 where parent_id = 850826;'
        ai_student_plan = 'update ai_student_plan set is_deleted = 0 where parent_id = 850826;'

        db = MysqlUtil.getConnect(self)
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(d_ai_order_info)
            cursor.execute(d_ai_member_info)
            cursor.execute(d_ai_user_test_result)
            cursor.execute(d_ai_user_test_paper)
            cursor.execute(d_ai_user_test_report)
            cursor.execute(d_ai_student_plan)
            db.commit()
            print('删除数据成功！')
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


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_result.py"])