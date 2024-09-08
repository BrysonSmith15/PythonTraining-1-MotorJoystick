# simple driver input (sometimes called OI or operator interface)
from wpilib import Joystick, XboxController
# The rev vendor library. Rev Robotics sells the Spark Max Motor Controller and the Neo (and 550) Motors which we use
# CANSparkLowLevel allows us to specify the kind of motor we are controlling
# CANSparkMax is the class we will interact with the most.
from rev import CANSparkMax, CANSparkLowLevel

# Get User Input
# this Joystick will be on port 0 on the driver station
my_joystick = Joystick(0)
# to read the 0 axis (often LX, or the vertical axis of the left stick)
my_joystick.getRawAxis(0)
# this Joystick will be on port 0 on the driver station.
# It has bindings for an XboxController which is the same as our Logitech Controllers
my_joystick = XboxController(0)
# reading the joystick can be easier with an XboxController.
# The different axis are named.
my_joystick.getLeftX()
# this can be assigned to a variable to be used later
lx_value = my_joystick.getLeftX()


# Output to Spark Max
# We say CANSparkLowLevel.MotorType.kBrushless for Neo and Neo 550 motors.
# They are Brushless motors
# We say CANSparkLowLevel.MotorType.kBrushed for CIM motors. They are Brushed.
# If you do not know, ask which kind of motor.
# Providing the wrong value can damage the motor
my_spark = CANSparkMax(5, CANSparkLowLevel.MotorType.kBrushless)
# this will make the motor move at its full speed.
# It is a percent measured from [-1.0, 1.0] inclusive
my_spark.set(1.0)
# This will stop the motor
my_spark.set(0.0)
# This will make the motor go fully in reverse
my_spark.set(-1.0)
