import itertools
import string
import time


class BruteForceAttackService:
    def Attack(self, password):
        characters = string.ascii_letters + string.digits + string.punctuation
        start_time = time.time()
        passwordLength = len(password)
        for password_length in range(1, passwordLength + 1):
            for attempt in itertools.product(characters, repeat=password_length):
                guess = ''.join(attempt)
                print("Trying: " + str(guess))
                if guess == password:
                    print("Password found:" + str(guess))
                    elapsed_time = time.time() - start_time
                    print(f"Method runtime: {elapsed_time:.6f} seconds")
                    return guess
        print("password not found")
        elapsed_time = time.time() - start_time
        print(f"Method runtime: {elapsed_time:.6f} seconds")
        return None
