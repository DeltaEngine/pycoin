from ..bitcoin.Solver import BitcoinSolver
from pycoin.satoshi.flags import SIGHASH_ALL

class DashSolver(BitcoinSolver):
    def solve(self, *args, **kwargs):
        kwargs["hash_type"] = SIGHASH_ALL
        return super(DashSolver, self).solve(*args, **kwargs)
