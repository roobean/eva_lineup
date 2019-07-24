import pandas as pd
import numpy as np


def main():
    data = pd.Series(
        np.random.randn(9),
        index=[
            ["a", "a", "a", "b", "b", "c", "c", "d", "d"],
            [1, 2, 3, 1, 3, 1, 2, 2, 3],
        ],
    )
    print(data)
    print(data.index)
    print(data["d"])
    # selection from inner level
    print(data.loc[:, 2])
    print(data.unstack())

    # naming levels


if __name__ == "__main__":
    main()

