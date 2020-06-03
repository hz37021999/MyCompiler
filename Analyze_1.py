import string
import sys
import Analyze_2
Identifier=['if','else','for','while','do','int','write','read','']
Delimiter="( ) } { ;"
Operator_1="+-*/"
Operator_2="<>="
def init(FileName):
	i=0
	row=1
	j=0
	Got_char=[]
	Str=''
	file_1=open(FileName,'r')
	file_2=open("analyze_2.txt",'wr')
	fin=file_1.read()
	file_1.close()
	for x in fin:
		Got_char.append(x)
	#judge String -----------------------***************************---------------------
	while i<len(Got_char)-1:
		while(Got_char[i] ==' 'or Got_char[i]=='\n'or Got_char=='\t'):
			if(Got_char[i]=='\n'):
				row+=1
			i+=1
		if Got_char[i].isalpha():
			Str+=Got_char[i]
			i+=1
			while(Got_char[i].isalpha()or Got_char[i].isdigit()):
				Str=Str+Got_char[i]
				i+=1
			while(cmp(Str,Identifier[j])and j<=7):
				j+=1
			if j>=8:
				file_2.write(Str+' ID '+str(row)+'\n')
			else:
				file_2.write(Str+' '+Str+' '+str(row)+'\n')
			Str=''
			j=0
	#Judge Number ************************--------------------**********************
		elif Got_char[i].isdigit():
			Str+=Got_char[i]
			i+=1
			if  Got_char[i-1]!='0'and Got_char[i].isdigit():
				while Got_char[i].isdigit():
					Str+=Got_char[i]
					i+=1
			file_2.write(Str+' NUM '+str(row)+'\n')
			Str=''
	#Judge Delimiter ---------------------********************--------------
		elif Delimiter.find(Got_char[i])>=0:
			Str+=Got_char[i]
			i+=1
			file_2.write(Str+' '+Str+' '+str(row)+'\n')
			Str=''
	#Judge Operator ********************-----------------------*************
		elif  Operator_1.find(Got_char[i])>=0 and Got_char[i+1]!='*' :
			Str+=Got_char[i]
			i+=1
			file_2.write(Str+' '+Str+' '+str(row)+'\n')
			Str=''
		elif Operator_2.find(Got_char[i])>=0:
			Str+=Got_char[i]
			i+=1
			if Got_char[i]=='=':
				Str+=Got_char[i]
				i+=1
			file_2.write(Str+' '+Str+' '+str(row)+'\n')
			Str=''
		elif Got_char[i]=='!':
			Str+=Got_char[i]
			i+=1
			if Got_char[i]=='=':
				Str+=Got_char[i]
				i+=1
			file_2.write(Str+' '+Str+' '+str(row)+'\n')
			Str=''
	#Judge Comment **************-----------------------------*************
		elif Got_char[i]=='/':
			Str+=Got_char[i]
			i+=1
			if Got_char[i]=='*':
				Str+=Got_char[i]
				i+=1
				while(Got_char[i]!='*'or Got_char[i+1]!='/'):
					Str+=Got_char[i]
					print (i,len(Got_char))
					i+=1
					if i+1>=len(Got_char):
						break
				if Got_char[i]=='*'and Got_char[i+1]=='/':
					Str+=Got_char[i]+Got_char[i+1]
					i+=1
					if i>len(Got_char):
						break
					file_2.write(Str+' Comment '+str(row)+'\n')
			#Str=''<pre name="code" class="python">i=0
row=1
Str=''
Got_char=[]
data={}
addr=0
file_new=open("analyze_3.txt",'wr')
labelp=0