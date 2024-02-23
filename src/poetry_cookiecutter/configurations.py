# Python Repository:
OPTION_1 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 0,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 0,
    "with_sentry_logging": "0",
    "with_streamlit_app": "0",
    "with_typer_cli": "1",
    "with_ml_training": "0",
    "with_ml_inference": "0",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}

# Pydantic Repository:
OPTION_2 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 0,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 1,
    "with_sentry_logging": "0",
    "with_streamlit_app": "0",
    "with_typer_cli": "1",
    "with_ml_training": "0",
    "with_ml_inference": "0",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}

# Streamlit Repository:
OPTION_3 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 0,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 0,
    "with_sentry_logging": "0",
    "with_streamlit_app": "1",
    "with_typer_cli": "0",
    "with_ml_training": "0",
    "with_ml_inference": "0",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}

# FastAPI Repository:
OPTION_4 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 1,
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

# FastAPI with ML Inference
OPTION_5 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 1,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 0,
    "with_sentry_logging": "0",
    "with_streamlit_app": "0",
    "with_typer_cli": "0",
    "with_ml_training": "0",
    "with_ml_inference": "1",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}

# FastAPI with ML Training and Inference
OPTION_6 = {
    "python_version": "3.11",
    "docker_image": "python:$PYTHON_VERSION-slim",
    "development_environment": "simple",
    "with_fastapi_api": 1,
    "with_jupyter_lab": 1,
    "with_pydantic_typing": 0,
    "with_sentry_logging": "0",
    "with_streamlit_app": "0",
    "with_typer_cli": "0",
    "with_ml_training": "1",
    "with_ml_inference": "1",
    "continuous_integration": "GitHub",
    "docstring_style": "Numpy"
}