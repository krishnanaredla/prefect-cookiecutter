from {{ cookiecutter.project_name }}.flows import flow

if __name__ == "__main__":
    flow.register(project_name="{{ cookiecutter.prefect_project }}")