





#  """BU KOMPUTER BILAN SON TOPISH OYNI"""
#              print("-+- Salom men 1, - dan 20-gacha son oyladim topolasizmi.? -+-")
#         komputer_son = random.randint(1, 20)
#          n = 0
#          while True:
#              user = int(input("Son kiriting: "))
#              n += 1
#                 if komputer_son == user:
#                     print(f"Tabriklaymiz six toptingiz urunishlar soni:{n} ")

#                     javob = input("Yana oynaysizmi.? ha/yoq: ")
#                 if javob == 'ha':
#                     continue
#                 else:
#                     print("Oyin tugadi")
#                     break
#                 elif komputer_son < user:
#             `       print("Siz yuborgan son katta ")

#                 elif komputer_son > user:
#                      print("Siz yuborgan son kichik ")



# boshi = 1
# oxiri = 20
# n = 0
# input("Siz 1,-dan 20-gacha son oylang men topaman\n Son oylab hohlagan tugmangizni bosing: ")

# while True:
#     son = random.randint(boshi, oxiri)
#     user = input(f"{son} tegmi (t), son kattami (+),  son kichikmi(-)>>> ")
#     n += 1
#     if user == "t":
#         print(f"Men topdim urunishlar soni: {n} ")
#         continue
#     elif user == "+":
#         boshi = son + 1
#         break

#     elif user == "-":
#         oxiri = son - 1

# import random as r
# sonlar = list(range(1, 11))
# print(sonlar)
# r.shuffle(sonlar)
# print(sonlar)


# """ Funksiya darsi 2-qism ! """
# def talaba(ismi, familiyasi, yoshi,):
#     talabalar = f"{ismi}, {familiyasi}, {yoshi} "
#     return talabalar

# Oqishqa_kelgan_talaba = talaba('Umid', 'Mardonov', 'yoshi 22')
# Oqishqa_kelmagan_talaba = talaba('Asil', 'Yuldoshov',  'yoshi 23')
# print(f"Oqishga kelgan talaba: {Oqishqa_kelgan_talaba} \n Oqishga kelmagan talaba: {Oqishqa_kelmagan_talaba} ")


# """ Matematik oyini """

# import random

# import os 

# def menu():
#     birinchimi = True
#     while True:
#         if birinchimi:
#             print("\n\nASSOLOMU ALAYKUM  Bu Matematik oyni dasturi\nBu dastur orqali siz oz bilimingizni sinab koroshingiz mumkun\nDastur ishga tushish uchun quydagi menudan kerakli darajani tanlab oynni boshlang")
#             tanlov = input("""\n\t\tKerakli bisimni tanlang:
#                 1.OSON,
#                 2.ORTA,
#                 3.QIYIN,
#                 4.CHIQISH, 
#             1-dan 4-gacha sizga kerakli son kiriting.
#             Kiriting>>> """)
#             birinchimi = False
#         else:
#             tanlov = input("Xato 1 va 4 sonlarni ichidagi sonlarni kiriting. ")
#         if tanlov.isdigit() and int(tanlov) in range(1, 5):
#             return int(tanlov)


# def play(daraja):
#     takror = 5
#     user_bal = 0
#     for j in range(takror):
#         amallar = random.choice(["+", "-", "*", "/"])
#         masala = None
#         javob = None
#         for son in range(daraja + 1):
#             a = random.randint(1, 10)
#             if son == 0:
#                 masala = str(a)
#                 javob = a
#             else:
#                 masala += f" {amallar} {a} "
#                 if amallar == "+":
#                     javob += a
#                 elif amallar == "-":
#                     javob -= a
#                 elif amallar == "*":
#                     javob *= a
#                 if amallar == "/":
#                     javob = round(javob / a, 2)          
#         natija = input(f"Misolni javobini yozing: {masala} = ")
#         if float(natija) == javob:
#             print(f"Javob togri!")
#             user_bal +=  1
#         else:
#             print(f"Xato, togri javob: {javob}\n")
#     print(f"Siz {takror} savoldan {user_bal}-ta togri javob topdingizmi")



# while True:
#     os.system('cls')
#     tanlov = menu()
#     if tanlov == 1:
#         print("\nHurmatli oyinchi siz menudan <<OSON>> bolimini tanladingizmi:")
#         play(daraja=1)

#     elif tanlov == 2:
#         print("\nHurmatli oyinchi siz menudan <<ORTA>> bolimini tanladingizmi:")
#         play(daraja=2)
        
#     elif tanlov == 3:
#         print("\nHurmatli oyinchi siz menudan <<QIYIN>> bolimini tanladingizmi:")
#         play(daraja=3)

#     elif tanlov == 4:
#         print("Siz oyindan chiqdingiz! ")
#         break

#     savol = input("Yana oyin oynaysizmi | ha/yoq: ")
#     if savol == "ha":
#         continue
#     else:
#         print("Oyin tugadi!")
#         break