import pickle

myObject = {'Key1':'data',
			'Key2':range(10)}
f = open('testPickleFile.pkl','wb')
pickle.dump(myObject,f)
f.close()

f = open('testPickleFile.pkl','rb')
myNewObject = pickle.load(f)

print (myObject)
print (myNewObject)