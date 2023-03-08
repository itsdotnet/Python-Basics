# darsda tashlab berilgan misollarni avval ishlamaganlarimiz:

# 1 (6) kalendar

# from calendar import *
# data = list(map(int,input().split("-")))
# a = month(data[1],data[0])
# a = a.split('\n')[1::]
# a[0] = "Du Se Ch Pa Ju Sh Ya"
# for i in a:
#     print(i)
    
# 2 (5) zodiac 

# try:
#     from datetime import *
#     a = list(map(int,input().split('"')[1].split('.')))
#     a = datetime(a[-1],a[1],a[0])
#     day,month = a.day,a.month
#     if month == 12:
#         sign = "O'qotar" if (day < 22) else "Tog' echkisi"
#     elif month == 1:
#         sign = "Tog' echkisi" if (day < 20) else "Qovg'a"
#     elif month == 2:
#         sign = "Qovg'a" if (day < 19) else 'Baliq'
#     elif month == 3:
#         sign = 'Baliq' if (day < 21) else "Qo'y"
#     elif month == 4:
#         sign = "Qo'y" if (day < 20) else 'Buzoq'
#     elif month == 5:
#         sign = 'Buzoq' if (day < 21) else 'Egizaklar'
#     elif month == 6:
#         sign = 'Egizaklar' if (day < 21) else 'Qisqichbaqa'
#     elif month == 7:
#         sign = 'Qisqichbaqa' if (day < 23) else 'Arslon'
#     elif month == 8:
#         sign = 'Arslon' if (day < 23) else 'Parizod'
#     elif month == 9:
#         sign = 'Parizod' if (day < 23) else 'Tarozi'
#     elif month == 10:
#         sign = 'Tarozi' if (day < 23) else 'Chayon'
#     elif month == 11:
#         sign = 'Chayon' if (day < 22) else "O'qotar"
#     print(sign)
# except:
#     print("Ma'lumot kiritishda hatolik !")

