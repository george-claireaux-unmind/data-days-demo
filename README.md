# data-days-demo

### initial setup
Requirements
- Docker (engine running)
- Python (built with 3.11)

get Airbyte running
`sh run-airbyte.sh` (this script is just taken directly from the Airbyte repo as of v0.50.1)

spin up local postgres db as data destination
`docker run --name postgres-dest -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`

### Dagster - Airbyte reconcilliation commands
- need to run `pip install -e .` first.
- `dagster-airbyte check -m data_stack.assets.airbyte`
- `dagster-airbyte apply -m data_stack.assets.airbyte`

### Run Dagster
- `dagit`