'''
une autre solution est d'utiliser ZMQ
MAIS, il faut identifier un full node qui offre un feed ZMQ
tcp://zmq.devnet.iota.org:5556 n'est pas stable...
'''
import time

from iota import Iota, TryteString
from iota import Tag, Transaction, TransactionHash

api = Iota("https://nodes.devnet.thetangle.org:443")

transactions = api.find_transactions(addresses=["GHLEMUXUIYJK9SKXOUMNEKZBRDHZVFUURXOYMQQODSWEGYRROOGGILVYTGTCCLOYDCETCKHUT9LRXJMMD"])
transactions_hashes = transactions['hashes']
#print(len(transactions_hashes), ' transactions_hashes')

while True:
    # Code executed here
    retrieved_transactions = api.find_transactions(
        addresses=["GHLEMUXUIYJK9SKXOUMNEKZBRDHZVFUURXOYMQQODSWEGYRROOGGILVYTGTCCLOYDCETCKHUT9LRXJMMD"])
    retrieved_transactions_hashes = retrieved_transactions['hashes']

    #print(len(retrieved_transactions_hashes), ' retrieved_transactions_hashes')

    new_transactions_hashes = [tx for tx in retrieved_transactions_hashes if tx not in transactions_hashes]

    #print(len(new_transactions_hashes), ' new_transactions_hashes')

    if len(new_transactions_hashes) != 0:
        transactions_hashes += new_transactions_hashes

        new_transactions_hashes_trytes = api.get_trytes(new_transactions_hashes)
        for tryte in new_transactions_hashes_trytes['trytes']:
            tx = Transaction.from_tryte_string(tryte)
            print(TryteString(tx.tag).decode())
            print(TryteString(tx.signature_message_fragment).decode())

    time.sleep(5)

