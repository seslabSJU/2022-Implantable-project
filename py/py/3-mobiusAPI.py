import requests
import json

def createApplicationEntity(AEname, serverURL):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
        "Content-Type":"application/json;ty=2"
    }
    body = {
        "m2m:ae":{
            "rn":AEname,
            "api":"0.2.481.2.0001.001.000111",
            "lbl":["key1","key2"],
            "rr": True,
            "poa":["MQTT|"]
        }
    }
    res = requests.post(serverURL+"/Mobius", headers=header, json=body)
    print(res.json())


def getApplicationEntity(AEname, serverURL):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius/"+AEname, headers=header, data="")
    print(res.json())


def createContainer(AEname,  dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname,
        "Content-Type":"application/vnd.onem2m-res+json; ty=3"
    }
    name = dir.split('/')[-1]
    udir = '/'.join(dir.split('/')[0:-1])
    print("udir:", udir)
    print("name:", name)
    body = {
        "m2m:cnt":{
            "rn":name,
            "lbl":[name],
            "mbs":16384
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+udir, headers=header, json=body)
    print(res.json())


def getContainer(AEname, dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname,
    }
    res = requests.get(serverURL+"/Mobius/"+AEname+dir, headers=header, data="")
    print(res.json())


def deleteContainer(AEname, dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "locale":"ko",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname
    }
    res = requests.delete(serverURL+"/Mobius/"+AEname+dir, headers=header, data = "")
    print(res.json())


#have to make COMMAND
def createSubscription(AEname, dir, webserver, serverURL):
    dir = addSlash(dir)
    header = {
        "X-M2M-Origin": AEname,
        "X-M2M-RI": "12345",
        "Content-Type": "application/json;ty=23"
    }
    body = {
        "m2m:sub": {
            "rn": "sub",
            "nu": [webserver + "?ct=json"],
            "nct": 1,
            "enc": {
                "net": [3]
            }
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+dir, headers=header, json=body)
    print(res.json())


def createContentInstance(AEname, dir, con, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "X-M2M-Origin": AEname,
        "X-M2M-RI": "12345",
        "Content-Type": "application/json;ty=4"
    }
    body = {
        "m2m:cin":{
            "con": con
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+dir, headers=header, json=body)
    print(res.json())

#get ae_list
def getApplicationEntityList(serverURL): # return AE name list
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius?fu=1&ty=2&lim=20", headers=header, data="")

    #print(res.json())
    
    res = res.json()['m2m:uril']
    for i, s in enumerate(res): # make ae name list
        res[i] = s[7:]
    
    return res

#remove all_ae
def removeAllApplicationEntity(serverURL):
    ae_list = getApplicationEntityList(serverURL)
    for step in ae_list:
        removeApplicationEntity(step)

#get ae_ri
def getApplicationEntityRI(serverURL, AEname):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius/"+AEname, headers=header, data="")
    res = res.json()
    ae_ri = res["m2m:ae"]["ri"]
    print(res)
    return ae_ri



#remove AEname
def removeApplicationEntity(serverURL, AEname):
    ri = getApplicationEntityRI(serverURL, AEname)

    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":ri,
    }
    res = requests.delete(serverURL+"/Mobius/"+AEname, headers=header, data="")
    res = res.json()
    print(res)

def getContentInstance(AEname, dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin": "SOrigin",
    }
    res = requests.get(serverURL+"/Mobius/"+AEname+dir, headers=header, data="").text
    #con = res.content()
    con1 = json.loads(res)
    return(con1['m2m:cin']['con'])


def addSlash(string):
    if string[0] != '/':
        string = '/' + string
    return string




d = getContentInstance('ServiceUser', '/test/la', 'http://34.64.221.188:7579')
print(d)