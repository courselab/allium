import random

import modular

class Prover:
    """They want to prove they know a solution to g^x mod p = y
    with given y, g and p (p prime)
    """
    def __init__(self, g, x, p, y):
        self.g = g
        self.x = x
        self.p = p
        self.y = y

    def new_round(self):
        """Selects a random r and computes g^r mod p

        Returns
        -------
        int
            Result from g^r

        """
        self.r = random.randint(0, self.p-1)
        return modular.pow(self.g, self.r, self.p)

    def answer_easy(self):
        """Answers the value of r

        Returns
        -------
        int
            Value of self.r

        """
        return self.r

    def answer_hard(self):
        """Answers the value of (x+r) mod p-1

        Returns
        -------
        int
            Value of (x+r) mod p-1

        """
        return (self.x + self.r) % (self.p - 1)


class Verifier:
    """They want to verify if the prover actually have an answer"""
    def __init__(self, g, p, y):
        self.g = g
        self.p = p
        self.y = y

    def new_round(self, C):
        """Sets value of C = g^r for a new round

        Parameters
        ----------
        C: int
            Value of C, selected randomly by prover

        """
        self.C = C

    def check_easy(self, answer):
        """Checks if answer to value of r is correct

        Parameters
        ----------
        answer: int
            Should be value of r

        """
        return (modular.pow(self.g, answer, self.p) == self.C)

    def check_hard(self, answer):
        """Checks if answer to value of (x+r) mod p-1 is correct

        Parameters
        ----------
        answer: int
            Should be value of (x+r) mod p-1

        """
        return (modular.pow(self.g, answer, self.p) == self.C * self.y % self.p)
