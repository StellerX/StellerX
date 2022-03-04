#remove new line '\n' syntax while reading lines of any file
def rmnl(l):
    n_l=[]
    for i in l:
        if i[len(i)-1:len(i)]=='\n':
            n_l.append(i[0:len(i)-1])
        else:
        	n_l.append(i)
    return n_l
    
def read(file_name,seperator):
	dictionary={}
	with open(file_name) as f:
		data=f.readlines()
		newDATA=[]
		n=[]
		for i in data:
			newDATA.append(i.split(seperator))
		for i in range(len(newDATA)):
			n.extend(rmnl(newDATA[i]))
		for i in range(len(n)):
			if i==0 or i%2==0:
				dictionary[n[i]]=n[i+1]	
	return dictionary

def autoxy(name):
    if len(name)==12:
        return str(11)
    else:
        return str(12)
