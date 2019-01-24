from ..SolutionChecker import ScriptError
from pycoin.satoshi.flags import SIGHASH_FORKID
from ..bitcoin.SolutionChecker import BitcoinSolutionChecker

class DashSolutionChecker(BitcoinSolutionChecker):
    def _signature_hash(self, tx_out_script, unsigned_txs_out_idx, hash_type):
        return self._signature_for_hash_type_segwit(tx_out_script, unsigned_txs_out_idx, hash_type)
