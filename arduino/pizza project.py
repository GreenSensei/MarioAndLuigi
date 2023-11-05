
import time, sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
board = CustomTelemetrix()
button_pressed = 0
button_pressed_2 = 0
button_state = False
button_state_2 = False
previous = 0 
number = 3

def setup():
    
    board.set_pin_mode_digital_input_pullup(9)
    board.set_pin_mode_digital_input_pullup(8)
    board.set_pin_mode_digital_output(3)
    time.sleep(0.1)
    # Put your code here.

def loop():
    # Put your code here.
    global number
    global button_pressed
    global button_pressed_2
    global button_state
    global button_state_2
    global previous
    if number != 0:
        number -= 1

    time.sleep(1)
    ordernumber = 12
    button_press = board.digital_read(8)
    button_press_2 = board.digital_read(9)
 

    if previous == button_press[0]:
        button_state = True
    else:
        button_state = False

    if number == 0:
        board.analog_write(3, 20)
        
    if previous == button_press_2[0]:
        button_state_2 = False
    else:
        button_state_2 = True

    if number == 0 and button_state_2 == 1:
        board.analog_write(3, 0)
        
    if  button_state_2:
        if button_press_2[0] == 0:
            button_pressed_2 += 1
    
    if button_pressed_2 > 0:
         board.analog_write(3, 0)

    if not button_state:
        if button_press[0] == 0:
            button_pressed += 1

        if button_pressed >=2:
            button_pressed = 0 
            time.sleep(0.1)

    if button_pressed == 0:
        board.displayShow(number)
            
        
    elif button_pressed == 1:
        board.displayShow(ordernumber)

    print(button_pressed)
    previous = button_press[0]
    time.sleep(0.1)

    # Give Firmata some time to handle the protocol.
    
# Put your functions here.

#--------------
# main program
#--------------
setup()
while True:
    try:
        loop()

    except KeyboardInterrupt: # Shutdown Firmata on Crtl+C.
        print ('shutdown')
        board.shutdown()
        sys.exit(0)  
board.analog_write(3, 0)