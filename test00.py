from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #클릭후 이미지로딩 기다리기
import urllib.request
import os

driver = webdriver.Chrome("c:/chromedriver.exe")


driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") # 구글 이미지 검색창
#elem = driver.find_element_by_name("q") #구를 검색창 name으로 찾기
#elem = driver.find_element_by_class_name("gLFyf.gsfi") # 구글 검색창 클래스롤 찾기
search= input("찾을 이미지를 입력하세요!") #키워드 입력
elem = driver.find_element_by_name("q")
elem.send_keys(search) #원하는 키워드 입력
elem.send_keys(Keys.RETURN) # 엔터



# 입력 디렉토리
directory = search + "/"
#save_path = "/Users/danuri/Desktop/images/" + search_term + "/"
#    create_folder_if_not_exists(save_path)


#  디렉토리 생성
if not os.path.exists(directory):
    os.makedirs(directory)



i=0
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        i+=1
        os.makedirs(directory+str(i))
        print('디렉토리 추가' +str(i))
# 저장 경로 설정



# 이미지 크룰링하기
#images = driver.find_element_by_xpath('//input[@type="image"][@src="/images/btn_next.png"]').click()
#images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute('src')
        urllib.request.urlretrieve(imgUrl, directory+ search + str(count) + ".jpg")

        print("Image saved:"+ search +"_{}.jpg".format(count))

        count += 1
    except:
        pass

driver.close()
