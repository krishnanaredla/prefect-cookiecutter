from {{ cookiecutter.project_name }}.flows import flow
from prefect.tasks.prefect.flow_run import (
        StartFlowRun
    )
from prefect.client import Client
import time
from typing import Dict

client = Client()

def getStatus(flow_id:str):
    finished = False
    while not finished:
        state = client.get_flow_run_info(flow_id).state
        print(state.message.strip('.'))
        time.sleep(10)
        finished = state.is_finished()
    return state

def main(params:Dict={}):
    flow_id = StartFlowRun(project_name="{{ cookiecutter.prefect_project }}",
            flow_name="{0}-flow".format("{{ cookiecutter.project_name }}"), parameters=params
        ).run()
    state = getStatus(flow_id)
    if state.is_successful():
        print("Completed Successfully")

if __name__ == "__main__":
    params = {}
    main(params)

