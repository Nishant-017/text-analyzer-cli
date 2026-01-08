# 🧠 Text Analyzer CLI

Text Analyzer is a Python-based command-line tool that demonstrates core **Natural Language Processing (NLP)** preprocessing concepts such as tokenization, part-of-speech tagging, named entity recognition, stemming, and lemmatization.

The project is designed for **learning, practice, and demonstration**, with clean CLI output rendered using **Rich** and modular NLP logic backed by **NLTK** and **spaCy**.

---

## ✨ Features

- Word, sentence, and LLM-style tokenization  
- Part-of-Speech (POS) tagging with descriptions  
- Named Entity Recognition (NER)  
- BIO tag generation  
- Stemming using:
  - Porter Stemmer
  - Snowball Stemmer
  - Lancaster Stemmer
- Lemmatization with POS tags  
- Stem vs Lemma comparison  
- Full text analysis combining multiple NLP steps  
- Clean and readable CLI output using Rich  
- Unit tests using pytest  

---

## 📂 Project Structure

# 🧠 Text Analyzer CLI

Text Analyzer is a Python-based command-line tool that demonstrates core **Natural Language Processing (NLP)** preprocessing concepts such as tokenization, part-of-speech tagging, named entity recognition, stemming, and lemmatization.

The project is designed for **learning, practice, and demonstration**, with clean CLI output rendered using **Rich** and modular NLP logic backed by **NLTK** and **spaCy**.

---

## ✨ Features

- Word, sentence, and LLM-style tokenization  
- Part-of-Speech (POS) tagging with descriptions  
- Named Entity Recognition (NER)  
- BIO tag generation  
- Stemming using:
  - Porter Stemmer
  - Snowball Stemmer
  - Lancaster Stemmer
- Lemmatization with POS tags  
- Stem vs Lemma comparison  
- Full text analysis combining multiple NLP steps  
- Clean and readable CLI output using Rich  
- Unit tests using pytest  

---

## 📂 Project Structure

task/
├── venv/
├── requirements.txt
├── text_analyzer/
│ ├── init.py
│ ├── cli.py
│ ├── tokenizers.py
│ ├── taggers.py
│ └── normalizers.py
└── tests/
├── test_tokenizers.py
├── test_taggers.py
└── test_normalizers.py



---

## ⚙️ Installation

### 1️⃣ Create and activate virtual environment


python -m venv venv
venv\Scripts\activate    # Windows

### 2️⃣ Install dependencies

python -m pip install -r requirements.txt

### 3️⃣ Download NLP resources

spaCy model
python -m spacy download en_core_web_sm

NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"


## 🧰 Tech Stack

Python

NLTK

spaCy

tiktoken

Typer

Rich

pytest

## 📝 Notes

spaCy language models are installed separately from Python packages.

Always activate the virtual environment before running the CLI or tests.

The project maintains a clean separation between:

NLP logic (modules)

CLI presentation (cli.py)

## 🎯 Learning Outcomes

This project demonstrates:

Practical NLP preprocessing workflows

Differences between stemming and lemmatization

Use of BIO tagging in NER

Writing testable, modular Python code

Building production-style CLI tools


