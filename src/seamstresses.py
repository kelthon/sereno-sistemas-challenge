from typing import Dict, List
from .show import show_distribution


def distribute_seamstress_work(
    seamstresses: List[Dict[str, int]],
    piece_parts: Dict[str, int],
    avaliable_time: int
) -> List[Dict[str, int]]:
    distribution = [{part: 0 for part in piece_parts} for _ in seamstresses]
    seamstress_avaliable_times = [avaliable_time for _ in seamstresses]

    for part_name, part_number in piece_parts.items():
        remaining_parts = part_number

        seamstresses.sort(key=lambda seamstress: seamstress[part_name])

        for i, seamstress in enumerate(seamstresses):
            if remaining_parts <= 0:
                break

            if seamstress_avaliable_times[i] <= 0:
                continue

            max_parts_for_seamstress = (seamstress_avaliable_times[i]) // seamstress[part_name]
            parts_to_allocate = min(max_parts_for_seamstress, remaining_parts)

            distribution[i][part_name] += parts_to_allocate
            time_spent = parts_to_allocate * seamstress[part_name]
            seamstress_avaliable_times[i] -= time_spent

            remaining_parts -= parts_to_allocate
    
    return distribution

if __name__ == '__main__':
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
        {'sleeve': 12, 'collar': 10, 'button': 8},
        {'sleeve': 15, 'collar': 8, 'button': 8},
        {'sleeve': 9, 'collar': 7, 'button': 10},
        {'sleeve': 9, 'collar': 12, 'button': 10},
    ]

    pieces = {
        'sleeve': 50,
        'collar': 50,
        'button': 50,
    }

    avaliable_time = 275

    show_distribution(distribute_seamstress_work(seamstresses, pieces, avaliable_time))
