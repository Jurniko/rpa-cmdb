import pandas as pd
from .str_unformat import str_unformat 
import os
from pathlib import Path
import time
class DfCMBD:
    global root_excel_path
    root_excel_path = './input/data.xlsx'
    global temp_excel_path
    temp_excel_path = './output/data_temp.xlsx'
    global output_excel_path 
    output_excel_path = './output/data_update.xlsx'
    
    def __init__(self):

        try:
            open(temp_excel_path).close() # Si no existe, error!
            self.df_root = self.df_format_to_root(pd.read_excel(temp_excel_path))
            print("ga")
        except:
            self.df_root = self.df_format_to_root(pd.read_excel(root_excel_path, sheet_name='Hoja1'))
            print("gaNO")
       
    def append_df(self, i_df):
        i_df = self.df_format_to_root(i_df)
        df_main = pd.concat([self.df_root, i_df], ignore_index=True)
        self.df_root = df_main

        self.save_temp()

    def save_temp(self):
        self.df_root.to_excel(temp_excel_path)
        #time.sleep(5)

    def to_excel(self, path = './output/data_temp.xlsx'):
        self.df_root.to_excel(path)
    
    def show(self):
        print(self.df_root)
     

    def df_format_to_root(self, i_df):
        root_columns = {
                'categoria'     :['categoria'],
                'hostname'	    :['hostname', 'host'],
                'ip'	        :['ip'],
                'descripcion'   :['descripcion']	,
                'servicio'      :['servicio'],
                'plataforma'	:['plataforma'],
                'edicion'	    :['edicion'],
                'version'	    :['version'],
                'administracion':['administracion'],
                'ambiente'	    :['ambiente'],
                'estado'	    :['estado'],
                'marca'	        :['marca'],
                'modelo'        :['modelo']	,
                'tipo'	        :['tipo'],
                'serie'	        :['serie'],
                'ubicacion'     :['ubicacion'],
                'hmc_fms'       :['hmc_fms', 'hmc/fms'],
                'rack'          :['rack'],
                'ur'	        :['ur'],
                'contenedor'    :['contenedor'],
                'hypervisor'    :['hypervisor'],
                'vcpu'          :['vcpu'],
                'ram'           :['ram', 'ram (gb)', 'ram(gb)'],
                'hdd'           :['hdd', 'hdd (gb)', 'hdd(gb)'],
                'procesador'    :['procesador'],
                'bahia'         :['bahia'],
                'propiedad'     :['propiedad', 'propiedades'],
                'inicio_garantia':['inicio_garantia', 'inicio garantia'],
                'venc_garantia' :['venc_garantia', 'venc garantia'],
                'garantia'      :['garantia']	,
                'empresa'	    :['empresa'],
                'inicio_contrato':['inicio_contrato', 'inicio contrato'],
                'venc_contrato' :['venc_contrato', 'venc. contrato'],
                'contrato'	    :['contrato'],
                'observaciones'	:['observaciones', 'observacion'],
                'fecha_alta'    :['fecha_alta', 'fecha alta']
            }
        for i_column in  i_df.columns:

            for root_column, ref_columns in root_columns.items():
                #if(ref_columns.get(key).index(column.lower()) != -1 ): #Buscamos el nombre columna nueva en elarray de 'supuestos' nombres, para convertirla al estandar.
                if(str_unformat(i_column) in ref_columns): #Buscamos el nombre columna nueva en el array de'supuestos' nombres, para convertirla al estandar.
                    to_rename = {}
                    to_rename[i_column] = root_column
                    i_df = i_df.rename(columns=to_rename)

        return i_df
        


    #def existsInArray(arr, val):
        


