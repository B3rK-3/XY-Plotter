""" ""
Positon can be determined by setting two circle equations equal to each other.
x^2 + y^2 = r^2
r -> is the length of the belt
    -> this can be detected by keeping the number of turns in a integer
    -> out motor is capable of doing 0.9 degrees per step
    -> our pulley teeths are 5 mm in diatemer r_(pulley) = 0.25 cm
    -> circumference of a circle -> c = 2(pi)r
        -> c = 0.50(pi) is the circumference for 360 degrees
        -> with each turn (0.9 degrees) it can release 0.00125(pi) cm
We can home the plotter by placing one or two switches on left side
(0,0) -> left top
(0,w) -> right top
(h,0) -> left bottom
(h,w) -> rigth bottom
"""

import math


class Instructions:
    def __init__(self, w, h, wPrintHead, hPrintHead, motorTurn):
        self.boardW = w  # The board width in cm
        self.boardH = h  # the board height in cm
        self.wPrintHead = wPrintHead  # width of print head
        self.hPrintHead = hPrintHead  # the distance from marker to the belt attachment
        self.PI = math.pi
        # partial circumference of circle -> s = 2(pi)*r*(angle/360)
        self.step = (
            2 * self.PI * 0.25 * (motorTurn / 360)
        )  # the amount moved in one step in cm

    def findNextMove(self, currPoint, nextPoint):
        oY, oX = currPoint  # old (y,x)
        leftRadius = math.sqrt(oY**2 + oX**2)
        rightRadius = math.sqrt(oY**2 + (self.boardW - oX) ** 2)
        y, x = nextPoint  # (y,x)
        # Radius for left belt would be c = sqrt(y^2+x^2)
        leftTargetRadius = math.sqrt(y**2 + x**2)
        # The distance from right to the point would:
        # y_(distance) = y
        # x_(distance) = w-x
        ydfr = y  # yDistanceFromRight
        xdfr = self.boardW - x  # xDistanceFromRight
        rightTargetRadius = math.sqrt(ydfr**2 + xdfr**2)
        # if such print head is heavy enough there should only be one point in which these value are true in our desired area.
        numLeftTurns = (leftTargetRadius - leftRadius) / self.step
        numRightTurns = (rightTargetRadius - rightRadius) / self.step

        return (numLeftTurns, numRightTurns)

    def home(self): #homing function
        pass

    def move(self, leftTurns, rightTurns):
        pass
