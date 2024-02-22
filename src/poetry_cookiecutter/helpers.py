import typer
import json
from pydantic import BaseModel, field_validator
import re


def extract_issue_preferences(json_data: str):
    """
    Extracts issue preferences from a JSON string provided as an argument.
    """
    try:
        # Load the JSON data into a dictionary
        with open(json_data, 'r') as file:
            data_dict = json.load(file)

        # Iterate over the dictionary values
        for key, value in data_dict.items():
            if key not in ["contact", "repository_description"]:
                if any(char.isdigit() for char in value):
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

    @field_validator('package_name')
    def truncate_and_convert(cls, v):
        # Truncate string preceding "/"
        truncated = v.split('/', 1)[-1] if '/' in v else v
        # Apply convert_values
        return cls.convert_values(truncated)


    @field_validator('*')
    def apply_convert_values(cls, v):
        return cls.convert_values(v)