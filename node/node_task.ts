import airplane from "airplane"
import { resources } from "airplane";

// Put the main logic of the task in this function.
export default async function(params) {
  // You can return data to show outputs to users.
  // Outputs documentation: https://docs.airplane.dev/tasks/outputs

  const run = await airplane.sql.query(
    new resources.PostgreSQLResource("res20220113z07xszb"),
    "SELECT company_name, total_dollars FROM accounts LIMIT 1",
  )
  console.log(run.status)
  console.log(process.env.AIRPLANE_TOKEN);

  return [
    {"environment": process.env.AIRPLANE_ENV_SLUG, "run_status": run.status, "runtime": process.env.AIRPLANE_RUNTIME},
  ];
}
