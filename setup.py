from setuptools import find_packages, setup

setup(
    name="data_days_demo",
    version="0.0.1",
    author_email="george.claireaux@unmind.com",
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    install_requires=[
        "dagster==1.3.9",
        "dagit==1.3.9",
        "dagster-dbt==0.19.9",
        "dagster-airbyte==0.19.9",
        "dagster-managed-elements==0.19.9",
        "dbt-core==1.5.1",
        "dbt-postgres==1.5.1",
        "notebook==6.5.4",
        "dagstermill==0.19.9",
        "pandas==2.0.2",
        "SQLAlchemy==2.0.16",
    ],
)
