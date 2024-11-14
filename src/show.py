from typing import Dict, List


def show_distribution(distribution: List[Dict[str, int]]) -> None:
    for i, allocation in enumerate(distribution):
        parts_allocated = ', '.join(f'{number} {part}(s)' for part, number in allocation.items())
        print(f'seamstress {i + 1}: {parts_allocated}')
