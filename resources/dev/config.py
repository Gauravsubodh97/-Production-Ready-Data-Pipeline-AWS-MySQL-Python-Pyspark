import os


key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "Wb4ULQJywpenLa2qq7l48sd5R9axyR0kXzAvQEpW+Dg="
aws_secret_key = "2Dqq/xrMZp6570atMaonyUwgc2GmvOr4NeFqtxQTIL4f9hr+ZttZ0XnbU1f/8Dm5"
bucket_name = "industry-data-engi-project"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "industry_project"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": '9667771241',
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id", "store_id", "product_name", "sales_date", "sales_person_id", "price", "quantity", "total_cost"]


# File Download location
local_directory = "D:\\Industry_pro_res_nd _DATA\\file_from_s3\\"
customer_data_mart_local_file = "D:\\Industry_pro_res_nd _DATA\\customer_data_mart\\"
sales_team_data_mart_local_file = "D:\\Industry_pro_res_nd _DATA\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "D:\\Industry_pro_res_nd _DATA\\sales_partition_data\\"
error_folder_path_local = "D:\\Industry_pro_res_nd _DATA\\error_files\\"
