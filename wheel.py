# Databricks notebook source
# MAGIC %sh python setup.py bdist_wheel 

# COMMAND ----------

pip install dist/edi_835_parser-1.6.0-py3-none-any.whl

# COMMAND ----------

pip show edi_835_parser

# COMMAND ----------

import os
import zipfile

wheel_file = "/Workspace/Repos/shouray.kumra@onyxhealth.io/edi-835-parser/dist/edi_835_parser-1.6.0-py3-none-any.whl"
extracted_dir = "/Workspace/Repos/shouray.kumra@onyxhealth.io/edi-835-parser/dist"

with zipfile.ZipFile(wheel_file, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

os.listdir(extracted_dir)

# COMMAND ----------


