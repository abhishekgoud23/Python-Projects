from hashlib import sha256
import time
MAX_NONCE = 10000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transaction, prev_hash, prefix_zeros):
    pre_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text= str(block_number)+transaction+prev_hash+str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(pre_str):
            print("YAY!,mined a bitcoin at:",nonce)
            return new_hash
    raise BaseException("Couldn't run")

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=2
    start = time.time()
    new_hash=mine(5,transactions,'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',difficulty)
    tot_time=str(time.time()-start)
    print(new_hash,tot_time)