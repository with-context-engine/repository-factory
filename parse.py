import json
import typer
from typing import Optional
from src.poetry_cookiecutter.configurations import (
    OPTION_1
)
from src.poetry_cookiecutter.helpers import extract_issue_preferences, GithubConfig
import json

app = typer.Typer()

@app.command()
def parse_inputs(json_data: str, github_repository: Optional[str] = None, github_repository_owner: Optional[str] = None):
    """Parses a JSON string and input variables and returns a dictionary according to Cruft Specifications."""

    # Create a dictionary with the input variables
    github_dictionary = {
        "package_name": github_repository,
        "author_name": github_repository_owner
    }

    with open(json_data, 'r') as file:
        data_dictionary = json.load(file)

    # Create a CruftConfig object
    github_specifications = GithubConfig.model_validate(github_dictionary).model_dump()

    # Find the number in the JSON data
    number = int(extract_issue_preferences(json_data))

    if number == 1:
        result = {**github_specifications, **{
            "package_description": data_dictionary["repository_description"], 
            "author_email": data_dictionary['contact'],
            "package_url": f"https://github.com/{github_repository}"
        }, **OPTION_1}
        print(json.dumps(result))  # Convert the dictionary to a JSON string
    
if __name__ == "__main__":
    app()
