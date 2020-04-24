import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


debug_file_handler = logging.FileHandler('logs_debug_numeric_functions.log')
debug_formatter = logging.Formatter('%(asctime)s || %(levelname)s || %(module)s || %(message)s')
debug_file_handler.setFormatter(debug_formatter)
debug_file_handler.setLevel(logging.DEBUG)

error_file_handler = logging.FileHandler('logs_error_numeric_functions.log')
error_formatter = logging.Formatter('%(asctime)s || %(levelname)s || %(module)s || %(message)s')
error_file_handler.setFormatter(error_formatter)
error_file_handler.setLevel(logging.ERROR)

logger.addHandler(debug_file_handler)
logger.addHandler(error_file_handler)

def add(x,y):
    result = x + y
    logger.info(f'{x} + {y} = {result}')
    return result

def subtract(x,y):
    result = x - y
    logger.info(f'{x} - {y} = {result}')
    return result

def multiply(x,y):
    result = x * y
    logger.info(f'{x} * {y} = {result}')
    return result

def divide(x,y):
    try:
        result = x / y

    except ZeroDivisionError as e:
        logger.exception("Someone tried to divide by zero!")
        raise e
    else:
        logger.info(f'{x} / {y} = {result}')
        return result
    finally:
        logger.debug("This we gonna log always.")

    print("This will not be printed!")
    logger.debug("Neither will this be logged!")