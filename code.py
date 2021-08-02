import keyboard as key
import mouse
from time import sleep

start_key = input('Клавиша запуска: ')
end_key = input('Клавиша выключения: ')
cps = int(input('CPS : '))


time_sleep = 1.8/cps 
if cps > 40:
    time_sleep = 1.4001/cps
time_sleep = float('{:.3f}'.format(time_sleep))

print(time_sleep)


while True:
    if key.is_pressed(start_key):
        mouse.double_click()
        sleep(time_sleep)


    if key.is_pressed(end_key):
        print("End")
        break

# 0.05 ~ 30 cps
# 0.075 ~ 25 cps
# 0.1 ~ 20 cps
# 0.5 ~ 4 cps
# 1 = 2 cps
