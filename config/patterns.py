# Matrix patterns: (begin_pattern, end_pattern, replacement)
MATRIX_PATTERNS = [
    (r'\\begin\s*{\s*matrix\s*}', r'\\end\s*{\s*matrix\s*}', r' \\newline '),
    (r'\\begin\s*{\s*pmatrix\s*}', r'\\end\s*{\s*pmatrix\s*}', r' \\newline '),
    # Add other matrix environments
]

# Table replacements: {pattern: replacement}
TABLE_REPLACEMENTS = {
    r'\\backslash\s*': r'\\',
    r'\\backslash\\backslash': r'\\newline',
    r'~': '',
    r'\\_': '_',
    r'\\text\\ ': r'\\text',
    r'\\multicolumn{\s*2\s*}{\s*[|]?[clr]\s*[|]?}': r'\\ &',
    # Add other table replacements
}

# Text replacements
TEXT_REPLACEMENTS = {
    r'\\textquotesingle': "'",
    r'\\strut': '',
    r'Sol\.': 'Sol.\\newline$',
    r'\\begin\s*{\s*quote\s*}': '',
    r'\\end\s*{\s*quote\s*}': ''
}

# Question/answer patterns
QUESTION_PATTERNS = {
    r'(\d+)\.\s*(.*?)(?=\d+\.|\Z)': self._format_question_answer,
    # More question patterns
}

def _format_question_answer(match: re.Match) -> str:
    """Format question and answer blocks"""
    num, content = match.groups()
    if "Ans." in content:
        parts = content.split("Ans.")
        return f"{num}. {parts[0]}Ans.\\newline${parts[1]}$"
    return f"{num}. {content}"