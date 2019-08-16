import yaml
from selenium import webdriver
class Login:
    def login(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        # url='https://www.baicu.com'
        self.driver.get(url)
        cookies = {
            "pgv_pvi": "7961922560",
            "pgv_pvid": "2743265175",
            "RK": "qMjYXnxgOz",
            "ptcz": "aaeb62f3349a30f618b5d0ec7622b8df93c3ec5acdc8016d00f694b2c7343332",
            "tvfe_boss_uuid": "f741249c4c96fac6",
            "o_cookie": "414495467",
            "eas_sid": "K1X5f6Z0z8i4H908n0I843x0W9",
            "uin_cookie": "o0414495467",
            "ied_qq": "o0414495467",
            "LW_uid": "c1M5s6N0L8D5g010g1e2A7N1p8",
            "LW_sid": "Q1Z546v0F895W026P0c5Y838L6",
            "pac_uid": "1_414495467",
            "ptui_loginuin": "414495467@qq.com",
            "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9%2Cen%3Bq%3D0.8",
            "wwrtx.i18n_lan": "zh-cn",
            "_ga": "GA1.2.1851545037.1564885369",
             "ssid":"s2069797800",
                               "wwrtx.ref": "direct",
        "wwrtx.refid": "24347488902947278",
        "wwrtx.ltype": "1",
        "wxpay.corpid": "1970325039078802",
        "wxpay.vid": "1688853275485164",
        "wwrtx.vid": "1688853275485164",
        "wwrtx.logined": "true",
        "_gid": "GA1.2.925684162.1565863202",
        "wwrtx.vst": "xEhI0wIaLSdJOqJmrSxn9tkwvr7UhLfzTYeGZBDiwIYUCI1TTrOQ_O7pFdoabxrhhSJ0swECm7n0hqj1rPS6TQLwh2mAbB368Ff08_Y6sLjCGlntrWR3uH_oMV-yuVIxO25atprsSxipeWlD-PD4DMcoJQkAUAh2dK-EibyIaCLsOxIQOVeoRHfXDhGXLZjAwQSAcjdKiUqOWDRvJc6M__0-8RpCPDcn7b6siYCvFHUjzlw_er4D7zszhV4PaFrUduAKeBb08TZfrSvATTcxKw",
        "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d": "1565660948,1565667178,1565863201,1565925798",
        "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d": "1565925798",
        "_gat": "1",
        "wwrtx.d2st": "a1203331",
        "wwrtx.sid": "Ih_B5m9zrwdwMXH22cWEYx1Aefi7piKaon4z7MGr7jS-nAa7C-9YLDeXHq8KHb8y",

        }

        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)