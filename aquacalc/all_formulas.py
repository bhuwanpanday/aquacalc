import math
import numpy as np
from scipy.optimize import brentq

from all_simple import area , velocity , flow , reynolds_number 


def swamee_jain(flow , diameter, ruhet, viscosity=1.3 * 10**-6):

    """
    Calculates the friction factor using the Swamee-Jain equation.

    Parameters:
    - flow (float): The flow rate of the fluid in the pipe (in cubic meters per second).
    - diameter (float): The diameter of the pipe (in meters).
    - ruhet (float): The roughness height of the pipe (in mm).
    - viscosity (float, optional): The dynamic viscosity of the fluid (in square meters per second). Default is 1.3 * 10**-6.

    Returns:
    - friction_factor (float): The friction factor calculated using the Swamee-Jain equation.

    Formula:
    The Swamee-Jain equation is given by:
    f = 0.25 / (math.log10((ruhet / (3.7 * diameter)) + (5.74 / Re**0.9))) ** 2

    where:
    - f is the friction factor.
    - Re is the Reynolds number calculated using the flow rate, diameter, and viscosity.

    Note:
    - This equation is used to estimate the friction factor in fully developed turbulent flow in pipes.
    - The equation assumes that the flow is turbulent and the pipe is smooth.
    """
    if not isinstance(flow, (int, float)):
        raise TypeError("Flow rate (Q) must be a number (int or a float)")
    if not isinstance(diameter, (int, float)):
        raise TypeError("Diameter must be a number (int or a float)")
    if not isinstance(ruhet, (int, float)):
        raise TypeError("Roughness height (ruhet) must be a number (int or a float)")
    if not isinstance(viscosity, (int, float)):
        raise TypeError("Viscosity must be a number (int or a float)")
   


    
    Re = reynolds_number(flow , diameter, viscosity)
    
    return 0.25 / (math.log10((ruhet / (3.7 * diameter)) + (5.74 / Re**0.9))) ** 2
    

# def not_complete_darcy_weisbach(flow , length, diameter, ruhet , friction_factor_method = 'swamee_jain'):
    
    

#     v = velocity(flow, diameter)
#     match friction_factor_method:
#         case 'swamee_jain':
#             f = swamee_jain(flow, diameter, ruhet)
        

#     return (
#         swamee_jain(Q, diameter, ruhet)
#         * (length / (diameter / 1000))
#         * (v**2)
#         / (2 * 9.81)
#     )



def colebrook_white(diameter, roughness, reynolds_number):
    
    """Calculates the friction factor for pipe flow using the Colebrook-White equation.

    Parameters:
    - diameter (float): The inner diameter of the pipe (in meters).
    - roughness (float): The absolute roughness of the pipe's inner surface (in meters).
    - reynolds_number (float): The Reynolds number of the flow, which is a dimensionless quantity.

    Returns:
    - friction_factor (float): The friction factor calculated using the Colebrook-White equation.

    Formula:
    The Colebrook-White equation is an implicit equation given by:
    1/sqrt(f) = -2 * log10((roughness/(3.7*diameter)) + (2.51/(reynolds_number*sqrt(f))))

   

    Note:
    - This function uses the Brent's method to solve the implicit Colebrook-White equation.
    - The function assumes that the flow is fully turbulent.
    - The Brent's method requires initial bracketing values, which are provided within a typical range for turbulent flow.
    - The viscosity parameter is not required because the Reynolds number is used directly.

    Exceptions:
    - ValueError: If the Brent's method fails to find a solution within the provided bracketing values, an error is raised.

    Example usage:
    friction_factor = colebrook_white(diameter=0.1, roughness=1e-5, reynolds_number=10000)
    """
   
  
    
    # Function to find root
    def f_zero(f):
        return 1.0 / math.sqrt(f) + 2.0 * math.log10(
            roughness / (3.7 * diameter) + 2.51 / (reynolds_number * math.sqrt(f))
        )

    # Initial bracketing values for f
    f_l = 0.008  # A reasonable lower bound for turbulent flow
    f_u = 0.08  # A reasonable upper bound for turbulent flow

    # Use Brent's method to find the root
    try:
        # Use Brent's method to find the root
        f = brentq(f_zero, f_l, f_u)
    except ValueError as e:
        raise ValueError("The Brent method failed to find a root: " + str(e))

    return f

