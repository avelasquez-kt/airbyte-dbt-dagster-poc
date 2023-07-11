from setuptools import find_packages, setup

setup(
    name="orchestrator",
    packages=find_packages(exclude=["orchestrator_tests"]),
    install_requires=[
        "dagster",
        "dagster-airbyte",
        "dagster-dbt",
        "dagster-postgres",
        "dbt-core",
        "dbt-postgres",
        "psycopg2-binary"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)