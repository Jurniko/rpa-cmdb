import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #Condiciones de sepera
import pandas as pd
from datetime import datetime

from src.utils.is_in_dictionary import IsInDictionary


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

limitDate = datetime(2022,11,7,6,0,0)
mails =[{}]

cont = 0
for element in elements_mails:

    cont += 1
    print(f'============= CORREO {cont} ================')
    #print(element.text)

    # Extract 

    dataHeader = element.find_elements(By.CSS_SELECTOR,'.Ejrkd')
    author = dataHeader[0].text # author
    title = dataHeader[1].text # title
    date = dataHeader[2].text # date
    subject = dataHeader[3].text # subject


    mails.append([
    { 'author': author,
    'title':title,
    'subject': subject}
    ])

       
    # Into mail

    element.click()
    """
    !PROBLEMA
    p1: Si ingresa en cada correo, podría encontrar TABLAS innecesarias
    s1: Convertir todo el correo en relación a los SELECTORES y convertirlos en TEXTO, y buscar 
    palabras claves de un DICCIONARIO predefinido.
    """

  
    wait = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.MtujV .L72vd')))
  
    textHtml = driver.find_element(By.CSS_SELECTOR,'.MtujV .L72vd').text
    
    print(IsInDictionary(textHtml).code('A1'))
    if(IsInDictionary(textHtml).code('A1') == False):
        continue

    print('### INICIANDO BUSQUEDA DE TABLAS ### \t')
  
    #Tables
    try: 
        # !! PREVEEER QUE PUEDEN HABER 2 TABLAS EN UN CORREO
        tableHtml = driver.find_element(By.CSS_SELECTOR,'.MtujV .L72vd table').get_attribute('outerHTML')
        df_table = pd.read_html(tableHtml)[0]
        print('Si tiene Tablas')
        #print(df_table)

    except:
        print('No tiene Tablas')
 
    #for table in tables:
    #    print(table.text)
    
    print('### FIN  ### \t')
    if (cont == 6):
        break
        

time.sleep(20)
