import re
from typing import List
from config.patterns import MATRIX_PATTERNS

class MatrixProcessor:
    def __init__(self):
        self.patterns = MATRIX_PATTERNS

    def process(self, content: str) -> str:
        """Process all matrix environments in the content"""
        for begin_pattern, end_pattern, replacement in self.patterns:
            content = self._process_matrix_env(content, begin_pattern, end_pattern, replacement)
        return content

    def _process_matrix_env(self, content: str, begin_pattern: str, end_pattern: str, replacement: str) -> str:
        """Process a specific matrix environment"""
        pattern = re.compile(fr'({begin_pattern})(.*?)({end_pattern})', re.DOTALL)
        return pattern.sub(lambda m: self._replace_matrix(m, replacement), content)

    def _replace_matrix(self, match: re.Match, replacement: str) -> str:
        """Replace matrix delimiters with specified replacement"""
        begin, matrix_content, end = match.groups()
        processed_content = matrix_content.replace(r'\\', replacement)
        return f"{begin}{processed_content}{end}"