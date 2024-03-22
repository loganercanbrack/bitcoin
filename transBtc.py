# Used to collect the transacted addresses from the blockchain and save in the blocks directory

import requests
import json
import re
from hashlib import sha256
import hashlib
import base58
from Crypto.Hash import RIPEMD160
import os

def get_latest_block():
    url = "http://127.0.0.1:8332/"
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblockcount", "params": []}
    response = requests.post(url, headers=headers, json=payload, auth=('ubuntu', 'Google5005!'))
    return response.json()['result']

def get_block_hash(block_number):
    url = "http://127.0.0.1:8332/"
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblockhash", "params": [block_number]}
    response = requests.post(url, headers=headers, json=payload, auth=('ubuntu', 'Google5005!'))
    return response.json()['result']

def get_block_data(block_hash):
    url = "http://127.0.0.1:8332/"
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblock", "params": [block_hash]}
    response = requests.post(url, headers=headers, json=payload, auth=('ubuntu', 'Google5005!'))
    return response.json()['result']

def get_transaction_data(tx_hash, block_hash):
    url = "http://127.0.0.1:8332/"
    headers = {"Content-Type": "application/json"}
    payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getrawtransaction", "params": [tx_hash, True, block_hash]}
    response = requests.post(url, headers=headers, json=payload, auth=('ubuntu', 'Google5005!'))
    return response.json()['result']

def pubkey_to_address(pubkey: str) -> str:
    sha256_result = sha256(bytes.fromhex(pubkey)).digest()
    ripemd160 = RIPEMD160.new()
    ripemd160.update(sha256_result)
    ripemd160_result = ripemd160.digest()
    network_byte = b'\x00'
    versioned_payload = network_byte + ripemd160_result
    sha256_2 = sha256(versioned_payload).digest()
    sha256_3 = sha256(sha256_2).digest()
    checksum = sha256_3[:4]
    binary_address = versioned_payload + checksum
    address = base58.b58encode(binary_address).decode('utf-8')
    return address

def main():
    latest_block = get_latest_block()
    print(f"Total Blocks: {latest_block}")
    for block_number in range(191879, latest_block + 1):
        print(f"Current Block: {block_number}")
        block_hash = get_block_hash(block_number)
        block_data = get_block_data(block_hash)
        addresses = []
        for tx_hash in block_data['tx']:
            tx_data = get_transaction_data(tx_hash, block_hash)
            for vout in tx_data['vout']:
                if vout['scriptPubKey']['type'] == 'pubkeyhash' or vout['scriptPubKey']['type'] == 'scripthash' or vout['scriptPubKey']['type'] == 'witness_v0_keyhash':
                    address = vout['scriptPubKey']['address']
                    addresses.append(address)
                elif vout['scriptPubKey']['type'] == 'pubkey':
                    desc = vout['scriptPubKey']['desc']
                    pattern = re.compile(r'pk\((.*?)\)')
                    match = pattern.search(desc)
                    if match:
                        raw_public_key = match.group(1)
                        address = pubkey_to_address(raw_public_key)
                        addresses.append(address)
        with open(f'blocks/{block_number}.txt', 'w') as f:
            for address in addresses:
                f.write(address + '\n')

if __name__ == '__main__':
    main()
