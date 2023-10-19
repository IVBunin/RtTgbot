from requests import get 
from bs4 import BeautifulSoup as bs
import pandas as pd
 

aplication  =  get("https://192.168.0.1")

print(aplication.status_code)

