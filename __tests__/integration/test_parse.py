import pytest

from pathlib import Path
from parse import parse_inputs
import json

@pytest.mark.parametrize(
    "input_file_name",
    [
        "01-choice.json",
    ],
)
def test_parse_inputs(input_file_name):
    """Test the parse_inputs function."""
    # Arrange
    input_file = Path(__file__).parents[2] / "expected_input" / input_file_name
    github_repository = "ajay-bhargava/poetry-cookiecutter"
    github_repository_owner = "ajay-bhargava"

    expected_output = {
        'package_name': 'Poetry Cookiecutter',
        'author_name': 'Ajay Bhargava',
        'package_description': 'This is a package that will help me create a pydantic repository for the Whispr Class',
        'author_email': 'bhargava.ajay@gmail.com',
        'package_url': 'https://github.com/ajay-bhargava/poetry-cookiecutter',
        'python_version': '3.11',
        'docker_image': 'python:$PYTHON_VERSION-slim',
        'development_environment': 'simple',
        'with_fastapi_api': 0,
        'with_jupyter_lab': 1,
        'with_pydantic_typing': 0,
        'with_sentry_logging': '0',
        'with_streamlit_app': '0',
        'with_typer_cli': '0',
        'with_ml_training': '0',
        'with_ml_inference': '0',
        'continuous_integration': 'GitHub',
        'docstring_style': 'Numpy'
    }

    # Act
    result = parse_inputs(
        input_file, 
        github_repository, 
        github_repository_owner
    )

    # Assert    
    assert result == print(json.dumps(expected_output))

        
