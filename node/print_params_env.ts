export default async function(params) {
  console.log(params);

  return [
    {
      "environment": process.env.AIRPLANE_ENV_SLUG,
      "airplane_resources_version": process.env.AIRPLANE_RESOURCES_VERSION,
      "airplane_resources": process.env.AIRPLANE_RESOURCES
    },
  ];
}
