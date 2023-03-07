# 1
# a = input().split()
# ls = []
# ls.append([''])
# ls.append([a[0]])
# ls.append([a[1]])
# ls.append([a[2]])
# ls.append([a[0],a[1]])
# ls.append([a[0],a[2]])
# ls.append([a[1],a[2]])
# ls.append([a[0],a[1],a[2]])
# print(ls)


# 2
# a = ["a","e","i","o","u","l","n","s","t","r"]
# b = ["d","g"]
# c = ["b","c","m","p"]
# d = ["f","h","w","v","y"]
# e = ["k"]
# f = ["j","x"]
# j = ["q","z"]
# st = input()
# ball = 0
# for i in st:
#     i = i.lower()
#     if i in a:
#         ball += 1
#     elif i in b:
#         ball += 2 
#     elif i in c:
#         ball += 3 
#     elif i in d:
#         ball += 4 
#     elif i in e:
#         ball += 5 
#     elif i in f:
#         ball += 8 
#     elif i in j:
#         ball += 10
# print(ball)


# 3
# dub_list = []
# l = list(input())
# for i in range(len(l)):
#     if l[i] in dub_list:
#         dub_list.append(l[i])
#         l[i] = f'{l[i]}_{dub_list.count(l[i])-1}'
#     else:
#         dub_list.append(l[i])
# print(*l)


# 4

# shu fayl bolishi kerak !!!

# words = open('forbidden_words.txt')
# words = words.read().split()
# st = input()
# num_up = []
# for i in range(len(st)):
#     if st[i].isupper():
#         num_up.append(i)
# st = st.lower()
# for i in words:
#     if i in st:
#         st = st.replace(i,'*'*len(i))
# for i in range(len(st)):
#     if st[i]=='*' and i in num_up:
#         num_up.remove(i) 
# for i in num_up:
#     st = st.replace(st[i],st[i].upper())
# print(st)


# 5

# from mysql import connector
# baza = connector.connect(
#     user = "root"
#     password = ""
# )
# baza.cursor()

# 6
# def hisobla(st: str,):
#     lst = st.split('.')
#     k = int(lst[0])*256**3 + int(lst[1])*256**2 + int(lst[2])*256 + int(lst[3])
#     return k

# N = int(input())
# dic = {}
# for i in range(N):
#     a = input()
#     dic.update({hisobla(a):a})
# new = list(dic)
# print(new)

# new.sort()
# for i in new:
#     print(dic[i])