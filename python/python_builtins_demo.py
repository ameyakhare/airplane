from airplane import email
from airplane import slack
from airplane import sql
from airplane import rest

# Put the main logic of the task in the main function.
def main(params):
    # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs

    email_run = email.message(
        email_resource_id="res20220217zko5xnjjkzb",
        sender=email.Contact(email="ameya@airplane.dev", name="Ameya"),
        recipients=[email.Contact(email="ameya@airplane.dev", name="Ameya")],
        subject="Greetings",
        message=":prayge:",
    )

    sql_run = sql.query(
        sql_resource_id="res20220113z07xszb",
        query="SELECT name, email FROM users LIMIT 1",
    )

    rest_run = rest.request(
        rest_resource_id="res20220613zmq8mxihtm8",
        method=rest.Method.GET,
        path="index",
    )

    slack.message(
        channel_name="test-builtins",
        message=f'Email sent to {email_run.output["number_of_recipients"]}',
    )
    slack.message(
        channel_name="test-builtins",
        message=f'SQL Run Row: {sql_run.output["Q1"][0]}'
    )
    slack.message(
        channel_name="test-builtins",
        message=f'REST Output: {rest_run.output}',
    )

    return [
        {"namespace": "email", "name": "message", "status": email_run.status.value},
        {"namespace": "sql", "name": "query", "status": sql_run.status.value},
        {"namespace": "rest", "name": "request", "status": rest_run.status.value},
    ]
