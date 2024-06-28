import math
import json
import requests
import pandas as pd


class DrugInteraction:
    def __init__(self, drug_name, drug_url, interaction_description):
        self._drug_name = drug_name
        self._drug_url = drug_url
        self._interaction_description = interaction_description

    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value

    @property
    def drug_url(self):
        return self._drug_url

    @drug_url.setter
    def drug_url(self, value):
        self._drug_url = value

    @property
    def interaction_description(self):
        return self._interaction_description

    @interaction_description.setter
    def interaction_description(self, value):
        self._interaction_description = value

    def __repr__(self):
        return f"DrugInteraction(drug_name={self.drug_name}, drug_url={self.drug_url}, interaction_description={self.interaction_description})"


class DrugInteractionResponse:
    def __init__(self, draw, records_total, records_filtered, data):
        self.draw = draw
        self.records_total = records_total
        self.records_filtered = records_filtered
        self.data = [DrugInteraction(*self.parse_interaction(entry)) for entry in data]

    def parse_interaction(self, entry):
        try:
            if 'href' in entry[0]:
                drug_url = entry[0].split('href="')[1].split('">')[0]
                drug_name = entry[0].split('">')[1].split('</a>')[0]
            else:
                drug_url = "Unknown"
                drug_name = entry[0]
        except IndexError:
            drug_url = "Unknown"
            drug_name = "Unknown"

        interaction_description = entry[1]
        return drug_name, drug_url, interaction_description

    def __repr__(self):
        return (f"DrugInteractionResponse(draw={self.draw}, records_total={self.records_total}, "
                f"records_filtered={self.records_filtered}, data={self.data})")

    def print_interactions(self):
        interactions = []
        for interaction in self.data:
            interactions.append((interaction.drug_name, interaction.drug_url, interaction.interaction_description))
        return interactions


