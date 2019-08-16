import time
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.common_method.Find_Element import Find_Element


class MgtTool_Page(Find_Element):
    def setup(self):
            self.dict = yaml.load(open(r'\WeWork\data\element.yaml'))
    def test_add_picture(self,image_path=None):
        # 点击管理工具
        self.CSS(self.dict['mgt_tools']).click()
        # 点击素材库
        self.CSS(self.dict['M_storage']).click()
        # 点击图片
        self.CSS(self.dict['image_click']).click()
        # 点击添加图片
        self.CSS(self.dict['image_add']).click()
        # 上传图片
        if image_path == None:
            try:
                self.CSS(self.dict['image_upload']) \
                    .send_keys(r'\WeWork\config\image.jpg')
            except Exception as e:
                print(e)
        else:
            try:
                self.CSS(self.dict['image_upload']) \
                    .send_keys(image_path)
            except Exception as e:
                print(e)
        # 判断是否上传成功
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel"))
        )
