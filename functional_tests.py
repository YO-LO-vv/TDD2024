from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox ()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 张三听说有一个在线代办事项的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页里包含“TO-DO” 这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do',header_text)

        #应用有一个输入代办事项的文本输入框
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #他在文本输入框中输入了"Buy flowers"
        inputbox.send_keys('Buy flowers')

        #他按了回车键后，页面更新了
        #代办事项表格中显示了"1: Buyflowers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table =  self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn('1: Buy flowers', [row.text for row in rows])

        #页面中又显示了一个文本输入框，可以输入其他代办事项
        #他输入了"Send a gift to Lisi"
        self.fail('Finish the test!')
        #页面再次更新，她的清单中显示了这两个代办事项

        #张三想知道这个网站是否会记住他的清单
        #他看到网站为他生成了一个唯一的URL

        #他访问那个URL，发现它的代办事项列表还在
        #他满意地离开了


if __name__ == '__main__':
    unittest.main()
