from selenium import webdriver
from datetime import datetime
import pytz

def _get_contents(usr_id, usr_pw):
    # Base Setup
    driver = webdriver.PhantomJS(executable_path='phantomjs', service_args=['--ignore-ssl-errors=true'])
    driver.implicitly_wait(1)
    base_url = 'http://credit.snue.ac.kr/sub/board.snue?boardId=credit_notice&mid=42'

    # Get HTML
    driver.get(base_url)
    titles = driver.find_elements_by_xpath('/html/body/div/ul/li/a')
    dates = driver.find_elements_by_xpath('/html/body/div/ul/li/span')

    result = []

    if len(titles)==len(dates):
        for i in range(len(titles)):
            title = titles[i].text
            url = titles[i].get_attribute('href')
            date = dates[i].text
            py_date = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
            tp = dict(title=title, url=url, py_date=py_date, date=date)
            result.append(tp)

    return result
