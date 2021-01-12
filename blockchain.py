#importando a biblioteeca datetime, cada bloco ele tem sua data exata
import datetime 
import hashlib
import json
from flask import Flask, jsonify


#iniciando o bloco 1, criando blockchain

class Blockchain: 
    #self as variaveis da classe pertence a classe
    def __init__(self): 
             #lista que vai conter o bloco (blockchain)
      self.chain = []
            #criando bloco genesis
      self.create_block(proof = 1, previous_hash = '0')

  #funcao de mineração para resolver o problema do HASH
    #adiconando o bloco no chain array 
    
    
    
    def create_block(self, proof, previous_hash):
        #criando dicionando, vai ter 4 chaves (index (numercao do bloco) datimete (dtata), previousHash(hash enterior))
        #criando o index do bloco
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof, 
                  'previous_hash': previous_hash }
        
        #incluindo o bloco na cadeira ou seja no blockchain
        self.chain.append(block)
        #retornando o valor quando chamar a funcao
        return block
    
    
    
    #metodo para retornar o bloco anterior
    def get_previous_block(self):
          #pegando bloco anterior
          return self.chain[-1]
          #numero para os mineradores achar ou seja a dificuldade, o numero espeicifico 
          
        
          
        
        
    def proof_of_work(self, previous_hash):
        
        new_proof = 1
              #checa se a prova é correta ou seja encontrou a solução
        check_proof = False
              
              #enquanto a variavel check prof estiver como falso
        while check_proof is False:
                  #gerando os hash no formato hexadecimal 
                 
          hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
                 #verificando se o hash atende o nivel de dificildade
                   #Se o hash iniciar com 4 zeros a esquerda 
        if hash_operation[:4] == '0000':     
            check_proof = true
        else:
             new_proof += 1
        
       return new_proof
    
    
    #Função HASH, ela vai retornar e gerar o SHA256 de um bloco
    def hash(self, block): 
        #gerando o JSON do bloco, transformando bloco em JSON
        encoded_block = json.dumps(block, sort_keys=True).encode()
        #gerando o hash do arquivo acima
        return hashlib.sha256(encoded_block).hexdigest()
            
    #funcao da cadeia de bloco,  chain é o bloco
    def is_chain_valid(self, chain):
        #loop para percorrer todos os blocos
        previous_block = chain[0]
        #index do bloco atual
        block_index = 1
        #passando por todos os blocos
        while block_index < len(chain):
            block = chain[block_index]    
            if block['previous_hash'] != self.hash(previous_block): 
                return False
           
            previous_proof = previous_block['proof']
            proof = block['proof']
            #gerando o HASH 
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2.encode()).hexdigest();
           #verificando se o bloco tem 4 zeros a esquerda
           if hash.operation[:4] != '0000';:
               return False
           previous_block = block
           block_index += 1 
           
         return True  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    