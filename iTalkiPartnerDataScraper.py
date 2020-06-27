from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time

def waiting_func(by_variable, attribute):

    try:

        WebDriverWait(driver, 10).until(lambda x: x.find_element(by=by_variable,  value=attribute))

    except (NoSuchElementException, TimeoutException):

        print('{} {} not found'.format(by_variable, attribute))

        exit()


#from csv into list of urls

csv_file = open('teachers.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

for i in range(1, length(urlList)):
    url = urlList[i]
    driver = webdriver.Chrome()
    driver.get(url)

    
    pageUrl = ''
    teacher_dict = {}
    name = find_element_by_xpath('.//div[@class="teacherCard-name"]').text
    lessonsStudents = find_element_by_xpath('.//div[@class="teacherCard-right-body"]').text
    totalLessons = find_element_by_xpath('.//div[@class = "statistic-number"]')[1].text
    marchLessons = find_element_by_xpath('.//div[@class="progressBar-col-number-bg"]')[1].text
    aprilLessons = find_element_by_xpath('.//div[@class="progressBar-col-number-bg"]')[2].text
    mayLessons = find_element_by_xpath('.//div[@class="progressBar-col-number-bg"]')[3].text
    teacher_dict['name'] = name
    teacher_dict['lessonsStudents'] = lessonsStudents
    writer.writerow(review_dict.values())
    button = driver.find_element_by_xpath('//button[@class="small-schedule-button btn btn-big btn-ghost-default"]')
    button.click()
    time.sleep(2)    
    <<Needs something that counts by cell type and presses the right button 3x

    #find_elements_by_class_name('//class[@class = "caption calendar-cell-container"]')
    #right button tage: <button type="button" class="next-week"><img width="7" height="14" src="/static/media/right.9b54dcb2.svg" alt="next"></button>
    #<div class="calendar-cell"></div>
    #<div class="calendar-cell calendar-cell-booked"></div>
    #<div class="calendar-cell calendar-cell-actived"></div>





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