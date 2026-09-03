# 3-11 / 3-4. Intentional Error (intentional_error.py)
# Intentionally trigger an IndexError by requesting an out-of-range index, then correct it.

motorcycles = ['honda', 'yamaha', 'Royal Enfield']

# Triggers an IndexError (List has 3 items, so max index is 2):
# print(motorcycles[3])  # IndexError: list index out of range

# Corrected code (Accessing valid indices: 0, 1, 2 or -1):
print(motorcycles[2])   # Output: Royal Enfield
print(motorcycles[-1])  # Output: Royal Enfield
