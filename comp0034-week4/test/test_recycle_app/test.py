from selenium import webdriver

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  

DRIVER_PATH = '/usr/local/bin/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://127.0.0.1:8050/') # change this link with our own website.