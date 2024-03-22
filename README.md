First get secp256k1 library from:
https://github.com/bitcoin-core/secp256k1.git

Zip also located in root. 
compile etc

{Add instructions}

Once finished, navigate to examples/ directory

Depends on libbase58 library from:
https://github.com/bitcoin/libbase58.git

Zip for libbase58 is also located in root directory

Install in the examples/directory

Move all depend files into this directory:

map.c 
map.h
ripemd160.c
ripemd160.h
sha256.c
sha256.h
thread.c

master_addresses.txt can be found at:

{Insert MEGA Link}
*** Only updated to block 835,000 ***
*** Saves days worth of bitcoin core calls and data extraction when collecting addresses and organizing as each block has to be called, its hash collected, then another call for tx's, then one more for transaction details. This is three http requests to bitcoin core per block. First 100,000 go by fast, but around 160,000 slows down exponentially due to shear volume of transactions per block. This equates to several days worth of building that eats up guessing time. ***
*** Recommended to download the txt file and sync up to current block count. ***
*** Stored on mega due to file size being >Gb ***
