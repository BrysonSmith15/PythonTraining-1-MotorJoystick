from wpilib import TimedRobot, Watchdog, run


class Robot(TimedRobot):
    # Initialize Robot
    def robotInit(self):
        Watchdog(0.05, lambda: None).suppressTimeoutMessage(True)

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
        pass

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
