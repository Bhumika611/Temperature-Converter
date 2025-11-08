"""
converter.py
------------
Handles temperature conversions between Celsius, Fahrenheit, and Kelvin.
"""

def convert_temperature(value, from_scale, to_scale):
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    :param value: numeric temperature value
    :param from_scale: 'C', 'F', or 'K' (source scale)
    :param to_scale: 'C', 'F', or 'K' (target scale)
    :return: converted temperature value (float)
    """

    if from_scale == to_scale:
        return value

    # Convert to Celsius first
    if from_scale == "C":
        celsius = value
    elif from_scale == "F":
        celsius = (value - 32) * 5 / 9
    elif from_scale == "K":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source scale.")

    # Convert from Celsius to target
    if to_scale == "C":
        return celsius
    elif to_scale == "F":
        return (celsius * 9 / 5) + 32
    elif to_scale == "K":
        return celsius + 273.15
    else:
        raise ValueError("Invalid target scale.")
