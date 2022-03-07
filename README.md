# Double spending scores

This code generates a list of addresses with a random score between 0 and 1. The list will be used to simulate the prevention of double spending attacks on the [TrustChain](https://github.com/Tribler/trustchain-superapp).

## Usage

The first argument of the file is the `length`. Default value is `128`. To generate 256 random addresses with random scores execute

```sh
./addresses.py 256
```

The second argument is the `seed`. Default value is `1337`.

```sh
./addresses.py 256 21000000
```

A file `output-addresses-<seed>-<length>.txt` will be created containing the output.

### Input addresses

To ensure certain addresses are in the output, one can place them in an input file named `input-addresses.txt`. Addresses in this file will be automatically added with a random score to the beginning of the output list.
