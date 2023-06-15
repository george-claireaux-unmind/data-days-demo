from dagster_airbyte import (
    AirbyteConnection,
    AirbyteSyncMode,
    AirbyteManagedElementReconciler,
    AirbyteDestinationNamespace,
    airbyte_resource,
    load_assets_from_connections,
)
from dagster_airbyte.managed.generated.sources import WhiskyHunterSource
from dagster_airbyte.managed.generated.destinations import PostgresDestination


airbyte_instance = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000",
        "username": "airbyte",
        "password": "password",
    }
)

# Source
whisky_source = WhiskyHunterSource(
    name="whisky-source"
)
# Destination
postgres_destination = PostgresDestination(
    name="postgres-dest",
    host="localhost",
    port=5432,
    username="postgres",
    password="mysecretpassword",
    database="postgres",
    schema="public",
    ssl_mode=PostgresDestination.Disable(),
)
# Connection
whisky_to_postgres_connection = AirbyteConnection(
    name="WhiskyAPI to Postgres",
    source=whisky_source,
    destination=postgres_destination,
    stream_config={
        "distilleries_info": AirbyteSyncMode.full_refresh_overwrite(),
        "auctions_data": AirbyteSyncMode.full_refresh_overwrite(),
        "auctions_info": AirbyteSyncMode.full_refresh_overwrite(),
    },
    normalize_data=True,
    destination_namespace=AirbyteDestinationNamespace.DESTINATION_DEFAULT,
)

# Reconciler
airbyte_reconciler = AirbyteManagedElementReconciler(
    airbyte=airbyte_instance,
    connections=[whisky_to_postgres_connection],
)

# Assets
airbyte_assets = load_assets_from_connections(
    airbyte=airbyte_instance,
    connections=[whisky_to_postgres_connection],
    key_prefix="postgres"
)
