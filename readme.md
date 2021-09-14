# Sentence Generator

This project generates sentences based on a Markov chain.

# Available Models

- Quotes: Trained with data from around 70K+ tweets
- Shakespeare: Trained with data from around 100K+ lines of Shakespeare
- Whatsapp: Trained with data from around 14K+ lines of WhatsApp group messages
- News: Trained with data from around 1.2M+ lines of news headlines

# Usage

```
model = Generator("<Model Name>") # Loads the model from models/
print(model.get()) # Generates a sentence and prints it
```

See workspace.ipynb for more usage details.

# Training

Each file should have sentences separated by newlines.

```
train("<filename>","< Model Name >"[,<Number of Sentences>])
```

# API

api.py is a REST like interaction with the program.
