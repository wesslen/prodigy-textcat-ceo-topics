import spacy_streamlit
import typer


def main(models: str, default_text: str = "As the importance of cloud, AI and digital platforms grows, this competition will become even more formidable."):
    models = [name.strip() for name in models.split(",")]
    spacy_streamlit.visualize(models, default_text, visualizers=["textcat_multilabel"])


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass