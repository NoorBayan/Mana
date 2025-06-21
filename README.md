# Mana (مَعنَى): A Thematically Annotated Corpus of Arabic Poetry

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Z6r-Q37jYzyjHcR-nAtRXRfr9BTAWLYG?usp=drive_link) 

---

### Table of Contents
- [Introduction](#introduction)
- [Core Features](#core-features)
- [Dataset Structure](#dataset-structure)
- [Data Fields Explained](#data-fields-explained-mana_corpuscsv)
- [Thematic Annotation Schema](#thematic-annotation-schema)
- [Interactive Exploration with Google Colab](#interactive-exploration-with-google-colab)
- [License](#license)

---

### Introduction

Welcome to **Mana (مَعنَى)**, a comprehensive digital resource for Arabic poetry. This large-scale corpus provides a vast collection of poems drawn from centuries of literary tradition, with each work meticulously annotated with multiple literary themes. Mana was developed to bridge a significant gap in digital resources for Arabic literature, offering a structured, machine-readable dataset ideal for computational analysis and academic research.

Our goal is to empower researchers, developers, and digital humanists with high-quality data to explore the rich tapestry of Arabic poetic heritage in new and innovative ways.

### Core Features

Mana is more than just a collection of texts; it's a feature-rich dataset designed for modern research needs:

*   **Deep Thematic Granularity**: Moving beyond simple single-theme labels, each poem in Mana is tagged with multiple relevant themes, complete with percentage scores reflecting their prominence. This multi-faceted approach captures the true thematic complexity of Arabic verse.
*   **A Catalyst for Computational Research**: Mana's structured format is ideal for training and benchmarking machine learning models. It supports tasks like multi-label classification, poetic sentiment analysis, and generative AI, paving the way for new applications in Arabic NLP.
*   **Broad Historical and Stylistic Scope**: The corpus covers a wide range of historical eras, from the pre-Islamic period to the modern day. Its detailed metadata enables large-scale quantitative studies on the evolution of literary themes and styles.
*   **Designed for Interdisciplinary Use**: Mana serves as a bridge between the humanities and computer science. It provides a common ground for literary scholars, historians, and NLP researchers to explore Arabic's poetic heritage using diverse methodologies.

### Dataset Structure

The dataset is organized into a primary data file and a directory of metadata files, ensuring clarity and ease of use. The main data file is named `mana_corpus.csv`.

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

| Column Name            | Description                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| `poem_id`              | A unique identifier for each poem.                                            |
| `poet_name`            | The name of the poet in Arabic script.                                        |
| `poem_title`           | The title of the poem in Arabic script.                                       |
| `poet_era`             | The historical period of the poet, linking to `era_definitions.json`.         |
| `original_diwan_theme` | The original theme from the source "Diwan" corpus, for reference.             |
| `verses`               | The complete text of the poem, with verses typically stored as a list of strings. |
| `themes`               | A list of hierarchical theme IDs from our taxonomy.                           |
| `percentages`          | A list of relevance scores (as percentages) for each assigned theme.          |

### Thematic Annotation Schema

The thematic annotation in Mana is guided by a custom-built hierarchical taxonomy. This schema, detailed in `corpus_metadata/hierarchical_thematic_taxonomy.json`, provides a structured vocabulary for poetic themes, capturing semantic relationships between them. Each theme entry includes a unique ID, Arabic and English names, a description, and its sub-themes.

### Interactive Exploration with Google Colab

To enhance the accessibility and usability of the **Mana** corpus, we have developed a user-friendly interactive notebook. This tool allows anyone to visually explore, filter, and analyze the dataset directly in their browser—no coding required.

➡️ **[Open the Interactive Explorer in Google Colab](https://colab.research.google.com/drive/1Z6r-Q37jYzyjHcR-nAtRXRfr9BTAWLYG?usp=drive_link)

The notebook provides two main interactive dashboards:

#### 1. Thematic Poem Browser

This feature allows you to navigate the corpus through its rich thematic hierarchy. You can:

*   **Drill-down through themes**: Start from broad categories (e.g., "Love Poetry") and progressively narrow down to specific sub-themes (e.g., "Chaste Love" -> "Love from a distance").
*   **Instantly access poems**: Once a theme is selected, the interface populates a list of all poems annotated with that theme.
*   **View detailed poem analysis**: Selecting a poem displays its full text, along with metadata (poet, era) and an interactive pie chart visualizing its thematic composition.

This browser makes discovering connections and finding specific examples of poetic expression incredibly easy.

*Figure 1: The interactive poem browser in action. Users can select thematic categories to filter poems and view a detailed analysis with a dynamic chart for each poem.*


 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Mana/main/images/ThematicPoemBrowser.png" width = "1000px"/>
 </p>

#### 2. Cross-Era Thematic Analysis Dashboard

This advanced analytical tool is designed for comparative literary studies. It empowers users to investigate how poetic themes have evolved or varied across different historical periods. The key functionalities include:

*   **Select a theme and a historical era**: For instance, analyze "Praise Poetry" during the "Umayyad Period".
*   **Generate dynamic bar charts**: The tool automatically processes the data and generates a series of hierarchical bar charts. Each chart breaks down the selected primary theme into its sub-themes, showing the frequency of each within the chosen era.
*   **Uncover literary trends**: This dashboard enables data-driven insights into questions like: "Which sub-themes of Satire were most prevalent in the Abbasid era compared to the Modern era?".


 <p align="center">
   <img src = "https://raw.githubusercontent.com/NoorBayan/Mana/main/images/ThematicAnalysis.png" width = "800px"/>
 </p>

This powerful feature transforms the Mana corpus from a static dataset into a dynamic laboratory for literary and historical inquiry.

### License

This work is licensed under the **Creative Commons Attribution 4.0 International License**.

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This means you are free to:
*   **Share** — copy and redistribute the material in any medium or format.
*   **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
*   **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

For the full license text, please see the [LICENSE](https://github.com/NoorBayan/Mana/blob/main/LICENSE) file.
