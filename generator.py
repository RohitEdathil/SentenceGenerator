from random import choices
from json import loads
import lzma


class Generator:
    """Generates sentences based on the loaded model"""
    START = "{{start}}"
    END = "{{end}}"

    def __init__(self, name: str) -> None:
        self.name = name
        raw_str = lzma.open(f"models/{name}.xz", "r").read()
        self.markov_chain = loads(raw_str)
        self.words = [i[:-1]
                      for i in open(f'models/{name}.txt', 'r').readlines()]

    def get(self) -> str:
        '''Returns a generated string'''
        response = []
        cur = self.START

        while cur != self.END:
            sample = self.markov_chain[str(self.words.index(cur))].keys()
            weights = self.markov_chain[str(self.words.index(cur))].values()
            cur = self.words[int(choices(
                list(sample), k=1, weights=list(weights))[0])]
            response.append(cur)
        s = ''
        for i in response:
            if i not in '!?.,':
                s += " "
            s += i
        return s[1:-8].capitalize()
