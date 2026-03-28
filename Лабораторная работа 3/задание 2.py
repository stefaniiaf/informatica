# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=","):  #создаем функцию с тремя аргументами
    first = participants_first_group.split(delimiter) #разбиваем строку первой группы на отдельные элементы(фамилии) и сохраняем в переменную
    second = participants_second_group.split(delimiter) #аналогично предыдущей строке только со второй группой
    participants = []                                   #создаем пустой список для элементов которые есть и впервой и во второй группе
    for participant in first:                           #запускаем цикл for для перебора элементов в первой  группе
        if participant in second:                       #если те же элементы есть и во второй группе
            participants.append(participant)            #добавляем с помощью append в наш список
    participants.sort()                                 #Сортируем элементы (фамилии) по алфавиту
    return participants                                 #возвращаем готовый список из общих элементов




# TODO Провеьте работу функции с разделителем отличным от запятой

groups = "Иванов|Петров|Сидоров"
groupt = "Петров|Сидоров|Смирнов"
h = find_common_participants(groups, groupt, "|") #тестируем функцию
print(h)