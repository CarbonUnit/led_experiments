from gpiozero import LED, Button
from time import sleep

#timeout in sec
LED_TIMEOUT_S = 0.5

#index of LED
led_list = [ 0,1 ,2 ,3 ,4 ]

#GPIO Pin used (mapped to index above)
pin_list = [ 4,17,27,22,23 ]

#Make a list of the LED index and LED pins as a dictionary
master_list = []
for i in range(0,5):
    temp_dict = {}
    temp_dict['led']      = led_list[i]
    temp_dict['pin']      = pin_list[i] 
    #Create an instance of the LED class with the given LED pin number
    temp_dict['led_inst'] = LED( temp_dict['pin'] )

    #Append the dictionary created above to the master_list of dictionaries
    master_list.append( temp_dict )

for each in master_list:
    print each


i = 0
while True:
    print( 'i = {item}'.format( item = i ) )

    #Turn off all the LEDs
    for led in master_list:
        print( 'led{} is lit?  {}'.format( led['led'], led['led_inst'].is_lit))
        led['led_inst'].off()

    #Turn on only the LED we want on, during this loop iteration
    master_list[ i ]['led_inst'].on() 


    sleep( LED_TIMEOUT_S )
    i = i+1
    if i > 4:
        i=0

     

      
    
