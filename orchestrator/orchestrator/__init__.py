from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
)

from dagster_dbt import DbtCliClientResource

from .assets import airbyte_assets
from .utils.constants import AIRBYTE_CONFIG, DBT_CONFIG, POSTGRES_CONFIG

defs = Definitions(
    assets=load_assets_from_package_module(airbyte_assets),
    resources={
        "dbt": DbtCliClientResource(**DBT_CONFIG)
    },
    schedules=[
        # update all assets once a day
        ScheduleDefinition(
            job=define_asset_job("all_assets", selection="*"), cron_schedule="@daily"
        ),
    ],
)
