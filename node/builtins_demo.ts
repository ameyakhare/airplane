import airplane from "airplane"

export default async function(params) {
  const emailRun = await airplane.email.message(
    "mail",
    {email: "ameya@airplane.dev", name: "Ameya"},
    [{email: "lee@airplane.dev", name: "Lee"}],
    "Greetings",
    ":prayge:",
  );

  const sqlRun = await airplane.sql.query(
    "db",
    "SELECT name, email FROM users LIMIT 1",
  );

  const restRun = await airplane.rest.request(
    "website",
    airplane.rest.Method.Get,
    "index",
  )

  return [
    {"namespace": "email", "name": "message", "status": emailRun.status},
    {"namespace": "sql", "name": "query", "status": sqlRun.status},
    {"namespace": "rest", "name": "request", "status": restRun.status},
  ];
}
