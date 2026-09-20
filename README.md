# Fiskus — incomplete AI experiment

A small experimental snapshot containing a generative-AI streaming implementation and Python dependency metadata.

**Status:** Legacy/incomplete; the checked-in files do not form a runnable Python application.

## What is actually present

- `app.py` contains TypeScript imports and a `streamTherapyResponse` export using `@google/genai`, despite its Python extension.
- `requirements.txt` lists Streamlit and the Python Google generative-AI library.
- `.devcontainer/devcontainer.json` provides development-container configuration.

## Setup limitation

Do not assume `streamlit run app.py` works: the file is not Python. Recover the intended source layout and runtime before installing or deploying this project. Similar conversational-AI work is present in `psycholog`; this snapshot is not presented as an independent finished product.

## Maintenance direction

Choose one runtime, restore the missing application structure and test a minimal response flow with synthetic inputs. Provider credentials belong outside source control and private keys must stay outside browser bundles. This experiment is not a clinical or diagnostic tool.
