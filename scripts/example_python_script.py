# Linked to https://app.airplane.dev/t/example_python_script [do not edit this line]

import os

# Put the main logic of the task in the main function.
def main(params):
    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    return [
        {"env": f"{os.environ['AIRPLANE_ENV']}"}
    ]
