# About the Computationally-Generated Thematic Layers

A substantial portion of the **Mana** corpus, encompassing over 148,000 poems, features thematic annotations generated through a computational framework. This document provides a concise overview of the methodology behind these large-scale annotations.

These thematic layers were produced as part of the **[Maqasid initiative](https://github.com/NoorBayan/Maqasid)**, which is dedicated to creating sophisticated computational approaches for analyzing Arabic literary traditions.

### The Annotation Process: A High-Level View

The generation of thematic tags for this extensive collection followed a structured, machine learning-driven workflow. Here is a simplified breakdown of the core steps:

1.  **Foundation in Human Expertise:** The system's intelligence was cultivated using a "gold-standard" dataset. This foundational set was meticulously labeled by specialists in Arabic literature, providing the machine with a rich source of expert knowledge to learn from.

2.  **Learning Poetic Nuance:** The underlying model was architected to grasp the complex nature of poetic language. It employs a specialized neural network design that processes both localized linguistic features and the broader sequential context of a poem. This enables it to identify multiple, often overlapping, thematic threads within a single work.

3.  **Large-Scale Application:** After a rigorous validation phase on unseen data, the trained system was used to analyze the wider Diwan collection. It assigned relevant thematic tags to each poem based on our [comprehensive thematic schema](https://github.com/NoorBayan/Mana/blob/main/corpus/hierarchical_thematic_taxonomy.json), also calculating a relevance score for each assigned theme.

### Interpreting the Automated Annotations

While these computationally-generated labels open new avenues for quantitative literary studies, users should consider the following points:

*   **A Tool for Discovery, Not a Final Word:** The labels are highly reliable statistical predictions. They are best used as a powerful lens for uncovering patterns and formulating research questions, rather than as definitive, case-by-case literary assertions.
*   **Strength in Aggregate Analysis:** This dataset is uniquely suited for birds-eye-view research. Its scale allows for robust analysis of large-scale literary phenomena, such as tracing thematic shifts over centuries or comparing the stylistic repertoires of entire poetic schools.
*   **An Evolving Resource:** The annotation of this corpus is a dynamic project. We anticipate ongoing refinements to both the dataset and the underlying models.

### For a Deeper Technical Dive

This document is designed for a general audience. For complete technical specifications of the model architecture, evaluation metrics, and the full research methodology, we invite you to explore the **[Maqasid Framework repository](https://github.com/NoorBayan/Maqasid)**.
