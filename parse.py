import json
import typer
from pydantic import BaseModel, validator
from typing import Optional
import re

app = typer.Typer()

#TODO Needs additional logic for email and package description while also 
# handling the case where number is found in these fields.
def extract_issue_preferences(json_data: str):
    """
    Extracts issue preferences from a JSON string provided as an argument.
    """
    try:
        # Load the JSON data into a dictionary
        data_dict = json.loads(json_data)

        # Iterate over the dictionary values
        for value in data_dict.values():
            # Check if the value contains digits
            if any(char.isdigit() for char in value):
                # Extract and return the number
                return ''.join(filter(str.isdigit, value))
        typer.echo("No number found in the JSON.")
    except json.JSONDecodeError:
        typer.echo("Invalid JSON format.")

class GithubConfig(BaseModel):
    package_name: str
    author_name: str

    @staticmethod
    def convert_values(v):
        if isinstance(v, str):
            # Convert snake_case and kebab-case to Regular String
            return re.sub(r'[_-]', ' ', v).title()
        return v

    @validator('package_name', pre=True)
    def truncate_and_convert(cls, v):
        # Truncate string preceding "/"
        truncated = v.split('/', 1)[-1] if '/' in v else v
        # Apply convert_values
        return cls.convert_values(truncated)

    @validator('*', pre=True)
    def apply_convert_values(cls, v):
        return cls.convert_values(v)

def parse_inputs(json_data: str, github_repository: Optional[str] = None, github_repository_owner: Optional[str] = None):
    """Parses a JSON string and input variables and returns a dictionary according to Cruft Specifications."""

    # Create a dictionary with the input variables
    github_dictionary = {
        "package_name": github_repository,
        "author_name": github_repository_owner
    }

    # Create a CruftConfig object
    github_specifications = GithubConfig.model_validate(**github_dictionary).model_dump()

    # Find the number in the JSON data
    number = extract_issue_preferences(json_data)

    # Use the number to select from an array of dictionaries and 
    # merge with the github_specifications and return the result



    
    





if __name__ == "__main__":
    app()
