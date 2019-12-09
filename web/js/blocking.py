from time import sleep

def sleep_3s():
    sleep(3)
    print('Wack up!')
print('start sleeping')
sleep_3s() #얘가 blocking 기능을 한다
print('end of program')