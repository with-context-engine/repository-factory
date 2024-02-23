[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/ajay-bhargava/poetry-cookiecutter) [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=735676626)

# Poetry Cookiecutter Template

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for scaffolding Python packages and apps. This repository is intended for organizations and super-user individuals who want to install some sence of order and rigor in code development. 

## 🍿 Demo

Starting development in My Package can be done with a single click by [opening My Package in GitHub Codespaces](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=450509735), or [opening My Package in a Dev Container](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/radix-ai/my-package).

## 🎁 Features

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote), and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- 🚚 Installing from and publishing to private package repositories and [PyPI](https://pypi.org/)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions) or [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)

## ✨ Using

### Creating a new Python project

#### 1. Clone this template
To create a new customization of this template, first press the big green button on the top right to clone this repository as your own. Then, create an issue by clicking on issues. You will be presented with a issue form template which will ask you to make one selection from a choice of 6 selections as follows:

#### 2. Create an issue
| No. | Category | Item | Jupyter | Additional Info |
|-----|----------|------|---------|-------|
| 1   | Python   | Package Repository        | :x: | `typer` is enabled by default with ability to push to PyPi |
| 2   | Python   | Pydantic Repository       | :x: | `mypy` Pydantic model checking is enabled by default with ability to push to PyPi |
| 3   | Streamlit| Streamlit Repository      | :x: | `streamlit` is enabled by default and ability to push to ECR is enabled |
| 4   | FastAPI  | FastAPI                   | :white_check_mark: | `fastapi` is enabled by default, with ability to push repo to ECR provided variables are supplied |
| 5   | FastAPI  | FastAPI with ML           | :white_check_mark: | `fastapi` is enabled by default, with ability to deploy a novel model from a foundation repository like [🤗](huggingface.co) to FastAPI endpoint from AWS API Gateway + AWS λ |
| 6   | FastAPI  | FastAPI with ML Training  | :white_check_mark: | `fastapi` is enabled by default, with ability to train the model. Data versioning is enabled via `DVC` and remote is configured. There is further ability to create FastAPI endpoint from AWS API Gateway + AWS λ  |

#### 3. Merge PR of the customization
Once the workflow has finished running, you can review the anticipated changes to your new customized repository by reviewing the PR. Once you are satisfied with the changes, you can merge the PR.