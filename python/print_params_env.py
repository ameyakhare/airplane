# Put the main logic of the task in the main function.
import os

def main(params):
    print(params)

    return [
        {
            "environment": os.environ.get("AIRPLANE_ENV_SLUG"),
            "airplane_resources_version": os.environ.get("AIRPLANE_RESOURCES_VERSION"),
            "airplane_resources": os.environ.get("AIRPLANE_RESOURCES"),
        },
    ]
