from random import *


def new_field():
    field = [['_' for j in range(3)] for i in range(3)]
    return field


def print_field(field):
    text = ''
    for i in range(len(field)):
        text += '\n'+' | '.join(field[i])
        # print(' | '.join(field[i]))
    return text

# определяем игрока и чем ходит


def set_players(human):
    hod = choice([True, False])  # определили рандомно 1го игрока
    # буду считать по ходу программы, что True - это бот, False - человек
    dic = {}
    dic[hod] = ['x']  # и добавили это значение в словарь
    dic[not hod] = ['0']
    if hod == True:
        dic[hod].append('bot')
        dic[not hod].append(human)
    else:
        dic[hod].append(human)
        dic[not hod].append('bot')

    print(dic)
    return (dic, dic[hod][1], hod)


def check_win(field, elem_go):
    # проверяем по строкам
    for el in field:
        if el.count(elem_go) == 3:
            return True
# здесь я тренируюсь транспонировать вложенный список ускоренными методами)
    # col_in_row = list(map(list, zip(*field)))
    col_in_row = [[field[j][i]
                   for j in range(len(field))] for i in range(len(field[0]))]
# проверяем по столбцаи   
    for el in col_in_row:
        if el.count(elem_go) == 3:
            return True
# проверяем главную диагональ
    find_el = 0
    for i in range(3): 
        if field[i][i] == elem_go: find_el+=1
    if find_el == 3: return True
# проверяем диагональ
    if field[2][0] == elem_go and field[1][1] == elem_go and field[0][2] == elem_go:
        return True

# сначала смотрим выигрышный ход, потом проигрышный закрыть, потом центр, потом рандом из свободных
def ch_field(field, bot_el,other_el):
    if bot_hod(field, bot_el,other_el) != None:
        pl = bot_hod(field, bot_el,other_el)
    elif  field[1][1] == '_':
        pl = (1, 1)  
    else:     
        _pos = [(index1,index2) for index1,value1 in enumerate(field) for index2,value2 in enumerate(value1) if value2=='_']
        # print(_pos)
        pl = choice(_pos)
    # print('оптимальный ход бота:', pl)
    return pl      

# проверяем возможность хода в принципе
def none_hod(field):
    none_hod = False
    _pos = [(index1,index2) for index1,value1 in enumerate(field) for index2,value2 in enumerate(value1) if value2=='_']
    if _pos == None:
        none_hod = True
    
    return none_hod
    
# проверка на умный ход, где уже есть макс.число эл-та бота, иначе если нет
# лучше закрывать ход соперника, а потом можно рандом из пустой строки, столбца
# field = [['_','_','_'],['_','_','_'],['_','_','_']]
def bot_hod(field, bot_el,other_el):
#сначала проверяем выигрышную позиции с эл-том бота 
        # проверяем по строкам
    for el in field:
        if el.count(bot_el) == 2 and '_' in el:
            pos = (field.index(el), el.index('_'))
            return pos

    col_in_row = list(map(list, zip(*field)))   
    # print(col_in_row)
    # проверяем по столбцаи   
    for el in col_in_row:
        if el.count(bot_el) == 2 and '_' in el:
            # возвращаем э-ты наоборот,т.к. список транспонирован
            pos = (el.index('_'), col_in_row.index(el))
            return pos
# проверяем главную диагональ
    if field[0][0] == field[1][1]== bot_el and field[2][2] == '_':
        return (2,2)
    if field[0][0] == field[2][2]== bot_el and field[1][1] == '_':
        return (1,1)
    if field[2][2] == field[1][1]== bot_el and field[0][0] == '_':
        return (0,0)
# проверяем диагональ
    if field[2][0] == field[1][1]== bot_el and field[0][2] == '_':
        return (0,2)
    if field[2][0] == field[0][2]== bot_el and field[1][1] == '_':
        return (1,1)
    if field[1][1] == field[0][2]== bot_el and field[2][0] == '_':
        return (2,0)
# теперь проверяем проигрышную позицию
        # проверяем по строкам
    for el in field:
        if el.count(other_el) == 2 and '_' in el:
            pos = (field.index(el), el.index('_'))
            return pos

    col_in_row = list(map(list, zip(*field)))   
    # print(col_in_row)
    # проверяем по столбцаи   
    for el in col_in_row:
        if el.count(other_el) == 2 and '_' in el:
            # возвращаем э-ты наоборот,т.к. список транспонирован
            pos = (el.index('_'), col_in_row.index(el))
            return pos
# проверяем главную диагональ
    if field[0][0] == field[1][1]== other_el and field[2][2] == '_':
        return (2,2)
    if field[0][0] == field[2][2]== other_el and field[1][1] == '_':
        return (1,1)
    if field[2][2] == field[1][1]== other_el and field[0][0] == '_':
        return (0,0)
# проверяем диагональ
    if field[2][0] == field[1][1]== other_el and field[0][2] == '_':
        return (0,2)
    if field[2][0] == field[0][2]== other_el and field[1][1] == '_':
        return (1,1)
    if field[1][1] == field[0][2]== other_el and field[2][0] == '_':
        return (2,0)


# print(bot_hod(field,'0','x'))       #это было для проверки     
