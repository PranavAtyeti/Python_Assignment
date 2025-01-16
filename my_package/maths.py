from .logger_config import logger

def add(a, b):
    logger.debug(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    logger.debug(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logger.error("Attempted to divide by zero.")
        raise ValueError("Cannot divide by zero!")
    logger.debug(f"Dividing {a} / {b}")
    return a / b
