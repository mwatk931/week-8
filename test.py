#I had AI make this test file, I wrote the sentences myself with AI assistance afterwards

import importlib.util
import random
from pathlib import Path


def load_sort_function(filename, function_name):
    file_path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(function_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load sorting module: {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


bubble_sort = load_sort_function("bubble_sort(arr).py", "bubble_sort")
insertion_sort = load_sort_function("insertion_sort(arr).py", "insertion_sort")
selection_sort = load_sort_function("selection_sort(arr).py", "selection_sort")

numbers = random.sample(range(1, 101), 20)
print("Original list:")
print(numbers)

bubble_list = numbers.copy()
insertion_list = numbers.copy()
selection_list = numbers.copy()

bubble_swaps = bubble_sort(bubble_list)
insertion_shifts = insertion_sort(insertion_list)
selection_swaps = selection_sort(selection_list)

print("\nBubble Sort:")
print(bubble_list)
print("Swaps:", bubble_swaps)

print("\nInsertion Sort:")
print(insertion_list)
print("Shifts:", insertion_shifts)

print("\nSelection Sort:")
print(selection_list)
print("Swaps:", selection_swaps)

print("\nComparison of swaps/shifts:")
print(f"Bubble Sort: {bubble_swaps} swaps")
print(f"Insertion Sort: {insertion_shifts} shifts")
print(f"Selection Sort: {selection_swaps} swaps")


''' Selection sort seems best because it takes 16 swaps vs 80 swaps/shifts for the other two. 
The other two are similar in that they both take 80 swaps/shifts. 
Insertion sort is a bit different in that it counts shifts instead of swaps, but the number is still 80. 
So selection sort is the best of the three. '''