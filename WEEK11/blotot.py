import os
import csv
import time
import gspread
from googleapiclient.errors import HttpError
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCE_FOLDER = os.path.join(BASE_PATH, "RESOURCES")
SERVOCE_KEY = os.path.join(RESOURCE_FOLDER, "cmpebsese1-4demopzgs-9e89dcd63ffd.json")

credential = ServiceAccountCredentials.from_json_keyfile_name(SERVOCE_KEY, scopes=['https://www.googleapis.com/auth/spreadsheets'])
client = gspread.authorize(credential)

sheet_url = "https://docs.google.com/spreadsheets/d/1_cObDcQeKN-XJYAwENeUn6mbSPbGlib0a-jvUZ-qGwc/edit?gid=0#gid=0"

gs_instances = client.open_by_url(sheet_url)

sheet_instances = gs_instances.worksheet(0)

googlesheet_data_tab0 = sheet_instances.get_all_records()
print(googlesheet_data_tab0)



'''
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_FOLDER = os.path.join(BASE_PATH, "RESOURCES")
CSV_PATH = os.path.join(CSV_FOLDER, "AKONGCSV.csv")

print(CSV_PATH)

csv_data = []

with open(CSV_PATH, mode='r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_data.append(row)

print("------------------------------------------------------------")
print(csv_data)
print(csv_data[2])



csv_new_data = []
for row in csv_data:
    csv_new_data.append([row[1], row[5]])

with open(os.path.join(CSV_FOLDER, "WRITE_CSV.csv"), mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_new_data)
'''



'''
print(os.getcwd())
print(os.listdir(os.getcwd()))
#os.makedirs(os.getcwd() + "/bagong new")
#os.makedirs(os.path.join(os.getcwd(), "bagong newer"))
#os.makedirs(os.path.join(os.path.join(os.getcwd(), "bagong newer"), "bagong newest"))
print(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

with open("danger.txt", "w", newline='')as dangerfile:
    print("File Created")

time.sleep(10)

pathdir = ""
for root, dirs, files in os.walk(BASE_PATH):
    for filename in files:
        print(filename)
        if filename == "danger.txt":
            print(os.path.join(root, filename))
            pathdir = os.path.join(root, filename)
            os.remove(pathdir)
            break
'''