def call_api():
    read_csv = pd.read_csv(r'C:\Users\gtush\Desktop\NotScrap\not_scrap_data.csv')
    entries = [927, 1110, 1305, 601, 678, 840, 876]
    header = {
        'Cookie': '_hjSessionUser_191585=eyJpZCI6IjFjYjQwMzhhLWY1MmMtNTQ0Ni05MDViLWFlMTE0YzE4OGJlZCIsImNyZWF0ZWQiOjE3MTk0ODY1NTEwMjksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_191585=eyJpZCI6IjdhMGYzYTMxLTEyMmMtNDRiYi1hNTFlLTE3ZDRjNTc0YzU0YSIsImMiOjE3MTk0ODY1NTEwMzEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __adroll_fpc=f776830d750ce97f9e7f77a74be9be0f-1719486551611; _ga=GA1.1.1190176613.1719486553; cookieyes-consent=consentid:OFREQkRXQTk2cHI2T0RseXBmbkxoblRZcGRzTnZwTm0,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _clck=1vmek86%7C2%7Cfmz%7C0%7C1639; _gcl_au=1.1.1547361869.1719486555; __hstc=49600953.b9644f0fc178704f89df98fef3273f4f.1719486555548.1719486555548.1719486555548.1; hubspotutk=b9644f0fc178704f89df98fef3273f4f; __hssrc=1; remember_public_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3pOakkzTXpaZExDSWtNbUVrTVRFa1dXVkhSVmx4V1haU1pFSTVTbU5oZEZob09XSnZMaUlzSWpFM01UazBPRFkyTmpNdU56TXdOVE0xTXlKZCIsImV4cCI6IjIwMjQtMDctMTFUMTE6MTE6MDMuNzMwWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl9wdWJsaWNfdXNlcl90b2tlbiJ9fQ%3D%3D--8289dde4d86a6daa434775efb671d1291a7ac2e0; __ar_v4=FAPGZQH4LBBKDJ7BEHFFXV%3A20240627%3A8%7CTAP76L6PNZHKTLZBWZQUKO%3A20240627%3A8%7CDA674JDALNFITKMDU7VWN6%3A20240627%3A8; _clsk=htob10%7C1719488580996%7C12%7C1%7Ct.clarity.ms%2Fcollect; _ga_DDLJ7EEV9M=GS1.1.1719486550.1.1.1719488579.60.0.0; __hssc=49600953.8.1719486555549; _omx_drug_bank_session=6KKuz87o7Tvnnh0B2nE2GuHnx3bD1dIJsXhqFCO79lNbCw4uF0x%2FJZQstt4z5lmTefMUGFpsQMq2OtFUFXfJz2Upyont2Utw36%2BFHkG6ycU0ymM5lMrS8YyBKEA54onkmgE5CK4KW%2F5vtBHvtO0VzcZeMJG9MAt1YwNcI%2FyvG2No544M040foz7v7Cz6UgzLybf3Yzek82HIlIuDsDbP3ucdmzqzi0yWOvlsxXnLnJSyC2ePxVS2eYM5LCJK2dxcMgMUjhi1DTkm%2BXM3YtIAZd04UDaNrwPFdUKwegkhQ8WnwQS%2F4JPeqMHiYoJnhJ7RlQvDa1CAoMnLzMn365Cis4A%2Bib%2BE5EiaIeWUKl6bZJ4B850J851nSD9N1MTteL8VcZbkIasIJok7EL5lhN9HZysSevu5RFSRqWlkfwu3UF4N6C8v3XYAwaC7sEb%2FKfPUjI7XYI9HeoE6PmsGr2P6qNGGjiWgfaFAhasN4vcgiR%2B2tCfqdIUyaNCFVNYJHWTXOrL8L%2BwmmMWc%2FRc7Scaj0ABHaHj1ahYw9ByhhS%2BsHvnQ2rsd27ZUzt5%2B9oWzYra5foNW2semHHr5FQ%3D%3D--2ZZEb3auIHMwd9gw--8k1t%2F2mdpe7%2Bcj3V8W5lMw%3D%3D'  # Placeholder for the actual cookie
    }

    for index, entry in enumerate(entries):
        n_page = entry / 100
        number_of_pages = math.ceil(n_page)
        print(number_of_pages)
        start_count = 1
        drug_name_list = []
        drug_url_list = []
        interaction_list = []
        base_drug_list = []
        base_url_list = []

        for page in range(number_of_pages):
            if page > 1:
                start_count = page * 100 + 1

            url = read_csv.at[index, 'Drug URL'] + "/drug_interactions.json"
            params = {
                'group': 'approved',
                'length': 100,
                'draw': page,
                'start': start_count
            }

            response = requests.get(url=url, headers=header, params=params)
            response_dict = response.json()

            drug_interaction_response = DrugInteractionResponse(
                draw=response_dict["draw"],
                records_total=response_dict["recordsTotal"],
                records_filtered=response_dict["recordsFiltered"],
                data=response_dict["data"]
            )

            interactions = drug_interaction_response.print_interactions()
            print(len(interactions))
            for drug_name, drug_url, interaction_description in interactions:
                drug_name_list.append(drug_name)
                drug_url_list.append("https://go.drugbank.com"+drug_url)
                interaction_list.append(interaction_description)
                base_drug_list.append(read_csv.at[index, 'Name'])
                base_url_list.append(read_csv.at[index, 'Drug URL'])

        df = pd.DataFrame({
            "Drug": drug_name_list,
            "Interaction": interaction_list,
            "URL": drug_url_list,
            "Base Drug": base_drug_list,
            "Base_Drug URL": base_url_list
        })
        drug_url = read_csv.at[index, 'Drug URL'].split("/")[-1]
        df.to_csv(fr'C:\Users\gtush\Desktop\Collection_2\{drug_url}.csv', index=False)
        print(fr'C:\Users\gtush\Desktop\Collection_2\{drug_url}.csv')


if __name__ == '__main__':
    call_api()
