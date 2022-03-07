import random

# Use a random seed to create a list of random addresses
random.seed(1337)

def generateAddress(length = 148, seed = None):
    """
    Generate a hexadeximal address
    """
    if seed is not None:
        random.seed(seed)
    address = ""
    for i in range(length):
        address +=  str(hex(random.randint(0, 15)))[2:]
    return address

def generateScore(seed = None):
    """
    Generate a random double spending score between 0 and 1
    """
    if seed is not None:
        random.seed(seed)
    return random.random()


def createAddressList(length = 100):
    """
    Create a list of random addresses with random scores
    """
    addresses = []
    for i in range(length):
        addresses.append((generateAddress(), generateScore()))
    return addresses



print(createAddressList(148))