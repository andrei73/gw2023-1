import os
from typing import List
from collections import Counter

class Puzzle1:
    def __call__(self, file_name: str) -> int:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        try:
            with open(file_path, 'r') as file:
                input_data = file.read()
        except IOError:
            raise Exception('Failed to read input file.')

        groups = input_data.split("\n\n")
        group_counts = [
            len(set(group.replace("\n", "")))
            for group in groups if group.strip()
        ]
        
        return max(group_counts)

# Example usage
if __name__ == '__main__':
    puzzle = Puzzle1()
    result = puzzle('input.txt')
    print(result)
