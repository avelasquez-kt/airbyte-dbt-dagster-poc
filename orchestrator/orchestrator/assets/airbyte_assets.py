from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition
)

from dagster_airbyte import (
    AirbyteResource, 
    load_assets_from_airbyte_instance
)

airbyte_instance = AirbyteResource(
    host="host.docker.internal",
    port="8000",
    username="airbyte",
    password="password",
)

airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)
