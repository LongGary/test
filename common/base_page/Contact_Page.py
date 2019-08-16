import time
import yaml
from selenium.webdriver.common.by import By
from common.common_method.Find_Element import Find_Element
class Test_Page(Find_Element):
    def setup(self):
        self.login()
        self.dict = yaml.load(open(r'\WeWork\data\element.yaml'))
        self.driver.implicitly_wait(5)

    def test_member(self,name=None,s_name=None,acount=None,phone=None):
            if name==None and s_name==None and acount==None and phone==None:
                element_add = self.Xpath(self.dict['e_add_member'])
                self.driver.execute_script("arguments[0].click();", element_add)
                # 姓名
                self.CSS(self.dict['e_name'])\
                    .send_keys( "等风来 %s" % str(time.time()))
                # 别名
                self.CSS(self.dict['e_sname'])\
                    .send_keys("龙家里 %s" % str(time.time()))
                # 账号
                self.CSS(self.dict['e_account'])\
                    .send_keys(" %s" % int(time.time()))
                # 手机号
                self.CSS(self.dict['e_phone'])\
                    .send_keys("1%s" % int(time.time()))
                # 点击保存
                element_save = self.Xpath(self.dict['e_save'])
                self.driver.execute_script("arguments[0].click();", element_save)
                assert "等风来" in self.driver.page_source
            else:
                element_add = self.CSS(self.dict['e_add_member'])
                self.driver.execute_script("arguments[0].click();", element_add)
                # 姓名
                self.CSS(self.dict['e_name']) \
                    .send_keys(name)
                # 别名
                self.CSS(self.dict['e_sname'])\
                    .send_keys(s_name)
                # 账号
                self.CSS(self.dict['e_account']).send_keys(acount)
                # 手机号
                self.CSS(self.dict['e_phone']).send_keys(phone)
                # 点击保存
                element_save = self.Xpath(self.dict['e_save'])
                self.driver.execute_script("arguments[0].click();", element_save)
                assert name in self.driver.page_source
    def test_member(self,serch_name=None):
        if serch_name == None:
            serch_button=self.CSS(self.dict['e_serch'])
            serch_button.send_keys('龙家里')
        else:
            serch_button = self.CSS(self.dict['e_serch'])
            serch_button.send_keys(serch_name)
    def disable_meber(self):
        #禁用
        self.CSS(self.dict['e_disable']).click()
        self.CSS(self.dict['e_submit']).click()
    def delet_member(self):
        #删除
        self.CSS(self.dict["e_delet"]).click()
        self.CSS(self.dict['e_submit']).click()







