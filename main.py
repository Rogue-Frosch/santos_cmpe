import os
import csv
import time

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_FOLDER = os.path.join(BASE_PATH, 'RESOURCES')
CSV_PATH = os.path.join(CSV_FOLDER, "AKONGCSV.csv")

print(CSV_PATH)

with open(CSV_PATH, mode='r', newlines='') as csvfile:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_data.append(row)

print("------------------------------------------------------------")






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