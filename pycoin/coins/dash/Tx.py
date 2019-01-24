
from .SolutionChecker import DashSolutionChecker
from .Solver import DashSolver
from pycoin.coins.bitcoin.Tx import Tx as BaseTx

class Tx(BaseTx):
    Solver = DashSolver
    SolutionChecker = DashSolutionChecker
    #TODO: add special transactions
