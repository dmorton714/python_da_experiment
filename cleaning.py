import pandas as pd
import numpy as np


def cleaning_data(df):
    categories = {
        'nintendo': ['3ds', 'dsiw', 'dsi', 'ds', 'wii', 'wiiu', 'ns', 'gb', 'gba', 'nes', 'snes', 'gbc', 'n64', 'vb', 'gc', 'vc','ww'], # noqa
        'pc': ['linux', 'osx', 'pc', 'arc', 'all', 'fmt', 'c128', 'aco'],
        'xbox': ['x360', 'xone', 'series', 'xbl', 'xb', 'xs'],
        'sony': ['ps', 'ps2', 'ps3', 'ps4', 'ps5', 'psp', 'psv', 'psn', 'cdi'],
        'mobile': ['ios', 'and', 'winp', 'ngage', 'mob'],
        'sega': ['gg', 'msd', 'ms', 'gen', 'scd', 'sat', 's32x', 'dc'],
        'atari': ['2600', '7800', '5200', 'aj', 'int'],
        'commodore': ['amig', 'c64', 'cd32'],
        'other': ['ouya', 'or', 'acpc', 'ast', 'apii', 'pce', 'zxs', 'lynx', 'ng', 'zxs', '3do', 'pcfx', 'ws', 'brw', 'cv', 'giz', 'msx', 'tg16', 'bbcm'] # noqa
    }

    # Step 2: Flatten categories into a single list
    all_items = []
    for sublist in categories.values():
        for item in sublist:
            all_items.append(item)

    # Step 3: Check for missing items
    all_items_lower = [item.lower().strip() for item in all_items]
    unique_values_lower = set(df['console'].str.lower().str.strip().unique())
    missing_items = set(all_items_lower) - unique_values_lower

    if missing_items:
        print(f"Missing items: {missing_items}")
    else:
        print("All items are covered.")

    # Step 4: Create conditions and values for np.select
    conditions = []
    for items in categories.values():
        conditions.append(df['console'].isin(items))

    values = list(categories.keys())

    # Step 5: Assign console manufacturers
    df['console_mfg'] = np.select(conditions, values, default='unknown')

    return df