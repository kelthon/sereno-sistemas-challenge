from typing import Dict, List

def seamstress_work_distribution(
    seamstresses: List[Dict[str, int]],
    piece_parts: Dict[str, int],
    avaliable_time: int
) -> List[Dict[str, int]]:
    distribution = [{part: 0 for part in piece_parts} for st in seamstresses]

    for part_name, part_number in piece_parts.items():
        allocation = 0
        
        seamstresses.sort(key= lambda seamstress: seamstress[part_name])

        for seamstress in seamstresses:
            if part_number <= 0:
                break
            
            index = seamstresses.index(seamstress)
            max_parts = (avaliable_time - allocation) // seamstress[part_name]
            allocation = min(max_parts, part_number)
            distribution[index][part_name] += allocation
            
            part_number -= allocation
    
    return distribution


def show_distribution(distribution: List[Dict[str, int]]) -> None:
    for i in range(len(distribution)):
        j = 0
        allocation = ''
        
        for part_name, part_number in distribution[i].items():
            if j != 0:
                allocation = f'{allocation}, {part_number} {part_name}(s)'
            else:
                allocation = f'{part_number} {part_name}(s)'
                j += 1

        print(f'seamstress {i}: {allocation}')

if __name__ == '__main__':
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
        {'sleeve': 12, 'collar': 10, 'button': 8},
        {'sleeve': 15, 'collar': 8, 'button': 8},
        {'sleeve': 9, 'collar': 7, 'button': 10},
        {'sleeve': 9, 'collar': 12, 'button': 10},
    ]

    pieces = {
        'sleeve': 150,
        'collar': 150,
        'button': 150,
    }

    avaliable_time = 180

    show_distribution(seamstress_work_distribution(seamstresses, pieces, avaliable_time))
