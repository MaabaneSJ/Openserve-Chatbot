from itertools import count
import json
from urllib import response
from pip._vendor import requests
# Prompt customer for inputs. Have as parameters (Interest API)
def functionEG(inputAddressText):
    # payload = {inputAddressText:"17 Thornton Rd, Westdene, Johannesburg"}
    # txtModalAddress = " "
    # payload2 = {txtModalAddress:inputAddressText}
    url='https://api.openserve.co.za/gateway/address/v1?.fullText={}&key=d6d810c7-d9f7-48bc-b383-9c31f355b200'.format(inputAddressText)
    # r = requests.get(url,params=payload2)
    r = requests.get(url)
    return r
    
st=input("What is your Street Address ")

# ct=input("What is your City ")
# txtAdd = st + ' '+ ct
txtAdd2=st
##########Calling the function############
result = functionEG(txtAdd2) 
#List
resultJSON = result.json()
print(result.url)
print(resultJSON)
# print(type(resultJSON))
# print(type(result))

######## Needs to go into a function ############
cc=[]
ccty=[]
for address in resultJSON:
    #Include individual storage!!
    # print(address['id'])
    cc.append(address['id'])
    # print(address['city'])
    ccty.append(address['city'])
    # print("######################")
    
print(cc)
print(ccty)
count=1
for i in ccty:
    countVariable=str(count)
    # str(print(countVariable+" = "))+str(print(i))
    print(str(countVariable+" = ")+str(i))
    count=count+1
    
i=int(0)
inputInteger2=input("Please choose your city in the list provided ")
intoInteger=int(inputInteger2)-1
# print(type(intoInteger))
index0= ccty[intoInteger]

print("Your address is: "+ st +" "+ index0)

# cityOptions=input("Please choose your city in the list provided ")
###Address variable is st
st=st + " " + index0
# print(st)
### Calling the full address !!!!!
resultFinal = functionEG(st).json() 
resultFinal2 = functionEG(st)
# data = json.loads('[...]')
#############Remove brackets
str = json.dumps(resultFinal[0])
# print(st)

firstValueInArray=[]
firstValueInArray=resultFinal[0]
# print(firstValueInArray)
print("###########################################")
print("Your full Address details:  ")
id=firstValueInArray["id"]
print("id" " = ",id)

mduFlag=firstValueInArray["mduFlag"]
print("mduFlag" " = ",mduFlag)

streetNr=firstValueInArray["streetNr"]
print("streetNr" " = ",streetNr)

streetName=firstValueInArray["streetName"]
print("streetName" " = ",streetName)

streetType=firstValueInArray["streetType"]
print("streetType" " = ",streetType)

locality=firstValueInArray["locality"]
print("locality" " = ",locality)

city=firstValueInArray["city"]
print("city" " = ",city)

stateOrProvince=firstValueInArray["stateOrProvince"]
print("stateOrProvince" " = ",stateOrProvince)

country=firstValueInArray["country"]
print("country" " = ",country)

geoCode=firstValueInArray["geoCode"]
print("geoCode" " = ",geoCode)

txtModalAddress = "Rooihuiskraal Rd, Kosmosdal, Centurion, Tshwane, Gauteng"
txtModalAddress=st
txtModalLat =-25.93200738495569 
txtModalLon =28.132845569886562
txtName ="Warwick"
txtSurname ="Attree" 
txtEmail ="attreewr1@telkom.co.za" 
txtContactNumber ="0713265874" 
Action ="insert" 
Prefered_ISP ="WA" 
ISPName ="Wa1" 
ISPCode ="wa2" 
ISPEmail ="Wa3"

# for key,value in firstValueInArray.items():
#     print(key, value)

def insertInterestAPI(txtModalAddress,txtModalLat,txtModalLon,txtName,txtSurname,txtEmail,txtContactNumber):

    # url='https://api.openserve.co.za/gateway/address/v1?.fullText={}&key=e77e5b93-72eb-45a3-b92b-3050dfd5a0a1'.format(inputAddressText)
    Action="insert" 
    Prefered_ISP="WA" 
    ISPName="Wa1" 
    ISPCode="wa2" 
    ISPEmail="Wa3"
    # https://api.openserve.co.za/gateway/address/v1?.fullText=61%20Oak%20Avenue&key=e77e5b93-72eb-45a3-b92b-3050dfd5a0a1
    url='http://cntrra20-waigis.telkom.co.za/apps/api/OSInterestRegister?txtModalAddress={}&txtModalLat={}&txtModalLon={}&txtName={}&txtSurname={}&txtEmail={}&txtContactNumber={}'.format(txtModalAddress,txtModalLat,txtModalLon,txtName,txtSurname,txtEmail,txtContactNumber)
    
    r = requests.get(url)
    
    
    return r


# txtModalAddress=Rooihuiskraal%20Rd,%20Kosmosdal,%20Centurion,%20Tshwane,%20Gauteng,%200157&txtModalLat=-25.93200738495569&txtModalLon=28.132845569886562&txtName=Warwick&txtSurname=Attree&txtEmail=attreewr1@telkom.co.za&txtContactNumber=0713265874&Action=insert&Prefered_ISP=WA&ISPName=Wa1&ISPCode=wa2&ISPEmail=Wa3
# print(insertInterestAPI(txtModalAddress,txtModalLat,txtModalLon,txtName,txtSurname,txtEmail,txtContactNumber).url)
# print(insertInterestAPI(txtModalAddress,txtModalLat,txtModalLon,txtName,txtSurname,txtEmail,txtContactNumber))