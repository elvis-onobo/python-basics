import logging

class CustomerException(Exception):
    pass


def risky_funct():
    logging.basicConfig(level=logging.ERROR)
    logging.error("There was an error in risky_funct.")
    raise CustomerException("Something went wrong")


try:
    risky_funct()
except CustomerException as e:
    print(e)