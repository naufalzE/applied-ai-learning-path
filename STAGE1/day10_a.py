data1 = {
    "stage": [
        "Stage 1",
        "Stage 1",
        "Stage 2",
        "Stage 3",
        "Stage 3"
    ],
    "duration": [
        100,
        50,
        75,
        120,
        80
    ]
}

import pandas as pd

data = pd.DataFrame(data1)
print(data.head())

grup = data.groupby("stage")["duration"].sum()
print(grup)