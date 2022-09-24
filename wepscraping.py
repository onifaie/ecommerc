import requests
import json
import smtplib, ssl



import sys

# from Send_Email.Send_Email import send_email
# sys.path is a list of absolute path strings
# sys.path.append('../Python_Automation')

# from Send_Email.Send_Email import *

from bs4 import BeautifulSoup  as bs # pip install Beautfulsoup 
import csv # including with python 
from itertools import zip_longest


def get_all_jop():
    

    jop_titleList=[]
    company_nameList=[]
    locationList=[]
    jop_skillsList=[]
    type_workList=[]

    cookies = dict(language='ar')

    # headers = {'Accept-Language': "lang=\AR-DZ"}
    result=requests.get("https://sa.indeed.com/jobs?q=python&l=Riyadh&from=searchOnHP&vjk=04f726171487f352",cookies=cookies)
    src=result.content
    #
    # print(src)
    soup=bs(src,"lxml")
    #print(soup)
    jop_title=soup.find_all("a",{"class":"jcs-JobTitle"})
    company_name=soup.find_all("span",{"class":"companyName"})
    location=soup.find_all("div",{"class":"companyLocation"})
    # jop_skills=soup.find_all("div",{"class":"jobsearch-jobDescriptionText"})
    # type_work=soup.find_all("div",{"class":"attribute_snippet"})

    for i in range (len(jop_title)):
        jop_titleList.append(jop_title[i].text)
        company_nameList.append(company_name[i].text)
        locationList.append(location[i].text)
        # jop_skillsList.append(jop_skills[i].text)
        # type_workList.append(type_work[i].text)


        



        
    print("this Jop Title >>>> ")
    print(jop_titleList)
    print("*"* 30)
    print("this List company Names >>>> ")
    print(company_nameList)
    print("*"* 30)
    print("this Location List >>>>")
    print(locationList)
    print("*"* 30)
    # print(jop_skillsList)
    # print("this Type_works >>>>> ")
    # print(type_workList)
    file_list=[jop_titleList,company_nameList,locationList]
    mydata=zip_longest(*file_list)
    with open("jop.csv","w") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(["jop_title","companyName","location"])
        wr.writerows(mydata)
        
get_all_jop()