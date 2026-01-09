import serial
import threading
import time

PORT = "COM1"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)

def send(message):
    try:
        ser.write((message + '\n').encode('utf-8'))
    except Exception as e:
        print(e)
    print(f"sent : {message}")

def receive():
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"received : {data}")
            return data

def received_continuous():
    while running:
        received_data = receive()
        time.sleep(0.1)

running = True
receiver_thread = threading.Thread(target=received_continuous, daemon=True)
receiver_thread.start()

try:
    while True:
        message = input("Enter your message : ")
        if message:
            send(message)

except KeyboardInterrupt:
    print("exit")

finally:
    running = False
    ser.close()