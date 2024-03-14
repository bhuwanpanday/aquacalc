import math
import numpy as np


def area(diameter):
    """Calculates the area of a circlular pipe.

    Args:
        diameter (float): The diameter of the pipe in mm .

    Returns:
        float: The area of the circularpipe  in m^2.
    """

    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if diameter <= 0:
        raise ValueError("Diameter cannot be zero or negative")
    return math.pi * (diameter / 1000 / 2) ** 2


def velocity(flow, diameter):
    """
    Calculates the average velocity of fluid in a circular pipe.

    Parameters:
    Q (float): The volumetric flow rate of the fluid in L/s.
    Diameter (float): The diameter of the pipe in mm.

    Returns:
    float: The average velocity of the fluid in m/s.
    """
    if not isinstance(flow, (int, float)):
        raise TypeError("Flow must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")

    return (flow / area(diameter)) / 1000

def reynolds_number(flow, diameter, viscosity=1.3 * 10**-6):
    """
    Calculates the Reynolds number for flow in a circular pipe.

    Parameters:
    Q (float): The flow rate of the fluid in m^3/s.
    Diameter (float): The diameter of the pipe in mm.
    viscosity (float): The viscosity of the fluid in m^2/s. Default is 1.3 * 10**-6.

    Returns:
    float: The Reynolds number.
    """
    if not isinstance(flow, (int, float)):
        raise TypeError("Flow rate (Q) must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if not isinstance(viscosity, (int, float)):
        raise TypeError("Viscosity must be a number (int or a float)")

    v = velocity(flow, diameter)
    return (v * diameter / 1000) / viscosity
