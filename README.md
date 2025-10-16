# NMCC-project6
## Introduction
The goal of this project is to investigate how neurological memory consolidation methods might be applied to improve the long-term memory of artificial neural networks.

## Roadmap
### Phase 1: Demonstrate learning interference
Objective: Train a model on some task A, then train it on some task B, then evaluate whether it forgot how to perform task A (as we expect it will).

## Prerequisites
### Virtual environment
#### Notes on requirements
- In order to keep Python library versions consistent, a list is maintained in requirements.txt. If you use another library, please add it to requirements.txt.
- Please note that the ML libraries listed in requirements.txt should be CPU-only for universality. Directories named 'venv-gpu' will also be ignored by Git in case you want to create a GPU-accelerated environment for your particular setup, but ideally, all code should still work correctly under the common CPU-based version of the venv defined by requirements.txt.

#### Linux
To create and activate the virtual environment (assuming shell is bash and python is installed as python3):
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
You will need to run `source ./venv/bin/activate` in every new session to activate the environment.

#### Windows
To create and activate the virtual environment (assuming shell is normal command prompt and python is installed as python):
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
You will need to run `venv\Scripts\activate.bat` in every new session to activate the environment.