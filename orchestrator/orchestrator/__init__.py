from dagster import (
    Definitions,
    ScheduleDefinition,
    load_assets_from_package_module,
)

from dagster_airbyte import AirbyteResource
from dagster_dbt import DbtCliClientResource

from .assets import airbyte_assets
from .utils.constants import AIRBYTE_CONFIG, DBT_CONFIG, POSTGRES_CONFIG

resources = {
    "airbyte": AirbyteResource(**AIRBYTE_CONFIG),    
    "dbt": DbtCliClientResource(**DBT_CONFIG)
}

defs = Definitions(assets=load_assets_from_package_module(assets), resources=resources)
