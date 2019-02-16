'''
une autre solution est d'utiliser ZMQ
MAIS, il faut identifier un full node qui offre un feed ZMQ
tcp://zmq.devnet.iota.org:5556 n'est pas stable...
'''
from iota import Iota

api = Iota("https://nodes.devnet.thetangle.org:443")
print(api.get_node_info())
transactions = api.find_transactions(addresses=["GHLEMUXUIYJK9SKXOUMNEKZBRDHZVFUURXOYMQQODSWEGYRROOGGILVYTGTCCLOYDCETCKHUT9LRXJMMD"])
print(transactions)