import pickle
import gzip

myObject = {'NewKey':'Data'}
f = gzip.open('testPickleFile.pkl','wb')
pickle.dump(myObject,f)
f.close()

f = gzip.open('testPickleFile.pkl','rb')
myNewObject = pickle.load(f)
f.close()

print(myObject)
print(myNewObject)