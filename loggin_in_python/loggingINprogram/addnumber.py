from logger import logging

def add_number(a, b):
    logging.debug(f"Adding operation is taking place for {a} and {b}")
    return a + b

logging.debug("add_number function has been called")
add_number(5, 7)
