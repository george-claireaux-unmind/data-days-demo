from dagster import (
    AssetSelection,
    Definitions,
    define_asset_job,
    file_relative_path,
)
from dagster._utils import file_relative_path
from dagster_dbt import dbt_cli_resource, load_assets_from_dbt_project
from dagstermill import ConfigurableLocalOutputNotebookIOManager

from .assets.airbyte import airbyte_assets
from .assets.jupyter import pandas_whisky_dataset, whisky_viz_jupyter_notebook

DBT_PROJECT_DIR = file_relative_path(__file__, "../data_stack_dbt")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROJECT_DIR, key_prefix="dbt"
)

update_viz_job = define_asset_job("update_whisky_viz", selection=AssetSelection.all())

defs = Definitions(
    assets=[airbyte_assets, pandas_whisky_dataset, whisky_viz_jupyter_notebook] + dbt_assets,
    resources={
        "dbt": dbt_cli_resource.configured(
            {
                "project_dir": DBT_PROJECT_DIR,
                "profiles_dir": DBT_PROJECT_DIR,
            }
        ),
        "output_notebook_io_manager": ConfigurableLocalOutputNotebookIOManager()
    },
    jobs=[update_viz_job],
    # could easily add a schedule too that triggers the viz job on a cron
    # schedules=[update_viz_schedule],
)
