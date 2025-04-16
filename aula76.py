
import requests
from bs4 import BeautifulSoup

url = "https://www.techtudo.com.br/"

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)