import random as rnd

# 1. Create a list of random number of dicts (from 2 to 10)
num_dicts = rnd.randint(2, 3)

dict_keys = [
    'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p',
    'q', 'r', 's', 't',
    'u', 'v', 'w', 'x',
    'y', 'z'
]

# Generate dictionaries with a random number of keys (from 2 to 10)
num_keys = rnd.randint(2, 5)
dicts = []

for _ in range(num_dicts):
    num_keys = rnd.randint(1, 5)
    keys = rnd.sample(dict_keys, num_keys)

    dicts.append({k: rnd.randint(0, 100) for k in keys})  # Assign random values (0–100)

# This dict will store key -> (value, index_of_dict_with_max_value)
common_dict = {}

# Iterate through each dictionary
for i, d in enumerate(dicts):
    for key, value in d.items():
        # If key already exists, compare and keep the one with higher value
        if key in common_dict:
            if value > common_dict[key][0]:  # Compare existing value
                common_dict[key] = (value, i)  # Update with new max value and its dict index
        else:
            # New key, add to common_dict
            common_dict[key] = (value, i)

result_dict = {}

for key, (value, index) in common_dict.items():
    count = sum(1 for d in dicts if key in d)

    if count > 1:
        # If key appears in multiple dicts, rename it with index of max-value dict (1-based index)
        result_dict[f"{key}_{index + 1}"] = value
    else:
        # Key appears only in one dict, keep as-is
        result_dict[key] = value

print("Generated dictionaries:")
for i, d in enumerate(dicts, 1):
    print(f"Dict {i}: {d}")

print("\nMerged dictionary:")
print(result_dict)
