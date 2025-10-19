import re
from config.patterns import QUESTION_PATTERNS

class QuestionProcessor:
    def __init__(self):
        self.patterns = QUESTION_PATTERNS

    def process(self, content: str) -> str:
        """Process question/answer formatting"""
        for pattern, repl in self.patterns.items():
            content = re.sub(pattern, repl, content)
        return content