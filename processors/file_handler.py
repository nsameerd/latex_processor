from pathlib import Path

class FileHandler:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> str:
        """Read the input file"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, output_path: Path, content: str):
        """Write the processed content to output file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)