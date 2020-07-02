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
    frame = pd.DataFrame(
        np.arange(12).reshape((4, 3)),
        index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
        columns=[["Ohio", "Ohio", "Colorado"], ["Green", "Red", "Green"]],
    )

    frame.index.names = ["key1", "key2"]
    frame.columns.names = ["state", "color"]
    print(frame)


if __name__ == "__main__":
    main()
