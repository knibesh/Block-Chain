# module 1 creating a blockchain *- coding: utf-8 -*-

#importing the libraries

import datetime
import hashlib
import json
from flask import Flask, jsonify

#Part 1 -Building a Blockchain

class Blockchain:
    def _init_|self|:
        self.chain = []
        self.create_block(proof =1, previous_hash = '0')
    def create_block(self,proof,previous_hash):
        block ={'index' : len(self.chain) + 1,
                'timestamp' : str(datetime.datetime.now()),
                'proof' : proof,
                'previuos_hash' : prvious_hash }
        self.chain.append(block)
        return block
    
def get_previous_block(self):
    return self.chain [-1]