import random
random_number= random.randint(1,10)
a = print("Менің ойымдағы санды табыңыз. Ол сан 1-10 арасында")
flag = True
while flag:
    a = False
    a = int(input())
    if a == random_number:
        print("Мәссаған! Мықты екенсіз! ")
        flag = False
        print("Тағыда ойнаймыз ба?! ")
    elif a < random_number:
            print("Менің саным бұдан үлкенірек! ")
    elif a > random_number:
            print("Менің саным бұдан кішігірек!")









#import random
#random_number = random.randint(1,10)
#play = True
#while play:
#    b = play
#    b = exit
#print("Угадай Мое Число")
#flag = True
#while flag:
#    a = int(input())
#    if a == random_number:
#        print("Ниче Се! Ты угадал мое Чило")
#        flag = False
#        print("Давай еще Раз!")
#    elif a < random_number:
#            print("Твое Число чуть Меньше")
#    elif a > random_number:
#            print("Твое Число чуть Больше")
    
    