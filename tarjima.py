import translators as ts

#e.g. ts.google

#e.g. ts._google.language_map



def trans():
    choice = None
    while choice != "0":
        tanla = input("Qaysi tildan tarjima qilmoqchisiz ?\nAgar inglz-o'zbek lug'ati kerak bo'lsa (1) ni bosing!\nAgar o'zbek-ingliz lug'ati kerak bo'lsa (2) ni bosing!\n>>> ")
        if tanla == "1":
            word = input("Enter the words!\n>>>")
            b = ts.google(word, from_language='en', to_language='uz')
            print(b)
        elif tanla == "2":
            soz = input("O'zbekcha so'zlar kiriting!\n>>> ")
            a = ts.google(soz, from_language='uz', to_language='en')
            print(a)
        else:
            print("notog'ri son kiritdingiz!")

        choice = input("Dastur ishlashda davom etsin (1)\nDastur to'xtasin (0)\n>>> ")
c = trans()
print(c)
