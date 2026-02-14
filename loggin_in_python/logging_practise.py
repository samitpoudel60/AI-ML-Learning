import logging

logging.basicConfig(   

    level=logging.DEBUG,  ##this will set the logging level to debug so that all the messages with level debug and above will be logged
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' ,##this is for the date time format
    force=True,

    handlers=[  ## we used handlers to log the messages to multiple destinations and here we are using two handlers 
        logging.FileHandler("arithmeticapp.log"),  ##this will save the log messages to a file named app.log
        logging.StreamHandler()  ##this will also print the log messages to the console
    ]
)

##now lest make a logger for our module Arithemic app
logger1=logging.getLogger("arithmic_app")

def add(a, b):
    logger1.debug(f"Adding operation is taking place for {a} and {b}")
    return a + b

def subtract(a, b):
    logger1.debug(f"Subtracting operation is taking place for {a} and {b}")
    return a - b

def multiply(a, b):
    logger1.debug(f"Multiplying operation is taking place for {a} and {b}")
    return a * b

def divide(a, b):
    
    try:
        logger1.debug(f"Dividing operation is taking place for {a} and {b}")
        result = a / b
        return
    except ZeroDivisionError:
        logger1.error("Division by zero is not allowed.")
        return None
    
 
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)
divide(10, 2)