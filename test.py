import requests

BASE = "http://127.0.0.1:5000/"

testdata = [
			{"likes" : 78, "name" : "Tjenare", "views" : 19009},
			{"likes" : 69, "name" : "Kul va?", "views" : 1311209},
			{"likes" : 412, "name" : "Hahahah", "views" :12312523}
		   ]
#response = requests.get(BASE + "helloworld/emma")

#response = requests.put(BASE + "video/1", {"name" : "Hello world", "views" : 1000, "likes" : 10})
#print(response.json())
#input()
#for i in range(len(testdata)):
#	response = requests.put(BASE + "video/" + str(i), testdata[i])
#	print(response.json())


#input()
response = requests.patch(BASE + "video/2", {"views" : 12314152, "likes" : 132})
print(response.json())
