d={"tete":"head","pomme":"apple","tour":"tower","frere":"brother","toi":"you"}

d["nouveau"]="new"



def dic(fr,en,d):
	if (fr in d) :
		return
	else :
		d[fr]=en
		
dic("aller","go")

def aff(d):
	for i in d.keys():
		print(d[i])
		
def dele(char,d):
	cd=d
	for i in cd.keys():
		if(i.startswith(char)) :
			del(d[i])
				