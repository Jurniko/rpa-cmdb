
import re

class IsInDictionary:
    def __init__(self, text):
        global str_text 
        str_text = text

    def code(self, str_code):
        default = 'A1'
        return getattr(self, 'exe_code_'+str_code, lambda: default)()

    # exe_code_A1  => dictionary_identify_mail_cmbd
    def exe_code_A1(self):

        aDictionary = [i.strip('\n') for i in open('./input/dictionary_identify_mail_cmbd.txt', mode="r", encoding="utf-8").readlines()]
        
        anyEqualityFound = False
        for value in aDictionary:
            if(str_text.find(value) != 1):
                print(value)
                anyEqualityFound = True
                break

        return anyEqualityFound # return True or False
        


