from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import argparse

def scrape_endpoints(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    endpoints = []

    # Find Swagger endpoints
    elements = driver.find_elements(by=By.CLASS_NAME, value='opblock')
    for element in elements:
        element.click()
        method = element.find_element(by=By.CLASS_NAME, value='opblock-summary-method').text
        path = element.find_element(by=By.CLASS_NAME, value='opblock-summary-path').text
        try:
            section = element.find_element(by=By.CLASS_NAME, value='opblock-section-request-body')
            description = section.find_element(by=By.CLASS_NAME, value='opblock-description-wrapper')
            tablink = description.find_element(by=By.LINK_TEXT, value='Schema')
            tablink.click()
            request_body = f'{{\n{description.find_element(by=By.CLASS_NAME, value='inner-object').text}\n}}'
        except:
            request_body = None
        endpoints.append({
            'method': method,
            'path': path,
            'request_body': request_body
        })
    driver.quit()

    return json.dumps(endpoints)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the Swagger UI')
    args = parser.parse_args()
    print(scrape_endpoints(args.url))