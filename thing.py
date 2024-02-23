import json
import typer

app = typer.Typer()

@app.command()
def open_json_string(json_data: str):
    """Opens a JSON string and returns a dictionary."""
    file_thing = json.loads(json_data)
    print(file_thing['github_repository_id'], file_thing) 

if __name__ == "__main__":
    app()