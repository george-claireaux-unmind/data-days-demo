from dagster import AssetIn, AssetKey, asset, file_relative_path
from dagstermill import define_dagstermill_asset
import pandas as pd
from sqlalchemy import create_engine


@asset(
        key_prefix="pandas_datasets",
        group_name="whisky",
        non_argument_deps={AssetKey(("dbt", "whisky_country_rollup"))}
)
def pandas_whisky_dataset():
    engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost/postgres')
    return pd.read_sql("select * from modelled.whisky_country_rollup", engine.connect())

whisky_viz_jupyter_notebook = define_dagstermill_asset(
    name="whisky_viz_jupyter",
    notebook_path=file_relative_path(__file__, "./notebooks/whisky_viz.ipynb"),
    ins={"data": AssetIn(("pandas_datasets", "pandas_whisky_dataset"))},
    key_prefix="jupyter",
    group_name="whisky",
)
