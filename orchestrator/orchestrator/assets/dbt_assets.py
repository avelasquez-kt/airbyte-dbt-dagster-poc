from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    with_resources
)

from dagster_dbt import load_assets_from_dbt_project
from ..utils.constants import DBT_CONFIG

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_CONFIG["project_dir"], profiles_dir=DBT_CONFIG["profiles_dir"]
)
