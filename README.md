# Installable Streamlit App
An example of packaging streamlit app.

## Project structure

```
project-root/
├── pyproject.toml
├── README.md
├── my_package/
│   ├── __init__.py
│   ├── my_module.py
│   ├── app.py
│   └── pages/
│       ├── page_1.py
│       └── page_2.py
```

## Install and run
In `pyproject.toml`, we set up an entry point to start the streamlit app,
so after running

```bash
pip install .
```

you can just start the app with the command

```bash
run-my-app
```
