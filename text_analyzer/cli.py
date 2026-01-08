

import typer
from text_analyzer.tokenizers import tokenize_text
from text_analyzer.taggers import pos_tagging
from text_analyzer.taggers import ner_bio_tagging
from text_analyzer.normalizers import stem_text
from text_analyzer.normalizers import lem_text

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()



app = typer.Typer()


@app.callback()
def main():
    """
    Text Analyzer CLI
    """
    pass


@app.command()
def tokenize(text: str):

    result = tokenize_text(text)

    print("\nTOKENIZATION")
    print("Input:", text)
    print("\nSentence Tokens:",len(result["sentences"]))
    for i, sent in enumerate(result["sentences"], start=1):
        print(f"{i}. {sent}")

    print("\nWord Tokens:",len(result["words"]))
    print(result["words"])

    print("\nLLM Token Count:", result["llm_token_count"])
    print("Estimated Cost:", "$", result["estimated_cost"])



POS_DESCRIPTIONS = {
    "NN": "Noun, singular",
    "NNS": "Noun, plural",
    "NNP": "Proper noun",
    "NNPS": "Proper noun, plural",
    "VB": "Verb, base form",
    "VBD": "Verb, past",
    "VBG": "Verb, gerund",
    "VBN": "Verb, past participle",
    "VBP": "Verb, present",
    "VBZ": "Verb, 3rd person",
    "RB": "Adverb",
    "IN": "Preposition",
    "DT": "Determiner",
    "JJ": "Adjective",
    ".": "Punctuation",
}


@app.command()
def pos(text: str):

    rows = pos_tagging(text)

    console.print(Panel(" POS Tagging", style="bold cyan"))
    console.print(f"[bold]Input:[/bold] \"{text}\"\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Token")
    table.add_column("POS")
    table.add_column("Description")

    for row in rows:
        tag = row["pos"]
        description = POS_DESCRIPTIONS.get(tag, "Other")

        table.add_row(
            row["token"],
            tag,
            description
        )

    console.print(table)


NER_DESCRIPTIONS = {
    "PERSON": "Person name",
    "ORG": "Organization",
    "GPE": "Geo-political entity",
    "LOC": "Location",
    "DATE": "Date",
    "TIME": "Time",
    "MONEY": "Monetary value",
    "PERCENT": "Percentage",
    "NORP": "Nationality / group",
    "FAC": "Facility",
    "EVENT": "Event",
    "LAW": "Law or regulation",
    "LANGUAGE": "Language",
    "PRODUCT": "Product",
}



@app.command()
def ner(text: str):

    entities, bio_tags = ner_bio_tagging(text)

    console.print(Panel(" Named Entity Recognition", style="bold cyan"))
    console.print(f"[bold]Input:[/bold] \"{text}\"\n")

    console.print("[bold]Entities Found:[/bold]")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Entity")
    table.add_column("Label")
    table.add_column("Description")

    if entities:
        for ent, label in entities:
            description = NER_DESCRIPTIONS.get(label, "Other")
            table.add_row(ent, label, description)
    else:
        table.add_row("—", "—", "No entities found")

    console.print(table)

    console.print("\n[bold]BIO Tags:[/bold]")
    for token, tag in bio_tags:
        console.print(f"{token}[{tag}]", end=" ")
    console.print()




@app.command()
def stem(text: str):
    rows = stem_text(text)

    console.print(Panel("Stemming", style="bold green"))
    console.print(f"[italic]Input:[/italic] {text}\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Original")
    table.add_column("Porter")
    table.add_column("Snowball")
    table.add_column("Lancaster")

    for row in rows:
        table.add_row(
            row["original"],
            row["porter"],
            row["snowball"],
            row["lancaster"]
        )

    console.print(table)





@app.command()
def lemmatize(text: str):

    rows = lem_text(text)

    console.print(Panel(" Lemmatization", style="bold cyan"))
    console.print(f"[bold]Input:[/bold] \"{text}\"\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Original")
    table.add_column("Lemma")
    table.add_column("POS")

    for row in rows:
        table.add_row(
            row["original"],
            row["lemma"],
            row["pos"]
        )

    console.print(table)




@app.command()
def compare(text: str):

    stems = stem_text(text)
    lemmas = lem_text(text)

    # Build lemma lookup
    lemma_map = {row["original"]: row["lemma"] for row in lemmas}

    console.print(Panel("🔬 Stem vs Lemma Comparison", style="bold cyan"))

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Original")
    table.add_column("Stem")
    table.add_column("Lemma")
    table.add_column("Winner")

    stem_real = 0
    lemma_real = 0
    total = 0

    for row in stems:
        original = row["original"]
        stem = row["porter"]
        lemma = lemma_map.get(original, original)
        total += 1

        if stem == lemma:
            winner = "TIE"
            stem_real += 1
            lemma_real += 1

        elif lemma == original and stem != original:
            winner = "LEMMA ✅"
            lemma_real += 1
        elif stem == original and lemma != original:
            winner = "STEM"
            stem_real += 1

        else:
            winner = "LEMMA "
            lemma_real += 1

        table.add_row(original, stem, lemma, winner)

    console.print(table)

#    # Summary
#    stem_pct = int((stem_real / total) * 100)
#
#    console.print("\n Summary:")
#    console.print(f"  Stemming real words: {stem_real}/{total} ({stem_pct}%)")
#    console.print(f"  Lemmatization real words: {lemma_real}/{total} ({int((lemma_real / total) * 100)}%)")




@app.command()
def analyze(text: str):

    tokens = tokenize_text(text)
    entities, _ = ner_bio_tagging(text)
    lemmas = lem_text(text)

    console.print(Panel(" Full Text Analysis", style="bold cyan"))
    console.print(f"[bold]Input:[/bold] \"{text}\"\n")

    # ---------------- Tokens ----------------
    console.print("[bold yellow]── Tokens ──────────────────────────────────[/bold yellow]")
    console.print(f"Words: {tokens['words']}")
    console.print(
        f"LLM Tokens: {tokens['llm_token_count']} "
        f"(Est. cost: ${tokens['estimated_cost']})\n"
    )

    # ---------------- Named Entities ----------------
    console.print("[bold yellow]── Named Entities ──────────────────────────[/bold yellow]")
    if entities:
        for ent, label in entities:
            console.print(f"• {ent:<10} → {label}")
    else:
        console.print("No entities found")

    # ---------------- POS + Lemmas ----------------
    console.print("\n[bold yellow]── POS + Lemmas ────────────────────────────[/bold yellow]")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Token")
    table.add_column("POS")
    table.add_column("Lemma")

    for row in lemmas:
        table.add_row(
            row["original"],
            row["pos"],
            row["lemma"]
        )

    console.print(table)




if __name__ == "__main__":
    app()
