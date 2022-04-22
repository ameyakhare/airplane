# Put the main logic of the task in the main function.
import os

def main(params):
    print("parameters: ", params)

    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    return [
        {"environment": os.environ.get("AIRPLANE_ENV_SLUG"), "message": "Testing in prod!"},
    ]
