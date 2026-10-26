# MLOps Basics

A small Python project that generates a sample CSV dataset and tracks the
dataset with [DVC](https://dvc.org/).

## Project structure

```text
mlops/
├── .dvc/                 # DVC configuration
├── src/
│   └── generate_data.py  # Sample dataset generator
├── data.dvc              # DVC metadata for the generated data/
├── requirements.txt
├── LICENSE
└── README.md
```

The generated `data/` directory and the local DVC storage directory `s3/` are
not committed to Git. `data.dvc` is the version-controlled pointer for the
dataset.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Generate the sample data

Run from the project root:

```powershell
python src\generate_data.py
```

This creates or replaces `data/sample_data.csv`.

## DVC

Install DVC if you need to fetch or publish the dataset:

```powershell
python -m pip install dvc
```

The DVC storage location is kept in the ignored `.dvc/config.local` file so a
machine-specific path is not committed to Git. Configure a remote for your
machine before using `dvc pull` or `dvc push`:

```powershell
dvc remote modify --local myremote url <YOUR_DVC_REMOTE_URL>
dvc pull
```

After regenerating data, review the change with `dvc status` and update the
tracked DVC metadata with `dvc add data` when appropriate.
