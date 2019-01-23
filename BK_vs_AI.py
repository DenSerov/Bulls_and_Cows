import random
import time

def ai_generate_number(l): #Сгеренировать число длиной l без повторяющихся цифр, за комрьютер(!)
#    s=list()
    s=''
    i=0
    while i<l:
        n=random.randint(0,9)
        #print("Сгенерирована цифра",n)
        c=str(n)
        if c not in s:
            i+=1
            s=s+str(c)
            #print("Цифра принята на позицию ",i)
            #s.append(c)
            #print("Число",s)
            #print("Длина",len(s))
    return s

def ai_byki(computer_string, human_string): # посчитать быков. Игра за  компьютер(!)
    b=0
    for j in range(len(computer_string)):
        if computer_string[j]==human_string[j]: b+=1
    return b

def ai_korovy(computer_string, human_string): # посчитать коров. Игра за  за компьютер(!)
    k=0
    for j in range(len(human_string)):
        if human_string[j] in computer_string: k+=1
    return k

def valid_number(human_string):
    validity=True
    count=0
    if human_string=='':
        print("Введите 4 неповторяющихся цифры от 0 до 9.")
        return False
    if len(human_string)>4:
        print("Вы ввели больше 4х символов. Введите 4 неповторяющихся цифры от 0 до 9.")
        return False
    if len(human_string)<4:
        print("Вы ввели меньше 4х символов. Введите 4 неповторяющихся цифры от 0 до 9.")
        return False
    for c in human_string:
        for i in range(len(human_string)):
            if c==human_string[i]: count+=1
    if count==4: validity=True
    else:
        print("Вы ввели повторяющиеся символы. Введите 4 неповторяющихся цифры от 0 до 9.")
        validity=False
    return validity

def ai_ask_number(computer_string):  # спросить у человека число. Игра за компьютер(!)
    human_string=''
    #len(human_string)!=4 or
    while not valid_number(human_string):
        human_string=input("Ввод> ")
#    valid_number(human_string)

    b=ai_byki(computer_string, human_string)
    k=ai_korovy(computer_string, human_string)
    k-=b
    print(b, "быков",k,"коров.")
    if b==4:
        return True
    else:
        return False
    return

def  ai_congratulation_for_human(attempts):
    i=attempts
    if i==0: congrat_string="ПО-МОЕМУ, ВЫ ЯСНОВИДЯЩИЙ!"
    elif i<=5: congrat_string="ПО-МОЕМУ, ВЫ ГЕНИЙ БЫКОВ И КОРОВ!"
    elif i<=6: congrat_string="ПО-МОЕМУ, ДОВОЛЬНО НЕПЛОХО!"
    elif i<=8: congrat_string="ПО-МОЕМУ, ВЫ ХОРОШО ИГРАЕТЕ!"
    elif i<=8: congrat_string="ПО-МОЕМУ, У ВАС ЕСТЬ МОЗГИ!"
    elif i<=10: congrat_string="НЕПЛОХО ДЛЯ НАЧАЛА!"
    return congrat_string


def ai_generate_all(): #сгенерировать все пространство чисел для угадывания человечекого числа
    numbers=list()
    m=0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                    for l in range(10):
                        if not (i==j or i==k or i==l or j==k or l==k or j==l):
                            s=str(i)+str(j)+str(k)+str(l)
                            numbers.append(s)
                            m+=1
                            #print(s,end=' ')
#    print('\n',m)
    return numbers

def ai_resheto(guess_list,guess,b,k,dificulty):
    OK=False
    numbers=list()
    bi=int(b)
    ki=int(k)
    bb=0
    kk=0
    if b=='0' and k=='0':
            for i in range(len(guess_list)):
#                time.sleep(0.001)
                OK=True
                for j in range(len(guess)):
                    if guess[j] in guess_list[i]:
                         OK=False
                         break
                if OK: numbers.append(guess_list[i])
            return numbers

    for i in range(len(guess_list)):          #проходим по всему списку чисел
        #time.sleep(0.001)
        OK=True
        kk=0
        bb=0
        for j in range(len(guess)):           #проход по цифрам названного числа
            if (guess[j] in guess_list[i]):   #если цифра есть в числе из списка, но не в том же месте!
                kk+=1                         #увеличиваем к-во коров
        for j in range(len(guess)):           # найти числа из списка угадывания где нужное количество цифр из данной попытки стоят на тех же местах
            if guess[j]==guess_list[i][j]:
                bb+=1
                #print(guess,guess_list[i],bb,kk)
        kk-=bb
        if kk!=ki: OK=False         #если к-во коров не равно тому, что на входе - отбрасываем это число
        if bb!=bi: OK=False
        if bi<3 and random.randint(0,19)>(11+dificulty): OK=True #Решето делаем крупнее, если сложность не самая высокая
        if OK: numbers.append(guess_list[i])  #остаются только числа с заданным числом коров и быков
    return numbers

