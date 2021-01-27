list=[]
names=[]
temp_names=[]
phoneNo=''
dob=input("Дата рождения(DDMMYYYY):")
if(len(dob)==8):
    day=dob[:2]
    month=dob[2:4]
    year=dob[4:]
else:
    print("Неверный формат, убедитесь, что это 8 цифр в DDMMYYYY")
    exit()

phoneNo=input("Введите номер телефона:")

def ListOfImportantWords():
    names.append(input("Имя:"))
    names.append(input("Фамилия:"))
    names.append(input("Никнейм:"))
    print("\n")
    names.append(input("Имя партнёра:"))
    names.append(input("Никнейм партнёра:"))
    print("\n")
    names.append(input("Имя домашнего животного:"))
    names.append(input("Наименование компании:"))
    print("\n")
    names.append(input("Имя ребенка:"))
    names.append(input("Никнейм ребенка:"))
    print("\n")
    names.append(input("Город:"))
    names.append(input("Страна:"))
    names.append(input("Любимый цвет:"))
    print("Введите все остальные ключевые слова: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while('' in names) : 
        names.remove('') 

def permute(inp): 
    n = len(inp) 
   
    mx = 1 << n 
   
    inp = inp.lower() 
      
    for i in range(mx): 
        combination = [k for k in inp] 
        for j in range(n): 
            if (((i >> j) & 1) == 1): 
                combination[j] = inp[j].upper() 
   
        temp = "" 
        for i in combination: 
            temp += i 
        temp_names.append(temp) 



def WordListCreator(list):
    for word in names:
        for i in range(0,len(word)+1):
            list.append(word[:i]+day+word[i:])
            list.append(word[:i]+month+word[i:])
            list.append(word[:i]+year+word[i:])
            if len(year)==4:
                list.append(word[:i]+year[2:]+word[i:])
            list.append(word[:i]+phoneNo+word[i:])
    if not phoneNo=='':
        list.append(phoneNo)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)



ListOfImportantWords()
for i in names:
    permute(i)       
names=names+temp_names
WordListCreator(list)
WriteToFile(list)

