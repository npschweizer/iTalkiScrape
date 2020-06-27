from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time

#from selenium.webdriver.support import expected_conditions as EC

import csv


url = r'https://italki.com/teachers/english'

driver = webdriver.Chrome(r'C:\Users\nates\Documents\chromedriver_win32\chromedriver.exe')

driver.get(url)

driver.maximize_window()

# Function of waiting until the present of the element on the web page

def waiting_func(by_variable, attribute):

    try:

        WebDriverWait(driver, 10).until(lambda x: x.find_element(by=by_variable,  value=attribute))

    except(NoSuchElementException, TimeoutException):

        print('{} {} not found'.format(by_variable, attribute))

        exit()




# tag for teacher results <p class="teachers-result" id="found-teacher-count"><span><strong>4778</strong> teachers found</span></p>
#<button type="button" class="teacher-card-more-menu-btn btn btn-standard btn-default"><span>Message this teacher</span></button>
time.sleep(2)
filterButton = driver.find_element_by_xpath('//div[@class="tag-filter"]')
filterButton.click()
time.sleep(4)
boxButton = driver.find_element_by_xpath('//input[@class="ant-checkbox-input"]')
boxButton.click()
applyButton = driver.find_element_by_xpath('//button[@class="ant-btn filter-apply-btn ant-btn-primary ant-btn-sm"]')
applyButton.click()

csv_file = open('urls.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
pageUrl = ''
teacher_dict = {}
counter = 0
while True:
    #counter += 1
    #if counter > 3:
     #   break
    try:
        waiting_func('xpath', '//button[@class="teachers-more btn btn-standard btn-ghost-default"]')
        button = driver.find_element_by_xpath('//button[@class="teachers-more btn btn-standard btn-ghost-default"]')
        button.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
    except NoSuchElementException:  
        print('working')
        for x in range(1, int(driver.find_element_by_xpath('//p[@class="teachers-result"]/span/strong').text)):
            x_str = str(x)
            teacherButton = driver.find_element_by_xpath(f'''//div[@id="found-teacher-{x_str}"]''')
            teacherButton.click()
            handles = driver.window_handles 
            driver.switch_to.window(handles[1])
            pageUrl = driver.current_url
            driver.close()
            driver.switch_to.window(handles[0])
            teacher_dict['pageUrl'] = pageUrl
            writer.writerow(teacher_dict.values())





    #except Exception as e:
     #   print(e)
      #  csv_file.close()
       # driver.close()
        #break
#button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]') old format, keeping so I remember what the syntax looked like
#Full Tag for Scroll Down: <button type="button" class="teachers-more btn btn-standard btn-ghost-default"><span>SHOW MORE</span></button>
#Teacher Card Detail
#<div class="teacher-card" id="found-teacher-1">

#for i in path:

 #   driver.get(i)

  #  waiting_func('id', 'react-root')

   # a = driver.find_element_by_id('react-root')

    #waiting_func('css selector', "iframe[class='r-1yadl64 r-16y2uox']")

    #b = driver.find_element_by_css_selector("iframe[class='r-1yadl64 r-16y2uox']")

    #waiting_func('tag name', 'iframe')

    #iframe = driver.find_element_by_tag_name('iframe')

    #driver.switch_to.frame(iframe)

    #detail = driver.find_element_by_tag_name('body')



    #waiting_func('class name', 'ep-MetricTopContainer')

    #impression = detail.find_element_by_class_name('ep-MetricTopContainer')

    #print(impression.text)

    #try:

     #   WebDriverWait(driver, 3).until(

      #      lambda x: x.find_element(by='class name', value='ep-ViewAllEngagementsButton'))

    #except TimeoutException:

     #   continue

    #view_all = driver.find_element_by_class_name('ep-ViewAllEngagementsButton')

    #view_all.click()

    #waiting_func('class name', 'ep-EngagementsSection')

    #engagesection = driver.find_element_by_class_name('ep-EngagementsSection')

    #waiting_func('class name', 'ep-MetricTopContainer')

#    engagement = engagesection.find_element_by_class_name('ep-MetricTopContainer')

 #   print(engagement.text)

  #  waiting_func('class name', 'ep-DetailedEngagementsSection')

   # detail = engagesection.find_element_by_class_name('ep-DetailedEngagementsSection')

    #waiting_func('class name', 'ep-SubSection')

    #engagement_details = detail.find_elements_by_class_name('ep-SubSection')

    #for _ in engagement_details:

     #   print(_.text)