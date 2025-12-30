from ucimlrepo import fetch_ucirepo 
import pandas as pd 
import numpy as np
import os 

class DataLoader:
  def __init__(self,filepath = 'data/raw'):
    self.filepath = filepath
  # fetch dataset 
  def fetch(self):
    """Fetch data from UCI Repo"""
    print("fetching Data...")
    return fetch_ucirepo(id=235)

  def convert_to_df(self):
    """ Return  data (as pandas dataframes) """
    try:
      individual_household_electric_power_consumption = self.fetch()
      df = individual_household_electric_power_consumption.data.features
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
    finally:
      return df

  def save_csv(self):
    try:
      df.to_csv('household_power_consumption.csv', index=False)
    except Exception as err:
      print(f"Error occurd while saving csv, {err=}")
  