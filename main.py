import requests
from bs4 import BeautifulSoup
import pandas as pd
from companies import urls, html_tags

headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/84.0.4147.105 Safari/537.36'}

all = []
for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')

        company_tags = html_tags["company"]
        company = soup.find(company_tags[0], {company_tags[1]: company_tags[2]}).text


        price_tags = html_tags["price"]
        price = soup.find(price_tags[0], {price_tags[1]: price_tags[2]}).text


        change_tags = html_tags["change"]
        change = soup.find(change_tags[0], {change_tags[1]: change_tags[2]}).text


        volume_tags = html_tags["volume"]
        volume = soup.find(volume_tags[0], {volume_tags[1]: volume_tags[2]}).text

        year_change_tags = html_tags["year_change"]
        year_change = soup.find(year_change_tags[0], {year_change_tags[1]: year_change_tags[2]}).text

        p_e_ratio_tags = html_tags["p_e_ratio"]
        p_e_ratio = soup.find(p_e_ratio_tags[0], {p_e_ratio_tags[1]: p_e_ratio_tags[2]}).text

        eps_tags = html_tags["eps"]
        eps = soup.find(eps_tags[0], {eps_tags[1]: eps_tags[2]}).text


        stock_row = [company, price, change, volume, year_change, p_e_ratio, eps]

        all.append(stock_row)


    except AttributeError:
        print("Change the Element id")

print(all)
column_names = ["Company", "Price", "Change", "Volume", "1-Year Change", "P/E Ratio", "EPS"]
df = pd.DataFrame(columns=column_names)
print(df)

for value in all:
    index = 0

    df.loc[index] = value
    df.index = df.index + 1
df = df.reset_index(drop=True)
df.to_excel('stocks.xlsx')
