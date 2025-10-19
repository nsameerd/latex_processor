from processors.file_handler import FileHandler
from processors.matrix_processor import MatrixProcessor
from processors.table_processor import TableProcessor
from processors.text_processor import TextProcessor
from processors.question_processor import QuestionProcessor
from pathlib import Path

def process_latex_file(input_path: Path, output_path: Path):
    """Main processing pipeline"""
    # Initialize processors
    processors = [
        TextProcessor(),
        TableProcessor(),
        MatrixProcessor(),
        QuestionProcessor()
    ]
    
    # Read input file
    file_handler = FileHandler(input_path)
    content = file_handler.read()
    
    # Apply all processors
    for processor in processors:
        content = processor.process(content)
    
    # Write output file
    file_handler.write(output_path, content)

if __name__ == "__main__":
    input_file = Path("input.tex")
    output_file = Path("processed_input.tex")
    process_latex_file(input_file, output_file)