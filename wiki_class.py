

class Wikipedia:
    
    def __init__(self):
        
        welcome = "Wikipediaga xush kelibsiz !"
        print(welcome)
        
    def wiki(self):
       
       search_txt = input("Siz nima haqida qidirmoqchisiz ? ") 
       try:
            import wikipedia           
            wikipedia.set_lang("uz")
            print (wikipedia.summary(search_txt))
       except ModuleNotFoundError:
            print("Bu modul mavjud emas !")    
       except: 
           print("Kechirasiz bunday natijani topa olmadik !")
        
        
        
        
def main():
    choice = None
    while choice != "0":
        obyekt = Wikipedia()
        print(obyekt.wiki())
        choice = input("Dastur to'xatashi uchun (0) ni bosing !\nDastur davom etishi uchun (1) ni bosing!")
        
main()