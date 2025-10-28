from page.login_page import Login_Page

def test_login(driver):
    #crear objeto
    loginpage = Login_Page(driver)
    loginpage.open()
    loginpage.login()