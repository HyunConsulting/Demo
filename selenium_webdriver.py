import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Chrome driver 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Google 웹사이트에 접속
# driver.get("https://www.google.com")

url = "https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net#login"
driver.get(url)

# #검색 입력창 찾기 (검색창의 이름이 'q')
# # search_box = driver.find_element(By.NAME,'q')
# search_box = driver.find_element(By.ID,"APjFqb")
id_box = driver.find_element(By.NAME,'loginId')
id_box.send_keys('kyunghyunjo@gamil.com')
pwd_box = driver.find_element(By.NAME,'password')
pwd_box.send_keys('jons00580*')
# log_button = driver.find_element(By.CLASS,'btn_g highlight submit')
# log_button.submit()
time.sleep(5)
driver.save_screenshot('login_result.png')
# #검색어 입력
# search_box.send_keys('Jennie')

# #검색 실행
# search_box.submit()
# time.sleep(5)

# #결과 페이지 스크린 샷 저장
# driver.save_screenshot('search_result.png')

# #브라우저 종료
driver.quit()
