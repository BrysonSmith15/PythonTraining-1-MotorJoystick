from wpilib import TimedRobot, Watchdog, run
from rev import CANSparkLowLevel, CANSparkMax
from wpilib import Joystick


class Robot(TimedRobot):
    # Initialize Robot
    def robotInit(self):
        Watchdog(0.05, lambda: None).suppressTimeoutMessage(True)
        self.my_motor = CANSparkMax(23, CANSparkLowLevel.MotorType.kBrushless)
        self.my_joystick = Joystick(0)

    def robotPeriodic(self) -> None:
        pass

    # Autonomous Robot Functions
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def autonomousExit(self):
        pass

    # Teleop Robot Functions
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        print(self.my_joystick.getRawAxis(0))
        self.my_motor.set(self.my_joystick.getRawAxis(0))

    def teleopExit(self):
        pass

    # Test Robot Functions
    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    def testExit(self):
        pass

    # Disabled Robot Functions
    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def disabledExit(self):
        pass

    def SimulationPeriodic(self) -> None:
        pass


# Start the Robot when Executing Code
if __name__ == "__main__":
    run(Robot)
