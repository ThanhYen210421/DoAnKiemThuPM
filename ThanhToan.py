import time

from selenium import webdriver
from selenium.webdriver import ActionChains as A
from selenium.webdriver.common.by import By as B
from selenium.webdriver.support.select import Select as S

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.maximize_window()
driver.get('https://thegioiskinfood.com/')

# Đóng quảng cáo
driver.implicitly_wait(15)
driver.find_element(B.CLASS_NAME,'windownpopup_close').click()

# Đóng MessagesBox
time.sleep(2)
iframeMes = driver.find_element(B.XPATH, '//*[@id="fb-root"]/div[2]/span/iframe')
driver.switch_to.frame(iframeMes)
time.sleep(4)
driver.find_element(
    B.XPATH,
    "/html/body/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/div",
).click()
driver.switch_to.default_content()

# Đăng nhập
driver.find_element(B.CLASS_NAME, "f-header-top-icon-account").click()
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(3) > input').send_keys("mailtest3@gmail.com")
time.sleep(3)
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(4) > input').send_keys("123456789hihi")
time.sleep(3)
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

#vaogiohang
time.sleep(3)
driver.find_element(B.CLASS_NAME,'f-header-top-icon-cart').click()
driver.find_element(B.XPATH,'//*[@id="sidenav"]/div/div[4]/div[3]/div/div[2]/a[1]').click()
#thanhtoan
time.sleep(2)
'''driver.find_element(B.CSS_SELECTOR,'#u_0_0_lG > div > div > div > div > div > div._a2zp > div._9dzn > div._9q4i > div > div').click()'''
driver.find_element(B.XPATH,'//*[@id="cart-page"]/div[1]/div[2]/div[1]/div[4]/div/div[2]/a').click()
driver.find_element(B.ID,'billing_address_full_name').clear()
driver.find_element(B.ID,'billing_address_full_name').send_keys("Như Ý")
time.sleep(2)
driver.find_element(B.ID,'billing_address_phone').clear()
driver.find_element(B.ID,'billing_address_phone').send_keys("0999999999")
time.sleep(2)
driver.find_element(B.ID,'billing_address_address1').clear()
driver.find_element(B.ID,'billing_address_address1').send_keys("Tử Cấm Thành")
time.sleep(2)
tinhthanh = S(driver.find_element(B.ID,'customer_shipping_province'))
tinhthanh.select_by_value("42")
time.sleep(2)
quanhuyen = S(driver.find_element(B.ID,'customer_shipping_district'))
quanhuyen.select_by_value("459")
time.sleep(2)
phuongxa = S(driver.find_element(B.ID,'customer_shipping_ward'))
phuongxa.select_by_value("24472")
time.sleep(2)
driver.find_element(B.CSS_SELECTOR,'#form_next_step > button').click()
#driver.find_element(B.CSS_SELECTOR,'#form_next_step > button > span').click()
#thoattaikhoan
driver.find_element(B.ID,'customer_logout_link').click()

driver.close()
