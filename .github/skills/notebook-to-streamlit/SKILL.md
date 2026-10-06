\---

name: notebook-to-streamlit

description: Convert the logic in Assignment\_1.ipynb into a Streamlit app (app.py) that recommends Rosa's best delivery promise. Use when building or updating the Streamlit app from the notebook.

\---



\# Notebook to Streamlit



\## Goal

Build `app.py`, a Streamlit app that helps Rosa choose the best promised delivery time for a zone and time block, using the logic from `Assignment\_1.ipynb`.



\## What to take from the notebook

\- Copy the `cost\_late` and `best\_promise` functions exactly as written. `best\_promise` calls `cost\_late`, so both are needed.

\- Import `ZONES`, `TIME\_BLOCKS`, `COSTS`, and `delivery\_times` from `starter`.



\## What to leave out

\- The `!pip install` cell (packages are installed through `requirements.txt` instead).

\- All `print()` test lines.

\- The Part I functions and rankings.

\- All markdown text.



\## App inputs

\- A dropdown to select a zone from `ZONES`.

\- A dropdown to select a time block from `TIME\_BLOCKS`.

\- Number inputs for the promise range: start, end, and step (in minutes). Build the promise list with `range`, making sure the end value is included.

\- Number inputs for the profit margin per order, churn per late order, and refund per late order, with defaults from `COSTS`.



\## On button click

\- Build a costs dictionary from the inputs, using the same keys as `COSTS` (`'refund'`, `'churn\_orders'`, `'margin'`).

\- Call `best\_promise` with the selected zone, time block, promise list, and costs.

\- Display the recommended promise.

\- If the recommended promise is 0, show a message that no promise in the range is profitable.



\## Requirements

\- Create `requirements.txt` with `streamlit`, `numpy`, and `git+https://github.com/zhouy185/rosa-starter.git`.

