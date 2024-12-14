from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import argparse
import re

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
            element.find_element(by=By.CLASS_NAME, value = 'authorization__btn') # Check if authorization is required
            secure = True
        except:
            secure = False
        try:
            section = element.find_element(by=By.CLASS_NAME, value='opblock-section-request-body')
            description = section.find_element(by=By.CLASS_NAME, value='opblock-description-wrapper')
            tablink = description.find_element(by=By.LINK_TEXT, value='Schema')
            tablink.click()
            # Build schema as a dictionary
            schema = {}
            schema_elements = section.find_elements(by=By.CLASS_NAME, value='property-row')
            for schema_element in schema_elements:
                key = schema_element.text.split('\n')[0].split(' ')[0] 
                value = schema_element.text.split('\n')[0].split(' ')[1]
                example = schema_element.text.split('\n')[1].split(' ')[1]
                schema[key] = {
                    'type': value,
                    'example': example
                }
        except:
            schema = None
        endpoints.append({
            'method': method,
            'path': path,
            'secure': secure,
            'path_param': True if '{' in path else False,
            'schema': schema
        })
    driver.quit()

    base_url = re.search(r'^.+?[^\/:](?=[?\/]|$)', url).group(0)

    return base_url, endpoints

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the Swagger UI')
    args = parser.parse_args()
    print(scrape_endpoints(args.url))