# Sentence Generator ✨

## [See Demo 👈](https://sentencesimulator.web.app/)

This project generates sentences based on [Markov Chains](https://en.wikipedia.org/wiki/Markov_chain).
All the sentences are generated based on a particular theme as mentioned in the below section.

# Available Models

- Quotes: Trained with data from around 70K+ tweets
- Shakespeare: Trained with data from around 100K+ lines of Shakespeare
- Whatsapp: Trained with data from around 14K+ lines of WhatsApp group messages
- News: Trained with data from around 1.2M+ lines of news headlines

# Usage 🛠

```python
model = Generator("<Model Name>") # Loads the model from models/
print(model.get()) # Generates a sentence and prints it
```

See workspace.ipynb for more usage details.

# Training 🏃‍♂️

Each file should have sentences separated by newlines.

```python
train("<filename>","< Model Name >"[,<Number of Sentences>])
```

# API

api.py is a FastAPI based app which provides an API interaction with the models.

# Screenshots 🌆

![Screenshot1](https://github.com/RohitEdathil/SentenceGenerator/blob/master/img/s1.jpg)
![Screenshot2](https://github.com/RohitEdathil/SentenceGenerator/blob/master/img/s2.jpg)
![Screenshot3](https://github.com/RohitEdathil/SentenceGenerator/blob/master/img/s3.jpg)

# Similar (and cooler 🤩) Projects
These are the projects from which I got inspired from.
 - [Subreddit Simulator](https://www.reddit.com/r/SubredditSimulator/)
 - [Donald Trump tweet simulator](https://filiph.github.io/markov/)
