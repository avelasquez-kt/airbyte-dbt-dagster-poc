from dagster._utils import file_relative_path
from dagster_postgres.utils import get_conn_string

PG_DESTINATION_CONFIG = {
    "username": "demo_user",
    "password": "password",
    "host": "host.docker.internal",
    "port": 5432,
    "database": "postgres",
}

AIRBYTE_CONFIG = {"host": "host.docker.internal", "port": "8000"}
DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt_project")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../dbt_project/config")
DBT_CONFIG = {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}

POSTGRES_CONFIG = {
    "con_string": get_conn_string(
        username=PG_DESTINATION_CONFIG["username"],
        password=PG_DESTINATION_CONFIG["password"],
        hostname=PG_DESTINATION_CONFIG["host"],
        port=str(PG_DESTINATION_CONFIG["port"]),
        db_name=PG_DESTINATION_CONFIG["database"],
    )
}
