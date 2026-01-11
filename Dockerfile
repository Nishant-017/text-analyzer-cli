
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#  Download spaCy English model

RUN python -m spacy download en_core_web_sm

#  Download NLTK datasets

RUN python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger wordnet stopwords


COPY . .

ENTRYPOINT ["python", "-m", "text_analyzer.cli"]

