import arrow

import airplane

# Put the main logic of the task in the main function.
def main(params):
    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs

    start = arrow.now()
    email_run = airplane.email.message(
        email_resource="mail",
        sender=airplane.email.Contact(email="ameya@airplane.dev", name="Ameya"),
        recipients=[airplane.email.Contact(email="lee@airplane.dev", name="Lee")],
        subject="Greetings",
        message=":prayge:",
    )
    print(f"Running email took {arrow.now()-start}")

    start = arrow.now()
    sql_run = airplane.sql.query(
        sql_resource="db",
        query="SELECT name, email FROM users LIMIT 1",
    )
    print(f"Running sql took {arrow.now()-start}")


    start = arrow.now()
    rest_run = airplane.rest.request(
        rest_resource="website",
        method=airplane.rest.Method.GET,
        path="index",
    )
    print(f"Running rest took {arrow.now()-start}")

    return [
        {"namespace": "email", "name": "message", "status": email_run.status.value},
        {"namespace": "sql", "name": "query", "status": sql_run.status.value},
        {"namespace": "rest", "name": "request", "status": rest_run.status.value},
    ]
