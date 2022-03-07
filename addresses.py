import os
import random
import sys

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


def createAddressList(length = 100, input = "input-addresses.txt"):
    """
    Create a list of random addresses with random scores
    """
    addresses = []

    n = 0
    # Check if the input file exists
    if os.path.isfile(input):
        # Read the addresses from the input file
        with open(input, "r") as f:
            for line in f:
                addresses.append((line.strip(), generateScore()))
                n += 1

    for i in range(n, length):
        addresses.append((generateAddress(), generateScore()))
    return addresses


def writeAddressList(addresses, output = "output-addresses.txt"):
    """
    Write the list of addresses to a file
    """
    with open(output, "w") as f:
        for address, score in addresses:
            f.write(address + " " + str(score) + "\n")

if __name__ == "__main__":
    # Read input from the command line
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    else:
        length = 128

    # Create a list of random addresses with random scores
    addresses = createAddressList(length)

    # Write the list to a file
    writeAddressList(addresses)