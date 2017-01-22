from gpiozero import LED, Button
from time import sleep

#led = LED(17)
#button = Button(2)

led_list = [ 0,1 ,2 ,3 ,4 ]
pin_list = [ 4,17,27,22,23 ]

master_list = []
for i in range(0,5):
    temp_dict = {}
    temp_dict['led']      = led_list[i]
    temp_dict['pin']      = pin_list[i] 
    temp_dict['led_inst'] = LED( temp_dict['pin'] )

    master_list.append( temp_dict )

for each in master_list:
    print each


'''
i = 0
while True:
    led.on()
    print('turned on LED')
    sleep(1)
    led.off()
    print('turned off LED')
    sleep(1)

    i = i+1
    print( 'i = %s' % i )
    print( 'i = {}'.format( i ) )
    if i > 15:
        i=0
'''    

     

      
    
