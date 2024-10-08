import random

# Класс "Игрок"
class Playr:
    def __init__(self, typ_p, name_p):
        # Тип игрока : True - компьютер
        self.typ_p = typ_p
        self.name_p = name_p

# Класс "Мешок с бочонками"
class Mbchnk:
    def __init__(self):
        self.masb = [i for i in range(1, 91)]

    # Возврат очередного бочонка (числа)
    # Нужно выдавать неповторяющиеся числа (бочонки)
    # И следить за тем чтобы мешок не исчерпался
    # Когда мешок пустой - выдается -1

    def oshbsh(self):
        my_list = [i for i in self.masb if i > 0]
        if len(my_list) == 0:
            return(-1)
        else:
            nompoz = random.randint(0, len(my_list) - 1) #
            znb = my_list[nompoz]
            self.masb = [-1 if i == znb else i for i in self.masb]
            return(znb)

# Класс "Карточка"
class Kart:
    # Сгенерировать карточку
    # В карточке генерируем неповторяющиеся числа
    # Для этого создаем класс "мешок" и вычерпываем из него 3 строки по 9 клеток
    def __init__(self, playr, vspb):
        self.name_k = playr.name_p
        tkart = []
        for i in range(1, 4):
            skart = []
            for j in range(1, 10):
                skart.append(vspb.oshbsh())
            tkart.append(skart)
        self.tkart = tkart

    # Зачеркнуть число
    # Ищем это число в карточке
    # Если оно найдено то возвращаем True
    # Если не найдено, то возвращаем False
    def zaccg(self, zch):
        for i in range(0, 3):
            for j in range(0, 9):
                zng = self.tkart[i][j]
                if zch == zng:
                    self.tkart[i][j] = - zng
                    return True
        return False

    # Функция "Карточка закрыта полностью ?"

    def krt_is_clouse(self):
        for i in range(0, 3):
            for j in range(0, 9):
                zng = self.tkart[i][j]
                if zng > 0:
                    return False
        return True

    # Выдать данные для печати карточки
    def prntk(self):
        lstvd = []
        lstvd.append('')
        dls = 0
        for i in range(0, 3):
            sttek = ''
            for j in range(0, 9):
                zng = self.tkart[i][j]
                pchv = ' ' + str(abs(zng)) if abs(zng) < 10 else str(abs(zng))
                pchz = ' ' + pchv + ' ' if zng > 0 else '-' + pchv + '-'
                sttek = sttek + pchz + '|'
                dls = len(sttek)
            lstvd.append(sttek)

        lstvd.append('-' * dls)
        pervst = '- ' + self.name_k + ' ------'
        lstvd[0] = pervst + '-' * (dls - len(pervst))

        return(lstvd)

def psostkrt(igrok1, igrok2): # Печать состояния карточек
    k1 = igrok1.prntk()
    k2 = igrok2.prntk()
    for i in range(0, 5):
        print(k1[i] + '    ' + k2[i])

def qw_homo(plr, krt): # Вопросы человеку через консоль и обработка ответов

    deplz = input(plr.name_p + ' - зачеркнуть число ' + str(tekch) + ' да\нет\стоп : ')  # Зададим вопрос зачеркнуть или не зачеркивать

    if deplz == 'да':
        if not krt.zaccg(tekch):
            return(plr.name_p + ' проиграл. Он попытался зачеркнуть число, которого нет в карточке.')
    elif deplz == 'нет':
        if krt.zaccg(tekch):
            return(plr.name_p + ' проиграл. Он не зачеркнул число, которое есть в карточке.')
    else:
        return('Выполнение программы прервано пользователем.')

    return('')

# Основной блок

vspb1 = Mbchnk()    # вспомогательный мешок для генерации карточки первого игрока
vspb2 = Mbchnk()    # Вспомогательный мешок для генерации карточки второго игрока
Mbchnk = Mbchnk()   # Основной мешок для игры

print('1. Человек / компьютер')
print('2. Человек / человек')
print('3. Компьютер / компьютер')
print('4. Выход')
regr = input('Выберите режим игры : ')

flprod = True
if regr == '1':
    playr1 = Playr(False, "Человек")
    playr2 = Playr(True, "Компьютер")
elif regr == '2':
    playr1 = Playr(False, "Человек 1")
    playr2 = Playr(False, "Человек 2")
elif regr == '3':
    playr1 = Playr(True, "Компьютер 1")
    playr2 = Playr(True, "Компьютер 2")
else:
    flprod = False

krt1 = Kart(playr1, vspb1)
krt2 = Kart(playr2, vspb2)
soo = ''

while flprod:
    psostkrt(krt1, krt2)    # Выведем состояния карточек

    if krt1.krt_is_clouse():
        soo = playr1.name_p + ' выиграл. Он первым закрыл все клетки в карточке.'
        break
    if krt2.krt_is_clouse():
        soo = playr2.name_p + ' выиграл. Он первым закрыл все клетки в карточке.'
        break

    tekch = Mbchnk.oshbsh() # Вытащим очередной бочонок из мешка

    if regr == '1': # Человек и компьютер
        soo = qw_homo(playr1, krt1)
        if soo != '':
            break
        krt2.zaccg(tekch)

    elif regr == '2': # Человек и человек
        soo = qw_homo(playr1, krt1)
        if soo != '':
            break
        soo = qw_homo(playr2, krt2)
        if soo != '':
            break

    elif regr == '3': # Компьютер и компьютер
        krt1.zaccg(tekch)
        krt2.zaccg(tekch)

print(soo)






