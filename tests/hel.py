import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from crawlers.scrapper import scrape_website
scrape_website("https://medium.com/@abhisadineni/why-zero-determinant-matrices-have-no-inverse-8f9ff3356ca0")