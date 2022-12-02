from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

tests_path_folder = 'C:/Users/user/function_gen_project/function_gen/list_links/'
# test_file_name= 'DBOFL-T691.mhtml'
list_files = os.listdir(path = tests_path_folder)
test_file_name = list_files[1]
link = tests_path_folder + test_file_name



print(list_files)
print(type(list_files))

print(test_file_name)
print(type(test_file_name))

browser = webdriver.Chrome()
browser.get(link)
time.sleep(10)
