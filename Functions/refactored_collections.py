import random as rnd

DICT_KEYS = [
    'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p',
    'q', 'r', 's', 't',
    'u', 'v', 'w', 'x',
    'y', 'z'
]

def generate_dicts(num_dicts:int=3, num_keys: int=3):
    dicts = []

    for _ in range(num_dicts):
        num_keys = rnd.randint(1, 5)
        keys = rnd.sample(DICT_KEYS, num_keys)

        dicts.append({k: rnd.randint(0, 100) for k in keys})  # Assign random values (0–100)

    return dicts


def map_dicts(dicts: list):
    mapped_dict = {}

    # Iterate through each dictionary
    for i, d in enumerate(dicts):
        for key, value in d.items():
            # If key already exists, compare and keep the one with higher value
            if key in mapped_dict:
                if value > mapped_dict[key][0]:
                    mapped_dict[key] = (value, i)
            else:
                # New key, add to mapped_dict
                mapped_dict[key] = (value, i)

    return mapped_dict


def make_common_dict(dicts: list):
    mapped_dict = map_dicts(dicts)

    common_dict = {}

    for key, (value, index) in mapped_dict.items():
        count = sum(1 for d in dicts if key in d)

        if count > 1:
            # If key appears in multiple dicts, rename it with index of max-value dict (1-based index)
            common_dict[f"{key}_{index + 1}"] = value
        else:
            # Key appears only in one dict, keep as-is
            common_dict[key] = value

    return common_dict


if __name__ == "__main__":
    dicts = generate_dicts(5, 3)

    print("Generated dictionaries:")
    for i, d in enumerate(dicts, 1):
        print(f"Dict {i}: {d}")

    result_dict = make_common_dict(dicts)
    print("\nMerged dictionary:")
    print(result_dict)
