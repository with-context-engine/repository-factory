OPTION_1 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 0,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 0,
    "with_sentry_logging": "0",
    "with_streamlit_app": "0",
    "with_typer_cli": "0",
    "with_ml_training": "0",
    "with_ml_inference": "0",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}