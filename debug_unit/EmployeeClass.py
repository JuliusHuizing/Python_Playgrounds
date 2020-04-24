import logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs_EmployeeClass.log')
formatter = logging.Formatter('%(asctime)s || %(levelname)s || %(module)s || %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        logger.info('Someone asked your name.')
        return self.first_name + " " + self.last_name
