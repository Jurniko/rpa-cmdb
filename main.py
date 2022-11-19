import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #Condiciones de sepera
import pandas as pd
import json

from bs4 import BeautifulSoup # Parse Selenium to HTML


#driver = webdriver.Chrome()
driver = webdriver.Edge()


driver.maximize_window()
driver.get('https://outlook.office365.com/mail/')

#driver.implicitly_wait(100)

# .hcptT => mails input
#  .gMkyO => author

"""
CONSIDERAR LO SIGUIENTE: 
    CREAR UN INPUT() Y ESPERAR A QUE SE LOGUEE PARA PROCEDER CON LAS FUNCIONALIDADES DEL ROBOT
    : ESTO PORQUE INPUT() HACE QUE EL CÓDIGO NO AVANCE Y SE QUEDE A LA ESPERA DE UN VALOR.
"""
##time.sleep(40)
"""
    WebDriverWait ( elemento a la espera, tiempo máximo de espera sino error )
"""


WebDriverWait(driver, 40).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.hcptT')))


elements_mails = driver.find_elements(By.CSS_SELECTOR, '.hcptT')

print(elements_mails.count)


mails = [{
    'author': '',
    'title':'',
    'subject':''
}]



cont = 0
for element in elements_mails:

    cont += 1
    print(cont)

    # Extract 

    """author = element.find_element(By.CSS_SELECTOR,'.gMkyO')
    title = element.find_element(By.CSS_SELECTOR,'.IjzWp')
    subject = element.find_element(By.CSS_SELECTOR,'.FqgPc')

    mails.append([
    { 'author': author.text,
    'title':title.text,
    'subject': subject.text}
    ])

    print(author.text + '\t')
    print(title.text + '\t')
    print(subject.text + '\t')"""
    print('########### INICIANDO BUSQUEDA DE TABLAS ######## \t')
   
    # Into mail

    element.click()

  
    wait = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.MtujV .L72vd')))

    #Tables
    #tables = driver.find_elements(By.CSS_SELECTOR,'.MtujV .L72vd table')
    tableHtml_toParse = driver.find_element(By.CSS_SELECTOR,'.MtujV .L72vd table').get_attribute('outerHTML')

    #print(tableHtml_toParse)
   
   
    #pdParseHtml =  BeautifulSoup(tableHtml_toParse, 'html.parser')

    #df_table = pd.read_html(str(pdParseHtml))
    tableHtml_toParse = """
    <table>
    <thead>
        <tr>
        <th>date</th>
        <th>name</th>
        <th>year</th>
        <th>cost</th>
        <th>region</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>2020-01-01</td>
        <td>Jenny</td>
        <td>1998</td>
        <td>0.2</td>
        <td>South</td>
        </tr>
        <tr>
        <td>2020-01-02</td>
        <td>Alice</td>
        <td>1992</td>
        <td>-1.34</td>
        <td>East</td>
        </tr>
        <tr>
        <td>2020-01-03</td>
        <td>Tomas</td>
        <td>1982</td>
        <td>1.00023</td>
        <td>South</td>
        </tr>
    </tbody>
    </table>
    """

    data = BeautifulSoup(tableHtml_toParse, 'html.parser')
    
    df_table = pd.read_html(tableHtml_toParse)
 
 
    #for table in tables:
    #    print(table.text)
        
    df_table[0]
  
    print('########### FIN  ######## \t')
    if (cont == 6):
        break
        

    time.sleep(10)
    break
