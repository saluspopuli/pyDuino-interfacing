import serial
import GUI as GUI

def init_serial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    return ser

def check_serial_data():
    while True:
        arduino_data = ser.readline().decode().strip().split("-")
        print(arduino_data)
        if arduino_data[0] != '' and arduino_data[1] != '':
            gui.move_label(arduino_data[0],arduino_data[1])

if __name__ == '__main__':

    ser = init_serial('COM9' , 9600)

    gui = GUI.GUI("Test")

    gui.root.after(20, check_serial_data())

    gui.start_gui()