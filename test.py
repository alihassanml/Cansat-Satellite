import serial

ser = serial.Serial('COM7', 115200)

while True:
    try:
        data = ser.readline().decode().strip()
        print(data)

    except ValueError:
        print("Error: Received invalid data")

ser.close()

