from pathlib import Path

import pandas as pd


def main() -> None:
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
    }
    dataframe = pd.DataFrame(data)
    dataframe.loc[len(dataframe)] = {"Name": "GF1", "Age": 20, "City": "City1"}
    dataframe.loc[len(dataframe)] = {"Name": "GF2", "Age": 30, "City": "City2"}

    output_path = Path("data") / "sample_data.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)
    print(f"CSV file saved to {output_path}")


if __name__ == "__main__":
    main()
