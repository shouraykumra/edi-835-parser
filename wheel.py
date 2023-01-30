# Databricks notebook source
# MAGIC %sh python setup.py bdist_wheel 

# COMMAND ----------

pip install dist/edi_835_parser-1.6.0-py3-none-any.whl

# COMMAND ----------

pip show edi_835_parser

# COMMAND ----------


