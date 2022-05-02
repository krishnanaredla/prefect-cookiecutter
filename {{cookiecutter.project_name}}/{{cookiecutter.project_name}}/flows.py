from prefect import Flow

from {{ cookiecutter.project_name }}.tasks import *

Flow_name = "{0}-flow".format("{{ cookiecutter.project_name }}")
with  Flow(name=Flow_name) as flow:
    # Code the flow

