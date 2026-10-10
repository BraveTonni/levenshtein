# levenshtein

Console tool that finds the closest matches to a query word in a text file using Levenshtein distance.

## How it works

Every word of the file is compared with the query through a dynamic programming matrix: insertion, deletion and substitution each cost 1. The matrix is built in pandas, so the steps can be inspected visually. Words with the smallest distance (up to 3) are printed.

## Usage

Put the text into `file.txt`, then:

```bash
python main.py
```

Enter a word at the `>` prompt:

```
> hello
hello - 0
hell - 1
```

## Requirements

- Python 3.10+
- pandas
