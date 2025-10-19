# LaTeX Content Processor

This project provides a Python-based pipeline for processing and transforming LaTeX content. It is designed to handle various elements within LaTeX documents, including text, tables, matrices, and question/answer formats, applying predefined rules for cleaning and reformatting.




## Project Structure

- `main.py`: The main script that orchestrates the processing pipeline.
- `patterns.py`: Defines regular expressions and replacement rules for various LaTeX elements.
- `file_handler.py`: Handles reading from and writing to files.
- `matrix_processor.py`: Processes LaTeX matrix environments.
- `question_processor.py`: Processes question and answer blocks.
- `table_processor.py`: Processes LaTeX table environments.
- `text_processor.py`: Processes general text-related issues and replacements.
- `input.tex`: Example input LaTeX file (to be created by the user).
- `processed_input.tex`: Output file after processing.




## Setup

To set up the project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Install dependencies:**

    This project uses standard Python libraries. No special installation is required beyond a Python environment.

3.  **Prepare input file:**

    Place your input LaTeX file (e.g., `input.tex`) in the root directory of the project. This file will be processed by the `main.py` script.




## Usage

To process a LaTeX file, simply run the `main.py` script:

```bash
python main.py
```

This script will:
- Read the content from `input.tex`.
- Apply a series of transformations using the defined processors (`TextProcessor`, `TableProcessor`, `MatrixProcessor`, `QuestionProcessor`).
- Write the processed content to `processed_input.tex`.

### Customizing Processing Rules

The processing rules are defined in `patterns.py`. You can modify this file to customize how different LaTeX elements are handled:

-   **`MATRIX_PATTERNS`**: A list of tuples defining patterns for matrix environments and their replacements. Each tuple contains a begin pattern, an end pattern, and a replacement string for `\\` within the matrix.
-   **`TABLE_REPLACEMENTS`**: A dictionary of regular expressions and their replacements for general table-related issues.
-   **`TEXT_REPLACEMENTS`**: A dictionary of regular expressions and their replacements for general text formatting issues.
-   **`QUESTION_PATTERNS`**: A dictionary of regular expressions and a function to format question and answer blocks.



