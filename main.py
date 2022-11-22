import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #Condiciones de sepera
import pandas as pd
from datetime import datetime

from src.utils.is_in_dictionary import IsInDictionary
from src.utils.df_cmbd import DfCMBD

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

mails = [{}]
cont = 0

for element in elements_mails:

    cont += 1
    print(f'============= CORREO {cont} ================')
    #print(element.text)

    # Extract 

    emailHeaderData = element.find_elements(By.CSS_SELECTOR,'.Ejrkd')
    author = emailHeaderData[0].text # author
    title = emailHeaderData[1].text # title
    date = emailHeaderData[2].text # date
    subject = emailHeaderData[3].text # subject


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

  
    # .MtujV .L72vd => Todo el relleno del correo
    # .AL_OM => Hora del correo
    wait = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.MtujV .L72vd .AL_OM' )))
  
    textHtml = driver.find_element(By.CSS_SELECTOR,'.MtujV .L72vd').text
    hora_sf = driver.find_element(By.CSS_SELECTOR,'.AL_OM' ).text
    horadt = datetime.strptime(hora_sf[4:len(hora_sf)], '%d/%m/%Y %H:%M')

    # Condicionales de busqueda 
    # ! Tener en cuenta que podriamos usar solo el TITULO y el ASUNTO y no TODO EL CONTENIDO esto por rendimiento

    if(IsInDictionary(textHtml).code('A1') == False):
        continue

    print('### INICIANDO BUSQUEDA DE TABLAS ### \t')
  
    #Tables
    try: 
        # !! PREVEEER QUE PUEDEN HABER 2 TABLAS EN UN CORREO
        tableHtml = driver.find_element(By.CSS_SELECTOR,'.MtujV .L72vd table').get_attribute('outerHTML')
        df_table = pd.read_html(tableHtml)[0]
        df_table = df_table.rename(columns=df_table.iloc[0]).drop(df_table.index[0]) #Corrigiendo la cabecera de la tabla
     

     
        df_date_append = pd.DataFrame({"Categoria":[datetime.today().strftime('%Y-%m-%d %H:%M:%S')]})

        a = DfCMBD()
        a.append_df(df_date_append)
        a.append_df(df_table)
        a.show()
       

        #dfa.to_excel('aaaa.xlsx')
        #print(df_table)

    except:
        print('No tiene Tablas')
 
    #for table in tables:
    #    print(table.text)
    
    print('### FIN  ### \t')
    if (cont == 6):
        break
        

time.sleep(20)
