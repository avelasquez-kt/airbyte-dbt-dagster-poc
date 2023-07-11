from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition
    # define_asset_job,
    # with_resources
)

from dagster_airbyte import (
    AirbyteResource, 
    load_assets_from_airbyte_instance
)

airbyte_instance = AirbyteResource(
    host="localhost",
    port="8000",
    username="airbyte",
    password="password",
)

airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)

# airbyte_job = define_asset_job(
#     "demo_job", AssetSelection.groups("demo_connection").upstream()
# )
