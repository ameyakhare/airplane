# Linked to https://app.airplane.so:5000/t/first_python_task [do not edit this line]

# Put the main logic of the task in the main function.
def main(params):
    print("parameters:", params)
    print("env:", os.environ)

    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    return [
        {"element": "hydrogen", "weight": 1.008},
        {"element": "helium", "weight": 4.0026}
    ]
