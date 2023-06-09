"""
fill in

"""
from etl_jobs.configuration.api_raw_data.apis import Apis
from etl_jobs.util.extract.api import get_api_data
from etl_jobs.util.load.delta_spark import append_table, to_spark_data_frame
from etl_jobs.util.transform.gold_sales import transform_gold_sales
from etl_jobs.util.transform.polar_bear import transform_machine_bronze


def etl_data_api():
    """
    fill in
    """
    # spark = SparkSession \
    #    .builder \
    #    .appName("Schema App") \
    #    .getOrCreate()
    for api in Apis:
        raw = get_api_data(api.url, "56c5cc10")
        if api.name == "bronze_machine_raw":
            append_table(to_spark_data_frame(raw), "bronze_machine_raw", "dev")
            transformed = transform_machine_bronze(raw)
            append_table(to_spark_data_frame(transformed), "silver_machine_raw", "dev")
        if api.name == "bronze_sales":
            append_table(to_spark_data_frame(raw), "bronze_sales", "dev")
            transformed = transform_gold_sales(raw)
            append_table(to_spark_data_frame(transformed), "gold_sales", "dev")
        else:
            append_table(to_spark_data_frame(raw), api.name, "dev")


if __name__ == "__main__":
    etl_data_api()
