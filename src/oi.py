from utils import joystick, singleton, intakestate
from constants import Constants
from wpilib.buttons.joystickbutton import JoystickButton
from commands import togglehatchlatch, drivetimed, setintakestate, setbackarm

class OI(metaclass=singleton.Singleton):
    """Deals with anything controller related,
    be it gamepads, joysticks, or steering wheels."""

    def __init__(self):
        self.driver = joystick.Joystick(
            Constants.DRIVER_PORT, Constants.DRIVER_X_MOD, Constants.DRIVER_Y_MOD, Constants.DRIVER_Z_MOD, Constants.DRIVER_T_MOD)
        self.operator = joystick.Joystick(
            Constants.OPERATOR_PORT, Constants.OPERATOR_X_MOD, Constants.OPERATOR_Y_MOD, Constants.OPERATOR_Z_MOD, Constants.OPERATOR_T_MOD)

        self.drive_buttons = [
            self.driver.getJoystickButton(n) for n in range(1, 13)]
        self.operator_buttons = [
            self.operator.getJoystickButton(n) for n in range(1, 13)]

        self.intake_suck = setintakestate.SetIntakeState(
            intakestate.IntakeState.SUCK)
        self.intake_spit = setintakestate.SetIntakeState(
            intakestate.IntakeState.SPIT)
        self.intake_stop = setintakestate.SetIntakeState(
            intakestate.IntakeState.STOP)
        self.hatch_toggle = togglehatchlatch.ToggleHatchLatch()

        # self.operator_buttons[0].whenPressed(setbackarm.SetBackArm(0))
        # self.operator_buttons[1].whenPressed(setbackarm.SetBackArm(10))
        # self.operator_buttons[2].whenPressed(setbackarm.SetBackArm(30))
        # self.operator_buttons[3].whenPressed(setbackarm.SetBackArm(60))

        self.operator_buttons[4].whenPressed(self.intake_spit)
        self.operator_buttons[4].whenReleased(self.intake_stop)
        self.operator_buttons[5].whenPressed(self.intake_suck)
        self.operator_buttons[5].whenReleased(self.intake_stop)

        self.operator_buttons[6].whenPressed(self.hatch_toggle)
	
	self.hatchbutton = JoystickButton(self.driver, 1)
        self.hatchbutton.whenPressed(togglehatchlatch.ToggleHatchLatch())
        self.scootleft = JoystickButton(self.driver, 5)
        self.scootleft.whenPressed(drivetimed.DriveTimed(Constants.SCOOT_SPEED * -1, 0, Constants.SCOOT_DURRATION))
        self.scootright = JoystickButton(self.driver, 6)
        self.scootright.whenPressed(drivetimed.DriveTimed(Constants.SCOOT_SPEED, 0, Constants.SCOOT_DURRATION))
