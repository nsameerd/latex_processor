import re
from typing import Dict
from config.patterns import TEXT_REPLACEMENTS

class TextProcessor:
    def __init__(self):
        self.replacements = TEXT_REPLACEMENTS

    def process(self, content: str) -> str:
        """Process all text-related issues in the content"""
        for pattern, repl in self.replacements.items():
            content = re.sub(pattern, repl, content)
        return content