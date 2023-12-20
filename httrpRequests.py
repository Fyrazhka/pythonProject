import requests
from randomuser import RandomUser
import pandas as pd
import json
from bs4 import BeautifulSoup # this module helps in web scrapping.

def task1():
    url='https://www.ibm.com/'
    r=requests.get(url)
    print(r.status_code)

    print(r.request.headers)
    header=r.headers
    print(r.headers)

    url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/Example1.txt'

    r=requests.get(url)
    print(r.status_code)


def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                      "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(),
                      "Picture": user.get_picture()})

    return pd.DataFrame(users)

def task2():
    df=pd.DataFrame(get_users())
    print(df)
def task3():
    data = requests.get("https://fruityvice.com/api/fruit/all")
    results = json.loads(data.text)
    pd.DataFrame(results)
    df2 = pd.json_normalize(results)
    print(df2)
    cherry = df2.loc[df2["name"] == 'Cherry']
    print((cherry.iloc[0]['family']), (cherry.iloc[0]['genus']))
    banana=df2.loc[df2["name"]=='Banana']
    print(banana.iloc[0]['nutritions.calories'])

    r=requests.get('https://api.catboys.com/img')
    print(r.status_code)
    print(json.loads(r.text))
    for i in range(10):
        print('https://robohash.org/' + str(df2.loc[i][i]))

def task4():
    html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())


if __name__=='__main__':
    task1()
    task2()
    task3()
    task4()