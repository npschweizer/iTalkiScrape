from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException

import pandas as pd

import csv

import time

def waiting_func(by_variable, attribute):

    try:

        WebDriverWait(driver, 10).until(lambda x: x.find_element(by=by_variable,  value=attribute))

    except (NoSuchElementException, TimeoutException):

        print('{} {} not found'.format(by_variable, attribute))

        exit()


#from csv into list of urls
df = pd.read_csv('urls1.csv', header = None)
urlList = list(df[df.columns[0]])
#csv_file = open('urls.csv', 'w', encoding='utf-8', newline='')

csv_file = open('teacherData1.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

print(urlList)
for url in urlList:
    driver = webdriver.Chrome(r'C:\Users\nates\Documents\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)    
    #pageUrl = ''
    teacher_dict = {}
    
    #name = driver.find_element_by_xpath('.//div[@class="teacherCard-name"]').text
    #waiting_func('xpath', './/div[@class="teacherCard-name"]')
    waiting_func('xpath', './/span[@class="number"]')
    rating = driver.find_element_by_xpath('.//span[@class="number"]').text
    waiting_func('xpath', './/div[@class="teacherCard-right-body"]/div[2]/span')
    lessons = driver.find_element_by_xpath('.//div[@class="teacherCard-right-body"]/div[2]/span').text
    waiting_func('xpath', './/div[@class="teacherCard-right-body"]/div[3]/span')
    students = driver.find_element_by_xpath('.//div[@class="teacherCard-right-body"]/div[3]/span').text
    aboutMeList = str()
    try:
        descButton = driver.find_element_by_xpath('.//span[@class="readMore"]')
        descButton.click()
        aboutMe = driver.find_elements_by_xpath('.//div[@class = "aboutMe-content"]')
        aboutMe1 = aboutMe[0].text
        teacher_dict['aboutMe1'] = aboutMe1
        aboutMe2 = aboutMe[1].text
        teacher_dict['aboutMe2'] = aboutMe2
        aboutMe3 = aboutMe[2].text
        teacher_dict['aboutMe3'] = aboutMe3    
    except NoSuchElementException:
        try:
            aboutMe = driver.find_elements_by_xpath('.//div[@class = "TextOverflow"]').text
            teacher_dict['aboutMe1'] = aboutMe
            teacher_dict['aboutMe2'] = str()
            teacher_dict['aboutMe3'] = str()
        except:
            teacher_dict['aboutMe1'] = str()
            teacher_dict['aboutMe2'] = str()
            teacher_dict['aboutMe3'] = str()
    except:
        pass


    months = driver.find_elements_by_xpath('//span[@class="ProgressBar-col-number-bg"]')
    if len(months) == 0:
        months = driver.find_elements_by_xpath('//span[@class="progressBar-col-number"]')
    try:
        march = months[0].text
        april = months[1].text
        may = months[2].text
    except:
        march = str()
        april = str()
        may = str()
    waiting_func('xpath', './/div[@class = "statistic-number"]')
    totalLessons = driver.find_element_by_xpath('.//div[@class = "statistic-number"]').text
    #marchLessons = driver.find_element_by_xpath('.//span[@class="progressBar-col-number-bg"][1]').text
    #aprilLessons = driver.find_element_by_xpath('.//span[@class="progressBar-col-number-bg"][2]').text
    #mayLessons = driver.find_element_by_xpath('.//span[@class="progressBar-col-number-bg"][3]').text

    teacher_dict['url'] = url
    teacher_dict['rating'] = rating
    teacher_dict['lessons'] = lessons
    teacher_dict['students'] = students
    teacher_dict['totalLessons'] = totalLessons
    teacher_dict['marchLessons'] = march
    teacher_dict['aprilLessons'] = april
    teacher_dict['mayLessons'] = may
    waiting_func('xpath', '//button[@class="small-schedule-button btn btn-big btn-ghost-default"]')
    button = driver.find_element_by_xpath('//button[@class="small-schedule-button btn btn-big btn-ghost-default"]')
    button.click()
    unavailable = []
    booked = []
    available = []

    for x in range(0,4):
        time.sleep(2)
        unavailable.append(len(driver.find_elements_by_xpath('//div[@class="calendar-cell"]')))
        booked.append( len(driver.find_elements_by_xpath('//div[@class="calendar-cell calendar-cell-booked"]')))
        available.append(len(driver.find_elements_by_xpath('//div[@class="calendar-cell calendar-cell-actived"]')))
        weekButton = driver.find_element_by_xpath('//button[@class="next-week"]')
        weekButton.click()
    teacher_dict['unavailable'] = unavailable
    teacher_dict['available'] = available
    teacher_dict['booked'] = booked
    writer.writerow(teacher_dict.values())
    


    #find_elements_by_class_name('//class[@class = "caption calendar-cell-container"]')
    #right button tage: <button type="button" class="next-week"><img width="7" height="14" src="/static/media/right.9b54dcb2.svg" alt="next"></button>






# Function of waiting until the present of the element on the web page





# tag for teacher results <p class="teachers-result" id="found-teacher-count"><span><strong>4778</strong> teachers found</span></p>
#<button type="button" class="teacher-card-more-menu-btn btn btn-standard btn-default"><span>Message this teacher</span></button>







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