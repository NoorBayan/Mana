# Mana (مَعنَى): A Thematically Annotated Corpus of Arabic Poetry

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper](https://img.shields.io/badge/Read%20the%20Paper-Data%20in%20Brief-b51e44.svg)](https://doi.org/YOUR_PAPER_DOI_HERE) <!-- <-- الرجاء وضع رابط الـ DOI الخاص بالورقة عند نشره -->

---

### Introduction

Welcome to **Mana (مَعنَى)**, a comprehensive digital resource for Arabic poetry. This corpus provides a vast collection of approximately half a million poems, each meticulously annotated with multiple literary themes. Mana was developed to bridge a significant gap in digital resources for Arabic literature, offering a structured, machine-readable dataset ideal for computational analysis and academic research.

Our goal is to empower researchers, developers, and digital humanists with high-quality data to explore the rich tapestry of Arabic poetic heritage in new and innovative ways.

### Core Features

Mana is more than just a collection of texts; it's a feature-rich dataset designed for modern research needs:

*   **Deep Thematic Granularity**: Moving beyond simple single-theme labels, each poem in Mana is tagged with multiple relevant themes, complete with percentage scores reflecting their prominence. This multi-faceted approach captures the true thematic complexity of Arabic verse.
*   **A Catalyst for Computational Research**: Mana's structured format is ideal for training and benchmarking machine learning models. It supports tasks like multi-label classification, poetic sentiment analysis, and generative AI, paving the way for new applications in Arabic NLP.
*   **Broad Historical and Stylistic Scope**: The corpus covers a wide range of historical eras, from the pre-Islamic period to the modern day. Its detailed metadata enables large-scale quantitative studies on the evolution of literary themes and styles.
*   **Designed for Interdisciplinary Use**: Mana serves as a bridge between the humanities and computer science. It provides a common ground for literary scholars, historians, and NLP researchers to explore Arabic's poetic heritage using diverse methodologies.

### Dataset Structure

The dataset is organized into a primary data file and a directory of metadata files, ensuring clarity and ease of use. Please note the main data file is named `mana_corpus.csv`.

```
/
├── mana_corpus.csv                 # The primary data file with all poems and annotations.
├── corpus_metadata/
│   ├── hierarchical_thematic_taxonomy.json  # Defines the multi-level thematic classification schema.
│   ├── era_definitions.json                 # Maps era IDs to their names and descriptions.
│   └── diwan_original_themes.json           # Provides context for theme IDs from the source corpus.
└── README.md
```

### Data Fields Explained (`mana_corpus.csv`)

This is the main file containing the poetic data. Below is a description of each column.

| Column Name                   | Description                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------- |
| `poem_id`                     | A unique identifier for each poem.                                            |
| `poet_name`                   | The name of the poet in Arabic script.                                        |
| `poem_title`                  | The title of the poem in Arabic script.                                       |
| `poet_era`                    | A numerical key linking to the poet's historical period in `era_definitions.json`. |
| `original_diwan_theme`        | The original theme ID from the source "Diwan" corpus, for reference.          |
| `verses`                      | The complete text of the poem. Verses are separated by a newline (`\n`) character. |
| `themes`                      | A semicolon-separated list of hierarchical theme IDs from our taxonomy.       |
| `percentages`                 | A semicolon-separated list of relevance scores (as percentages) for each assigned theme. |


### Thematic Annotation Schema

The thematic annotation in Mana is guided by a custom-built hierarchical taxonomy. This schema, detailed in `corpus_metadata/hierarchical_thematic_taxonomy.json`, provides a structured vocabulary for poetic themes, capturing semantic relationships between them. Each theme entry includes a unique ID, Arabic and English names, a description, and its sub-themes.


### License

The Mana corpus is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share and adapt this material for any purpose, provided you give appropriate credit.

### Contact

For questions, feedback, or collaborations, please reach out to the corresponding author:
**Reema G. Al-anazi Nour** at `rgalanizy@pnu.edu.sa`.
