from datetime import datetime

import requests

TOKEN = "s2jkl2l1n3af14v9asd8fa12fv9fa8s7jh12u3o0d"
USERNAME = "wajeehulhassan"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# #
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response)
ID="graph1"
habit_name="Cycling "
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_prams = {
    "id": ID,
    "name": habit_name,
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_prams, headers=headers)
# print(response.text)

pixel_endpoint=f"{graph_endpoint}/{ID}"
today=datetime.now()

pixel_params={
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.1",
}
# pixel_response=requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_response.text)

#Pixel Updating using put
date_for_update="20220723"
updating_endpoint=f"{pixel_endpoint}/{date_for_update}"
update_params={
    "quantity": "12.3"
}
# update_response=requests.put(url=updating_endpoint,json=update_params,headers=headers)
# print(update_response.text)

#deleteing a pixel

date_for_deleting="20220723"
deleting_endpoint=f"{pixel_endpoint}/{date_for_update}"
deleting_response=requests.delete(url=deleting_endpoint,headers=headers)
print(deleting_response)
