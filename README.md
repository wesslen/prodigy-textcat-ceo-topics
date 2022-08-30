<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Textcat model of CEO Letters topics

This project creates a textcat model on American CEO Letters to Shareholders to identify topics (e.g., Technology)

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `db-in` | One time to create spaCy config for modeling |
| `create-config` | One time to create spaCy config for modeling |
| `textcat-manual` | Textcat manual in a text by highlighting them and selecting the respective labels. |
| `textcat-teach` | Textcat teach (active learning) in a text. |
| `merge` | Merge textcat teach with existing annotations |
| `data-to-spacy` | Merge your annotations and create data in spaCy's binary format |
| `data-to-spacy-teach` | Merge your annotations and create data in spaCy's binary format |
| `train-prodigy` | Train a textcat model with prodigy |
| `train-spacy` | Train a textcat model with spaCy |
| `train-curve` | Train the model with Prodigy by using different portions of training examples to evaluate if more annotations can potentially improve the performance |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `clean` | Remove intermediate files |
| `clean-prodigy` | Clean Prodigy datasets |
| `document` | Export README for project details |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `initial-train` | `db-in` &rarr; `data-to-spacy` &rarr; `train-spacy` |
| `teach-train` | `merge` &rarr; `data-to-spacy-teach` &rarr; `train-spacy` |
| `diagnose` | `train-curve` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/ceo-letters-sample.jsonl`](assets/ceo-letters-sample.jsonl) | Local | Sample of sentences from CEO Letters for Five Companies |
| [`assets/ceo_tech_dataset.jsonl`](assets/ceo_tech_dataset.jsonl) | Local | JSONL-formatted development data exported from Prodigy, annotated with `TECHNOLOGY` labels (300 examples) |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->