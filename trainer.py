
from tqdm import tqdm
from json import dumps
import lzma
START, END = "{{start}}", "{{end}}"


def add(words: list, sentence: list, word: str):
    if word not in words:
        sentence.append(len(words))
        words.append(word)
    else:
        sentence.append(words.index(word))


def train(file: str, name: str, limit: int = None) -> None:
    """
    Generate the model with data from the given file.
    """

    # Reads, tokenize and adds sentences to array 'sentences'
    sentences = []
    words = []
    with open(f"data/{file}", 'r') as f:
        if limit:
            data = f.readlines()[:limit]
        else:
            data = f.readlines()
        for line in tqdm(data, desc="Parsing data"):
            sentence = []
            add(words, sentence, START)
            for word in line.lower().split():
                # Splits word and punctuation
                if word[-1] in "?!.,":
                    add(words, sentence, word[:-1])
                    add(words, sentence, word[-1])
                    continue
                add(words, sentence, word)
            add(words, sentence, END)
            sentences.append(sentence)

    # Counts frequenzy of following
    markov_chain = {}
    for sentence in tqdm(sentences, desc="Training model"):
        for i in range(len(sentence) - 1):
            if not markov_chain.get(sentence[i]):
                markov_chain[sentence[i]] = {sentence[i + 1]: 1}
                continue
            if not markov_chain[sentence[i]].get(sentence[i + 1]):
                markov_chain[sentence[i]][sentence[i + 1]] = 1
                continue
            markov_chain[sentence[i]][sentence[i + 1]] += 1
    # Normalizing values
    for lead in tqdm(list(markov_chain.keys()), desc="Normalizing Values"):
        sum = 0
        for counts in markov_chain[lead].values():
            sum += counts
        for follow in markov_chain[lead].keys():
            markov_chain[lead][follow] /= sum
    # Writes model to file
    print(f"Writing model to {name}")
    lzma.open(f"models/{name}.xz", "w").write(dumps(markov_chain).encode())
    dumps(markov_chain)
    with open(f"models/{name}.txt", 'w') as f:
        f.write("\n".join(words))
    print(f"Done writing model to {name}")
