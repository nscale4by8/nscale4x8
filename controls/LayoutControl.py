from gpiozero import LED
from time import sleep
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

turnoutLetterToPointsID = {
   "A" : 0,
   "YA" : 1,
   "B" : 2,
   "C" : 3,
   "D" : 4,
   "E" : 5,
   "F" : 6,
   "G" : 7,
   "YBC" : 8,
   "H" : 9,
   "I" : 10,
   "J" : 11,
   "K" : 12,
   "L" : 13,
}

class TestModeA:
   def __init__(self):
      pass
     
   def enter(self, control):
      state = True
      i = 0
      while i < len(turnoutLetterToPointsID):
         print(i)
         control.setPoints(i, state)
         sleep(0.25)
         control.setPoints(i, not state)
         i += 1
         char = raw_input("next: ")
         print(char)
         if char.startswith("b"):
            i -= 1
            state = not state
            print(state)
         
class TestModeB:
   def __init__(self):
      pass
     
   def enter(self, control):
      control.setPoints(0, False)
      control.setPoints(1, False)
      control.setPoints(2, False)
      control.setPoints(3, False)
      control.setPoints(4, False)
      control.setPoints(5, False)
      control.setPoints(6, False)
      control.setPoints(7, False)
      control.setPoints(8, False)
      control.setPoints(9, False)
      control.setPoints(10, False)
      control.setPoints(11, False)
      control.setPoints(12, False)
      control.setPoints(13, False)
      control.setPoints(0, True)
      control.setPoints(1, True)
      control.setPoints(2, True)
      control.setPoints(3, True)
      control.setPoints(4, True)
      control.setPoints(5, True)
      control.setPoints(6, True)
      control.setPoints(7, True)
      control.setPoints(8, True)
      control.setPoints(9, True)
      control.setPoints(10, True)
      control.setPoints(11, True)
      control.setPoints(12, True)
      control.setPoints(13, True)

class DoubleMainMode:
   def __init__(self):
      pass
      
   def enter(self, control):
      control.setPoints(1, False)
      control.setPoints(2, False)
      control.setPoints(3, True)
      control.setPoints(8, True)
      control.setPoints(9, False)
      control.setPoints(10, False)
      control.setPoints(11, False)
            
class TwistedDogboneMode:
   def __init__(self):
      pass
      
   def enter(self, control):
      control.setPoints(8, False)
      control.setPoints(4, True)
      control.setPoints(7, False)
      control.setPoints(5, False)
      control.setPoints(10, False)
      control.setPoints(11, True)
      control.setPoints(2, False)
      control.setPoints(1, True)
      control.setPoints(15, True)
      
class LayoutControl:
   MotorHatI2C_ID = 0x6f
   motorHats = {}
   gpioPinSequence = (17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 23, 24, 25, 8, 7, 16)
   gpioPins = {}
   
   @staticmethod 
   def turnOffMotors():
      for id in  LayoutControl.motorHats:
         motorHat = LayoutControl.motorHats[id]
         for motorID in range(1, 5):
            motorHat.getMotor(motorID).setSpeed(0)
            motorHat.getMotor(motorID).run(Adafruit_MotorHAT.RELEASE)
   
   def initMotorHats(self):
      hat = Adafruit_MotorHAT(addr=LayoutControl.MotorHatI2C_ID)
      for motorID in range(1, 5):
         hat.getMotor(motorID).setSpeed(0)
      LayoutControl.motorHats[LayoutControl.MotorHatI2C_ID] = hat
   
   def initRelays(self):
      for gpioPin in LayoutControl.gpioPinSequence:
         LayoutControl.gpioPins[gpioPin] = LED(gpioPin)
         LayoutControl.gpioPins[gpioPin].on(); '''means off because active-low'''

   def __init__(self):
      self.initRelays()
      self.initMotorHats()

   def setPoints(self, pointsID, state):
      pinNumber = LayoutControl.gpioPinSequence[pointsID]
      motorHat = LayoutControl.motorHats[LayoutControl.MotorHatI2C_ID]
      motor = motorHat.getMotor(3)
      if state:
         motor.setSpeed(0)
         motor.run(Adafruit_MotorHAT.FORWARD);
         motor.setSpeed(255)
      else:
         motor.setSpeed(0)
         motor.run(Adafruit_MotorHAT.BACKWARD);
         motor.setSpeed(255)
         
      gpioPinNumber = LayoutControl.gpioPinSequence[pointsID]
      gpioPin = LayoutControl.gpioPins[gpioPinNumber]
      gpioPin.off(); # means on because active-low
      sleep(0.2)  # Don't leave relay on very long to avoid damaging solonoid
      gpioPin.on(); # means off because active-low'''
      motor.setSpeed(0)

   def setMode(self, mode):
      mode.enter(self)

# Auto-disable motors on shutdown!
atexit.register(LayoutControl.turnOffMotors)

   
control = LayoutControl()
testMode = TestModeA()
#mode = DoubleMainMode()
mode = TwistedDogboneMode()
lastMode = mode
control.setMode(mode)

def changeSpeedBy(delta):
   global speed
   global lastSpeedDelta
   speed += delta
   lastSpeedDelta = delta
   if speed > 250:
      speed = 250
   elif 0 < delta and speed < 100:
      speed = 100
      
   if speed < 0:
      speed = 0

speed = 0
lastSpeedDelta = 10
direction = Adafruit_MotorHAT.FORWARD
otherDirection = Adafruit_MotorHAT.BACKWARD
motorHat = LayoutControl.motorHats[LayoutControl.MotorHatI2C_ID]
motor1 = motorHat.getMotor(1)
motor1.run(direction);
motor1.setSpeed(0)
motor2 = motorHat.getMotor(4)
motor2.run(direction);
motor2.setSpeed(0)
motor3 = motorHat.getMotor(2)
motor3.run(direction);
motor3.setSpeed(0)

print("""
   q: Quit
   w: Increase speed
   s: Decrease speed
   r: Set speed to 0 and reverse
   f: Set speed to 0 and forward
   t: Test mode
""")


print("Speed: {} {}".format(speed, 
   "Forward" if direction == Adafruit_MotorHAT.FORWARD else "Backward"))
while True:
   choice = raw_input("Throttle:")
   if choice.startswith("q"):
      break
   elif choice.startswith("w"):
      changeSpeedBy(10)
   elif choice.startswith("s"):
      changeSpeedBy(-10)
   elif choice.startswith("r"):
      speed = 0
      direction = Adafruit_MotorHAT.BACKWARD
      otherDirection = Adafruit_MotorHAT.FORWARD
   elif choice.startswith("f"):
      speed = 0
      direction = Adafruit_MotorHAT.FORWARD
      otherDirection = Adafruit_MotorHAT.BACKWARD
   elif choice.startswith("t"):      
      control.setMode(testMode)
      control.setMode(lastMode)
   elif "" == choice.strip():
      changeSpeedBy(lastSpeedDelta)
      
   motor1.run(otherDirection);
   motor1.setSpeed(speed)
   motor2.run(direction);
   motor2.setSpeed(speed)
   motor3.run(direction);
   motor3.setSpeed(speed)
   print("Speed: {} {}".format(speed, 
      "Forward" if direction == Adafruit_MotorHAT.FORWARD else "Backward"))
