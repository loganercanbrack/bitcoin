# Used to organize the block txt files in the blocks directory into a single file without duplicates

import os
import re

BLOCKS_DIR = 'blocks'
LAST_BLOCK_FILE = 'last_processed_block.txt'
MASTER_FILE = 'master_addresses.txt'

def get_last_processed_block():
    try:
        with open(LAST_BLOCK_FILE, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def set_last_processed_block(block_number):
    with open(LAST_BLOCK_FILE, 'w') as file:
        file.write(str(block_number))

def extract_addresses_from_file(file_path):
    with open(file_path, 'r') as file:
        return re.findall(r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b', file.read())

def main():
    last_processed_block = get_last_processed_block()
    new_last_processed_block = last_processed_block
    addresses_set = set()

    for file_name in sorted(os.listdir(BLOCKS_DIR), key=lambda x: int(x.split('.')[0])):
        block_number = int(file_name.split('.')[0])
        if block_number > last_processed_block:
            file_path = os.path.join(BLOCKS_DIR, file_name)
            print(f'Processing file: {file_name}')
            addresses_set.update(extract_addresses_from_file(file_path))
            new_last_processed_block = block_number

    with open(MASTER_FILE, 'a') as master_file:
        for address in addresses_set:
            master_file.write(address + '\n')

    set_last_processed_block(new_last_processed_block)
    print(f'Processed up to block {new_last_processed_block}.')

if __name__ == '__main__':
    main()
