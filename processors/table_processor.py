import re
from typing import Dict
from config.patterns import TABLE_REPLACEMENTS

class TableProcessor:
    def __init__(self):
        self.replacements = TABLE_REPLACEMENTS

    def process(self, content: str) -> str:
        """Process all table-related issues in the content"""
        # Process table environments
        content = self._process_table_environments(content)
        
        # Apply general table replacements
        for pattern, repl in self.replacements.items():
            content = re.sub(pattern, repl, content)
        
        return content

    def _process_table_environments(self, content: str) -> str:
        """Special handling for array/tabular environments"""
        pattern = re.compile(r'\\begin\s*{\s*(array|tabular)\s*}(.*?)\\end\s*{\s*\1\s*}', re.DOTALL)
        return pattern.sub(self._fix_table_content, content)

    def _fix_table_content(self, match: re.Match) -> str:
        """Fix content within table environments"""
        env_type, table_content = match.groups()
        fixed_content = table_content.replace(r'\\', r'\\newline')
        return f"\\begin{{{env_type}}}{fixed_content}\\end{{{env_type}}}"