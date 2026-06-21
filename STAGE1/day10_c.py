data = {
    "duration": [
        20,
        40,
        60,
        80,
        100,
        1000
    ]
}
import pandas as pd
df = pd.DataFrame(data)

duration = df["duration"].describe().round(0)
print(duration)
