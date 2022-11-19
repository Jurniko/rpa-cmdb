from selenium.webdriver.support.wait import WebDriverWait

def check_elem_state(xpath):
    try:
        WebDriverWait(driver, 1, 1).until(EC.presence_of_element_located((By.XPATH, login_xpath)))
        print('Element present')
    except:
        print('Sorry - not present')

    try:
        WebDriverWait(driver, 1, 1).until(EC.visibility_of_element_located((By.XPATH, login_xpath)))
        print('Element visible')
    except:
        print('Sorry - not visible')

    try:
        WebDriverWait(driver, 1, 1).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        print('Element clickable')
    except:
        print('Sorry - not clickable')