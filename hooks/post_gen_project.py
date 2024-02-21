import os
import shutil

# Read Cookiecutter configuration.
package_name = "{{ cookiecutter.__package_name_snake_case }}"
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_sentry_logging = int("{{ cookiecutter.with_sentry_logging }}")
with_streamlit_app = int("{{ cookiecutter.with_streamlit_app }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
continuous_integration = "{{ cookiecutter.continuous_integration }}"
is_deployable_app = "{{ not not cookiecutter.with_streamlit_app|int }}" == "True"
is_api_endpoint = "{{not not cookiecutter.with_fastapi_api|int}}" == "True"
is_publishable_package = "{{ not cookiecutter.with_fastapi_api|int and not cookiecutter.with_streamlit_app|int }}" == "True"
is_ml_training_script = int("{{ cookiecutter.with_ml_training }}")
is_ml_inference_script = int("{{ cookiecutter.with_ml_inference }}")

# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    if os.path.exists(f"src/{package_name}/py.typed"):
        os.remove(f"src/{package_name}/py.typed")
    if os.path.exists(".github/dependabot.yml"):
        os.remove(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    if os.path.exists(f"src/serve/api.py"):
        os.remove(f"src/serve/api.py")
    if os.path.exists("__tests__/test_api.py"):
        os.remove("__tests__/test_api.py")

# Remove Sentry if not selected.
if not with_sentry_logging:
    if os.path.exists(f"src/{package_name}/sentry.py"):
        os.remove(f"src/{package_name}/sentry.py")
    if os.path.exists("__tests__/test_sentry.py"):
        os.remove("__tests__/test_sentry.py")

# Remove Streamlit if not selected.
if not with_streamlit_app:
    if os.path.exists(f"src/serve/app.py"):
        os.remove(f"src/serve/app.py")

# Remove ML training scripts if not selected.
if not is_ml_training_script:
    if os.path.exists(f"src/{package_name}/fit.py"):
        os.remove(f"src/{package_name}/fit.py")
    if os.path.exists("__tests__/test_train.py"):
        os.remove("__tests__/test_train.py")
    if os.path.exists(".github/workflows/train.yml"):
        os.remove(".github/workflows/train.yml")
    if os.path.exists(f"src/{package_name}/train"):
        shutil.rmtree(f"src/{package_name}/train")

# Remove ML inference scripts if not selected.
if not is_ml_inference_script:
    if os.path.exists(f"src/{package_name}/deploy.py"):
        os.remove(f"src/{package_name}/deploy.py")
    if os.path.exists(".github/workflows/endpoint.yml"):
        os.remove(".github/workflows/endpoint.yml")
    if os.path.exists("src/serve/package.json"):
        os.remove("src/serve/package.json")
    if os.path.exists("src/serve/requirements.txt"):
        os.remove("src/serve/requirements.txt")
    if os.path.exists("src/serve/serverless.yml"):
        os.remove("src/serve/serverless.yml")
    if os.path.exists(f"src/{package_name}/deploy-inference.py"):
        os.remove(f"src/{package_name}/deploy-inference.py")
    if os.path.exists(f"src/{package_name}/deploy"):
        shutil.rmtree(f"src/{package_name}/deploy")

# Neither ML training nor inference is selected.
if not is_ml_training_script and not is_ml_inference_script:
    if os.path.exists(f"src/{package_name}/settings.py"):
        os.remove(f"src/{package_name}/settings.py")
    if os.path.exists(".github/workflows/serve.yml"):
        os.remove(".github/workflows/serve.yml")

# Remove Typer if not selected.
if not with_typer_cli:
    if os.path.exists(f"src/{package_name}/cli.py"):
        os.remove(f"src/{package_name}/cli.py")
    if os.path.exists("__tests__/test_cli.py"):
        os.remove("__tests__/test_cli.py")

# Remove Serve Directory if neither FastAPI nor Streamlit is selected.
if not with_fastapi_api and not with_streamlit_app:
    if os.path.exists(".github/workflows/serve.yml"):
        os.remove(".github/workflows/serve.yml")
    if os.path.exists("src/serve"):
        shutil.rmtree("src/serve")

if is_ml_inference_script and is_api_endpoint:
    if os.path.exists(".github/workflows/ship.yml"):
        os.remove(".github/workflows/ship.yml")
    if os.path.exists("src/serve/api.py"):
        os.remove("src/serve/api.py")
    if os.path.exists("src/serve/api-ml-inference.py"):
        os.rename("src/serve/api-ml-inference.py", "src/serve/api.py")

if is_ml_inference_script and is_api_endpoint and not is_ml_training_script:
    if os.path.exists(f"src/{package_name}/deploy"):
        shutil.rmtree(f"src/{package_name}/deploy")
    if os.path.exists(f"src/{package_name}/deploy-inference.py"):
        os.rename(f"src/{package_name}/deploy-inference.py", f"src/{package_name}/deploy.py")

if is_api_endpoint and not is_ml_inference_script:
    if os.path.exists("src/serve/api-ml-inference.py"):
        os.remove("src/serve/api-ml-inference.py")
    if os.path.exists(f"src/{package_name}/deploy-inference.py"):
        os.remove(f"src/{package_name}/deploy-inference.py")

if is_ml_training_script and is_ml_inference_script:
    if os.path.exists(f"src/{package_name}/deploy-inference.py"):
        os.remove(f"src/{package_name}/deploy-inference.py")

# Remove the continuous integration provider that is not selected.
if continuous_integration != "GitHub":
    if os.path.exists(".github/"):
        shutil.rmtree(".github/")
elif continuous_integration != "GitLab":
    if os.path.exists(".gitlab-ci.yml"):
        os.remove(".gitlab-ci.yml")

# Remove unused GitHub Actions workflows.
if continuous_integration == "GitHub":
    if not is_deployable_app and not is_api_endpoint:
        if os.path.exists(".github/workflows/ship.yml"):
            os.remove(".github/workflows/ship.yml")
    if not is_publishable_package:
        if os.path.exists(".github/workflows/publish.yml"):
            os.remove(".github/workflows/publish.yml")
