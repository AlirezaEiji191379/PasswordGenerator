import argparse
import hashlib

from PasswordCracker.BruteForceAttack.BruteForceAttackService import BruteForceAttackService
from PasswordCracker.DictionaryAttack.DictionaryAttackService import DictionaryAttackService

parser = argparse.ArgumentParser(description="crack password.")
parser.add_argument('--password', help="password", default= 'alireza')
parser.add_argument('--method', choices=['brute_force', 'dictionary'], default='dictionary', help="type of attack")
args = parser.parse_args()

if args.method == "brute_force":
    BruteForceAttackService().Attack(args.password)

elif args.method == "dictionary":
    DictionaryAttackService("./PasswordCracker/password_list.txt").Attack(hashlib.sha256(args.password.encode()).hexdigest())

else:
    raise ValueError("invalid password attack")
