import RPi.GPIO as GPIO
import time
import threading

PUL = 17
DIR = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR, GPIO.OUT, initial=GPIO.LOW)

STEPS_PER_REV = 200 * 32   # 200 шагов * 1/32 (поставила на драйвере)
MIN_RPM = 0
MAX_RPM = 150


def read_speed():
    global rpm
    while True:
        text = input("Новая скорость (об/мин): ")
        try:
            val = float(text)
        except ValueError:
            print("Нужно число")
            continue
        rpm = max(MIN_RPM, min(MAX_RPM, val))
        print(f"Скорость: {rpm} об/мин")

rpm = 0
threading.Thread(target=read_speed, daemon=True).start()

GPIO.output(DIR, GPIO.HIGH)
time.sleep(0.01)

try:
    while True:
        delay = 60 / (rpm * STEPS_PER_REV) / 2
        GPIO.output(PUL, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        time.sleep(delay)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