def report(attempts_list,b_hist,k_hist,size_hist):
    for i in range(len(attempts_list)):
        print("Попытка:", i+1, "| Число:", attempts_list[i],"| Быков: ",b_hist[i],"| Коров: ",k_hist[i],"| Размер списка: ",size_hist[i])
    return

def initial(used_digits):
    gstr=''
#    print(used_digits)
    while len(gstr)<4:
        ch=str(random.randint(0,9))
#        print(ch, type(ch),type(gstr),type(used_digits))
        if (ch not in gstr) and (ch not in used_digits):
            gstr=gstr+ch
            used_digits=used_digits+ch

#    print("used_digits",used_digits)
#    print("g",gstr)
    return gstr

def single_game(dificulty):

    b=0
    k=0
    j=0
    used_digits=''
    win=False
    human_win=False
    guess_list=ai_generate_all()
    attempts_list=list()
    b_hist=list()
    k_hist=list()
    size_hist=list()

    computer_string=ai_generate_number(4)
    print("Я загадала в уме в 4х-значное число ;)")
    input("Загадайте тоже 4х-значное число и нажмите ENTER для начала игры>")

    while not win:
            j+=1 # номер хода

            """
                ХОД ЧЕЛОВЕКА
            """
            human_win=ai_ask_number(computer_string)
            retry=True
            if human_win:
                print("Я действительно загадал число", computer_string)
                print("Ты угадал с",j,"-й попытки!!!")
                print(ai_congratulation_for_human(j))
                retry=False

            """
               КОНЕЦ ХОДА ЧЕЛОВЕКА

               НАЧАЛО ХОДА КОМПЬЮТЕРА
            """
            size_hist.append(len(guess_list))
            if len(guess_list)==1:
                print()
                print("Вы загадали",guess_list[0],"!!!")
                print("А у меня было число", computer_string,"\n")
                print()
                report(attempts_list,b_hist,k_hist,size_hist)
                win=True
                retry=False
                break


            if len(guess_list)==0:
                print(":'-( Что-то я запуталась. Давай все сначала, а?")
                print("У меня было число", computer_string)
                break
            i=0

            while retry: #ВЫБОР ЧИСЛА ИЗ СПИСКА РАНЕЕ НЕ ИСПОЛЬЗОВАВШИХСЯ
                print("Вариантов",len(guess_list))
                if j<3 and dificulty==9:
                    guess=initial(used_digits)
                    used_digits=used_digits+guess
                    retry=False
                elif j==3 and len(guess_list)>160 and dificulty==9:
                    used_digits=used_digits[2:]
                    guess=initial(used_digits)
                    used_digits=used_digits+guess
                    retry=False
                else:
                    i=random.randint(0,len(guess_list)-1)
                    if guess_list[i] not in attempts_list:
                        retry=False
                        guess=guess_list[i]
                attempts_list.append(guess)

            print("Попытка",j,". Число",guess,"?")




            valid_input=False
            while not valid_input:
                bkstr=input("Быков-коров > ")
                b=0
                k=0
                try:
                    b=int(bkstr.split('-')[0])
                    k=int(bkstr.split('-')[1])
                except: pass

                bk=b+k
                if b>=0 and k>=0 and bk<=4 and len(bkstr)==3:
                    valid_input=True
                else:
                    print("Пожалуйста, введите еще раз. Например, 1 бык и 2 коровы: 1-2.")

            b_hist.append(b)
            k_hist.append(k)
            #print(b,k,"быков/коров принято для попытки", guess)
            guess_list=ai_resheto(guess_list,guess,b,k,dificulty)
    return


#начало основного тела программы
user=0

while True: #бесконечный цикл
    dificulty=0
    try: user=int(input("Давай играть в Быков и Коров! [1 - да, 2 - нет]: "))
    except: pass
    if user==1:
        try:
            dificulty=6+int(input("Выбери сложность [1-3]: "))
            if dificulty>9: dificulty=9
            if dificulty<0: dificulty=0
        except: pass
        used_digits=''
        single_game(dificulty)

    elif user==2:
        print("Ну ладно! Тогда до свидания!")
        break
    user=0
