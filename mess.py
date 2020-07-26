from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import csv
import math,random
import datetime

t=Tk()
width1=t.winfo_screenwidth()
height1=t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (width1,height1))
t.title("PaymentBook")
t.iconbitmap(r"favicon (7).ico")

##################################### FIRST WINDOW###########################################
#for top framework[f1=topframe,l1,l2]
f1=Frame(t,width=width1,height=height1/5,bg="IndianRed4")
f1.pack(side=TOP)
image = PhotoImage(file="icons8-khanda-96.png")
label = Label(t,image=image,bg="IndianRed4")
label.place(x=170,y=15)

l1=Label(f1,text="PUNJAB 'E' MESS",font=("Arial",60,"bold"),width=25,bg="IndianRed4")
l1.place(x=50,y=20)
l2=Label(f1,text="JODHADIH MORE CHAS - 827013, BOKARO(JH) Mob: 7033585340,7004803479",font=("Arial",20,"bold"),width=80,bg="IndianRed4")
l2.place(x=10,y=110)

branchs=["Computer Science Engineering.","Electronics and Communication Engineering.","Electrical engineering.","Mechanical Engineering.","Civil Engineering.","Electrical and Eletronic Engineering."]

###############declaring variable for registration######################################33

customername=StringVar()
fathername=StringVar()
roomnumber=StringVar()
mobilenumber=StringVar()
fathermobilenumber=StringVar()


################################## ADD CUSTOMER FRAME######################################
#for register [leftframe1,l4,l5,l6,l7,l8,l9,l10,l11,e1,e2,e3,e4,e5,b3,b4,combo1,combo2,combo3,combo4]
def add_customer():
		leftframe1=Frame(width=width1-width1/3.3,height=height1-height1/5,bg="gray")
		leftframe1.place(x=0,y=height1/5)
		
		date=Label(leftframe1,text="Date",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		date.place(x=20,y=20)
		day=list(range(1,32))
		month=["January","February",'March','April','May','June','July','August','September','October','November','December']
		year=list(range(2017,2036))
		global comboday
		global combomonth
		global comboyear
		comboday=Combobox(leftframe1,width=5,font=("Arial",15,"bold"),values=day)
		comboday.place(x=120,y=20)
		combomonth=Combobox(leftframe1,width=5,font=("Arial",15,"bold"),values=month)
		combomonth.place(x=200,y=20)
		comboyear=Combobox(leftframe1,width=5,font=("Arial",15,"bold"),values=year)
		comboyear.place(x=280,y=20)

#customer name
		l4=Label(leftframe1,text="Customer Name",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l4.place(x=70,y=110)
		e1=Entry(leftframe1,width=43,font=("Arial",15,"bold"),textvariable=customername)
		e1.place(x=300,y=110)
#father name
		l5=Label(leftframe1,text="Father Name",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l5.place(x=70,y=150)
		e2=Entry(leftframe1,width=43,font=("Arial",15,"bold"),textvariable=fathername)
		e2.place(x=300,y=150)
#room number
		l6=Label(leftframe1,text="Room No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l6.place(x=70,y=190)
		e3=Entry(leftframe1,width=43,font=("Arial",15,"bold"),textvariable=roomnumber)
		e3.place(x=300,y=190)
#mobile number
		l7=Label(leftframe1,text="Mobile No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l7.place(x=70,y=230)
		e4=Entry(leftframe1,width=43,font=("Arial",15,"bold"),textvariable=mobilenumber)
		e4.place(x=300,y=230)
#father mobile number
		l8=Label(leftframe1,text="Father Mobile No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l8.place(x=70,y=270)
		e5=Entry(leftframe1,width=43,font=("Arial",15,"bold"),textvariable=fathermobilenumber)
		e5.place(x=300,y=270)
#branch
		l9=Label(leftframe1,text="Branch",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l9.place(x=70,y=310)
		global combo1
		combo1=Combobox(leftframe1,width=41,font=("Arial",15,"bold"),values=branchs)
		combo1.place(x=300,y=310)
		
#year
		l10=Label(leftframe1,text="Year",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l10.place(x=70,y=350)
		year=["1st year","2nd year","3rd year","4th year"]
		global combo2
		combo2=Combobox(leftframe1,width=41,font=("Arial",15,"bold"),values=year)
		combo2.place(x=300,y=350)
#session start
		l11=Label(leftframe1,text="Session   From",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l11.place(x=70,y=390)
		session=list(range(2017,2036))
		global combo3
		combo3=Combobox(leftframe1,width=10,font=("Arial",15,"bold"),values=session)
		combo3.place(x=300,y=390)
#session end
		l11=Label(leftframe1,text="To",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l11.place(x=520,y=390)	
		sessionend=list(range(2021,2040))
		global combo4
		combo4=Combobox(leftframe1,width=10,font=("Arial",15,"bold"),values=sessionend)
		combo4.place(x=640,y=390)

		b3=Button(leftframe1,text="Back",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=home)
		b3.place(x=1,y=500)

		b4=Button(leftframe1,text="Register",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=csvfile)
		b4.place(x=630,y=500)

		b5=Button(leftframe1,text="Create new Table",width=18,font=("Arial",15,"bold"),bg="gray",anchor="center",activebackground="grey",command=createtable)
		b5.place(x=720,y=20)
		bill()


################################## CREATE TABLE FRAME ###########################################
#create table window
def createtable():
	text.delete(1.0,END)
	createtableframe=Frame(width=width1-width1/3.3,height=height1-height1/5 ,bg="gray")
	createtableframe.place(x=0,y=height1/5)

	l3=Label(createtableframe,text="Create New Table",font=("Arial",35,"bold"),width=25,bg="gray",anchor="center")
	l3.place(x=30,y=30)

	date=Label(createtableframe,text="Date",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
	date.place(x=150,y=150)
	day=list(range(1,32))
	month=["January","February",'March','April','May','June','July','August','September','October','November','December']
	year=list(range(2017,2036))
	global combocreateday
	global combocreatemonth
	global combocreateyear
	combocreateday=Combobox(createtableframe,width=5,font=("Arial",15,"bold"),values=day)
	combocreateday.place(x=230,y=150)
	combocreatemonth=Combobox(createtableframe,width=10,font=("Arial",15,"bold"),values=month)
	combocreatemonth.place(x=330,y=150)
	combocreateyear=Combobox(createtableframe,width=5,font=("Arial",15,"bold"),values=year)
	combocreateyear.place(x=500,y=150)

	createlable1=Label(createtableframe,text="Year",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
	createlable1.place(x=150,y=220)
	year=["1st year","2nd year","3rd year","4th year"]
	global combocreate1
	combocreate1=Combobox(createtableframe,width=41,font=("Arial",15,"bold"),values=year)
	combocreate1.place(x=230,y=220)

	submitbutton=Button(createtableframe,text="Submit",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=createnewtable)
	submitbutton.place(x=300,y=300)

	b3=Button(createtableframe,text="Back",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=add_customer)
	b3.place(x=1,y=500)
	bill()


################################### TEXT AREA FOR REGISTER #######################################
#f3 OR text
def registertext():
	text.delete(1.0,END)
	name=customername.get()
	fname=fathername.get()
	room=roomnumber.get()
	mobile=mobilenumber.get()
	fmobile=fathermobilenumber.get()
	branch=combo1.get()
	years1=combo2.get()
	startsession=combo3.get()
	endsession=combo4.get()
	days=comboday.get()
	months=combomonth.get()
	years=comboyear.get()
	text.insert(END,"\tWelcome to PUNJAB 'E' MESS\n")
	text.insert(END,"\tJodhadih More Chas - 827013,\n     Bokaro(JH) Mob: 7033585340,7004803479\n")
	text.insert(END,"\n************************************************************")
	text.insert(END,f"\n Customer name :  {name}")
	text.insert(END,f"\n Father name :  {fname}")
	text.insert(END,f"\n Room No. :  {room}")
	text.insert(END,f"\n Mobile No. :  {mobile}")
	text.insert(END,f"\n Father Mobile No. :  {fmobile}")
	text.insert(END,f"\n Branch :  {branch}")
	text.insert(END,f"\n Year:  {years1}")
	text.insert(END,f"\n Session : {startsession} to { endsession}")
	text.insert(END,f"\n Register Date : {days}-{months}-{years}")

def validmonth():
	paymentmonth1=firstmonth.get()
	paymentmonth2=secondmonth.get()
	paymentmonth3=thirdmonth.get()
	month1=combo5.get()
	month2=combo6.get()
	month3=combo7.get()
	if paymentmonth2.isdigit() and paymentmonth2!='' and month2!='':
		return True
	elif paymentmonth2=='' and paymentmonth2=='' and month2=='':
		return True
	else:
		messagebox.showerror("Opps","Please Enter Valid Month2 and Amount2")

	if paymentmonth3.isdigit() and paymentmonth3!='' and month3!='':
		return True
	elif paymentmonth3=='' and paymentmonth3=='' and month3=='':
		return True
	else:
		messagebox.showerror("Opps","Please Enter Valid Month3 and Amount3")

#################################### BILL AREA #################################################
def billarea():
	global x
	x=random.randint(100,10000)
	d = datetime.datetime.now()
	cd=d.strftime("%d-%m-%y  %I:%M %p")
	paymentmonth1=firstmonth.get()
	paymentmonth2=secondmonth.get()
	paymentmonth3=thirdmonth.get()
	month1=combo5.get()
	month2=combo6.get()
	month3=combo7.get()
	names=customername1.get()
	fname=fathername1.get()
	room=roomnumber1.get()
	if paymentmonth1.isdigit() and month1!='':		
		text.delete(1.0,END)
		text.insert(END,"\tWelcome to PUNJAB 'E' MESS\n")
		text.insert(END,"\tJodhadih More Chas - 827013,\n     Bokaro(JH) Mob: 7033585340,7004803479\n")
		text.insert(END,"\n************************************************************")
		text.insert(END,f"\n Bill No. :  {x} \t\t Date : {cd}")
		text.insert(END,f"\n Customer name :  {names}")
		text.insert(END,f"\n Father name :  {fname}")
		text.insert(END,f"\n Room No. :  {room}")
		text.insert(END,"\n------------------------------------------------------------------------")
		text.insert(END,"\nMonth \t\tStatus \t\tAmount")
		text.insert(END,"\n------------------------------------------------------------------------")
		if paymentmonth1!='' and month1!='':
			text.insert(END,f"\n{month1}\t\tPaid\t\t{paymentmonth1}.0")
		if paymentmonth2!='' and month2!='':
			text.insert(END,f"\n{month2}\t\tPaid\t\t{paymentmonth2}.0")
		if paymentmonth3!='' and month3!='':
			text.insert(END,f"\n{month3}\t\tPaid\t\t{paymentmonth3}.0")			
		text.insert(END,"\n\n------------------------------------------------------------------------")
		a=b=c=0
		if paymentmonth1!='':
			a=int(paymentmonth1)
		if paymentmonth2!='':
			b=int(paymentmonth2)
		if paymentmonth3!='':
			c=int(paymentmonth3)
		total=float(eval('a+b+c'))
		text.insert(END,f"\n\t\tTotal Amount:\t\t {total}")
		text.insert(END,"\n\n\n\n\n\t\t\t\tSignature")
		amount.set(total)
	else:
		messagebox.showerror("Opps","Please Enter Valid Month and Amount")



##############################  REGISTER INT0 FILE  ##############################################
#for register into file
def register():
	name=customername.get()
	fname=fathername.get()
	room=roomnumber.get()
	mobile=mobilenumber.get()
	fmobile=fathermobilenumber.get()
	branch=combo1.get()
	years=combo2.get()
	startsession=combo3.get()
	endsession=combo4.get()
	file=open('bills/'+name+".txt","w")
	file.write(name+"\n")
	file.write(fname+'\n')
	file.write(room+'\n')
	file.write(mobile+'\n')
	file.write(fmobile+'\n')
	file.write(branch+'\n')
	file.write(years+'\n')
	file.write(startsession+'\n')
	file.write(endsession+'\n')
	messagebox.showinfo("Confirmation","Register Succesfully")
	file.close()


################################ CREATE NEW TABLE#############################################
###############################register into csv file #####################################
def createnewtable():
		years1=combocreate1.get()
		years=combocreateyear.get()
		if years1=='' and years=="":
			messagebox.showerror("Opps","Please fill date and current year to create table")
		else:
			try:
				with open("list/"+years1+"  "+years+".csv","x",newline='') as f:
					w=csv.writer(f)
					w.writerow(['Customer name','father name','date','room','mobile number','father mobile number','branch','year','start session','end session',"January","February",'March','April','May','June','July','August','September','October','November','December'])
					messagebox.showinfo("Confirmation","Table Created Succesfully with name  "+years1+"   "+years+".txt")
			except:
				messagebox.showwarning("Check","Table "+years1+"   "+years+".txt"+"is alrealdy present")
				
		combocreate1.set('')
		combocreateyear.set('')
		combocreateday.set('')
		combocreatemonth.set('')
		

######################################### READ CSV FILE  ########################################
found=0
def readfile():
	global found
	global found1
	global answer
	years1=combo2.get()
	years=comboyear.get()
	names=customername.get()
	name=names.strip()
	fnames=fathername.get()
	fname=fnames.strip()
	try:
		found=0
		found1=0
		f=open("list/"+years1+"  "+years+".csv","r")
		r=csv.reader(f)
		data=list(r)
		for line in data:
			if name in line:
				found=1
				break
		for line1 in data:
			if fname in line1:
				found1=1
				break
		answer="yes"
	except:
		answer="no"		


######################################### CREATE TABLE FOR STUDENT IN CSV ######################
def csvfile():
	names=customername.get()
	name=names.strip()
	if name=='':
		messagebox.showerror("Opps","Please fill Details")
	else:	
		fnames=fathername.get()
		fname=fnames.strip()
		room=roomnumber.get()
		mobile=mobilenumber.get()
		fmobile=fathermobilenumber.get()
		if ((mobile.isdigit()==True) and (len(mobile)==10) and ((mobile.startswith("6")) or (mobile.startswith("7")) or (mobile.startswith("8")) or (mobile.startswith("9")))) and ((fmobile.isdigit()==True) and (len(fmobile)==10) and ((fmobile.startswith("6")) or (fmobile.startswith("7")) or (fmobile.startswith("8")) or (fmobile.startswith("9")))):
				branch=combo1.get()
				years1=combo2.get()
				startsession=combo3.get()
				endsession=combo4.get()
				days=comboday.get()
				months=combomonth.get()
				years=comboyear.get()
				global found
				global found1
				readfile()
				if found==1 and found1==1:
					messagebox.showwarning("Opps",name+" is alrealdy present in list")
				elif answer=="yes":
					registertext()
					ans=messagebox.askyesno("Confirmation...","Please Confirm Details...\nDo You Want To Save...")
					if ans==True:
						with open("list/"+years1+"  "+years+".csv","a",newline='') as f:
							w=csv.writer(f)
							w.writerow([name.title(),fname.title(),days+'/'+months+'/'+years,room,mobile,fmobile,branch,years1,startsession,endsession,'','','','','','','','','','','',''])
							messagebox.showinfo("Congratulation...","Register Successful")
					else:
						messagebox.showinfo("Information...","\tThankyou \nDetails Not Save into file")
						
				elif answer=="no":
					messagebox.showerror("Opps","Sorry "+years1+"  "+years+".txt"+" Table is not present...\nplease create Table..")
				
				
				name=customername.set('')
				fname=fathername.set('')
				room=roomnumber.set('')
				mobile=mobilenumber.set('')
				fmobile=fathermobilenumber.set('')
				branch=combo1.set('')
				years1=combo2.set('')
				startsession=combo3.set('')
				endsession=combo4.set('')
				days=comboday.set('')
				months=combomonth.set('')
				years=comboyear.set('')
		else:
			messagebox.showerror("Opps","Invalid Mobile Number\nPlease fill correct Mobile Number")
	
#########################################LIST SEARCH TEXT ######################################
def list_search():	
	years1=combosearchyear.get()
	years=combosearchyears.get()
	sframe2=Frame(width=width1,height=height1-height1/5,bg="gray")
	sframe2.place(x=0,y=height1/5)
	s=Scrollbar(sframe2)
	s.pack(side=RIGHT,fill=Y)
	s1=Scrollbar(sframe2,orient=HORIZONTAL)
	s1.pack(side=BOTTOM,fill=X)
	text11=Text(sframe2,width=143,height=27,bg="IndianRed1",font=(20),padx=30,pady=40,wrap='none',yscrollcommand=s.set,xscrollcommand=s1.set)
	text11.pack(side=LEFT,pady=0)
	s.config(command=text11.yview)
	s1.config(command=text11.xview)
	text11.delete(1.0,END)
	try:
		f=open("list/"+years1+"  "+years+".csv","r")
		r=csv.reader(f)
		data=list(r)
		l=[0,1,3,10,11,12,13,14,15,16,17,18,19,20,21]
		num=0
		a='\t'		
		for name in data:
			text11.insert(END,f"{num}   {name[0]}\t\t\t{name[1]}\t\t\t{name[3]}\t {name[10]}\t\t{name[11]}\t\t{name[12]}\t\t{name[13]}\t\t{name[14]}\t\t{name[15]}\t\t{name[16]}\t\t{name[17]}\t\t{name[18]}\t{a}{name[19]}\t{a}{name[20]}\t{a}{name[21]}")					
			text11.insert(END,"\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			num+=1
		text11.config(state=DISABLED)
	except:
		messagebox.showerror("Opps",years1+"  "+years+" file not found")
		

########################################## HOME ################################################
# [leftframe,l3,b1,b2]

def home():
				
		#this is for left frame
		leftframe=Frame(t,width=width1-width1/3.3,height=height1-height1/5,bg="gray")
		leftframe.place(x=0,y=height1/5)

		l3=Label(leftframe,text="WELCOME",font=("Arial",50,"bold"),width=25,bg="gray",anchor="center")
		l3.place(x=0,y=33)		

		b1=Button(leftframe,text="Recieve Payment",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=recieve_payment)
		b1.place(x=360,y=200)
		b2=Button(leftframe,text="Add New Customer",width=18,font=("Arial",20,"bold"),bg="gray",anchor="center",activebackground="grey",command=add_customer) #line  18 to 77
		b2.place(x=360,y=300)
		bill()
		text.delete(1.0,END)

##################################### LIST SEARCH ###########################################
		
		sframe=Frame(t,width=width1,height=30,bg="IndianRed4")
		sframe.place(x=0,y=0)

		year=["1st year","2nd year","3rd year","4th year"]
		global combosearchyear
		global combosearchyears
		combosearchyear=Combobox(sframe,width=8,font=("Arial",15),values=year)
		combosearchyear.place(x=width1-320,y=0)

		years=list(range(2017,2036))
		combosearchyears=Combobox(sframe,width=6,font=("Arial",15),values=years)
		combosearchyears.place(x=width1-200,y=0)
		
		listsearch=Button(sframe,text="Search List",width=10,font=("Arial",10,"bold"),bg="IndianRed4",anchor="center",activebackground="IndianRed4",command=list_search) #line  18 to 77
		listsearch.place(x=width1-100,y=0)

		listsearch=Button(sframe,text="Back",bd=1,width=10,font=("Arial",10,"bold"),bg="IndianRed4",anchor="center",activebackground="IndianRed4",command=home) #line  18 to 77
		listsearch.place(x=0,y=0)

#####################################TEXT FOR RECIEVE PAYMENT################################

def receivepayment():
	names=search.get()
	fname=fathername1.get()
	room=roomnumber1.get()
	n=customername1.get()
	text.delete(1.0,END)
	text.insert(END,"\tWelcome to PUNJAB 'E' MESS\n")
	text.insert(END,"\tJodhadih More Chas - 827013,\n     Bokaro(JH) Mob: 7033585340,7004803479\n")
	text.insert(END,"\n************************************************************")
	text.insert(END,f"\n Customer name :  {n}")
	text.insert(END,f"\n Father name :  {fname}")
	text.insert(END,f"\n Room No. :  {room}")
	text.insert(END,"\n------------------------------------------------------------------------")
	text.insert(END,"\nMonth \t\tStatus \t\tAmount")
	text.insert(END,"\n------------------------------------------------------------------------")
	#text.insert(END,"\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember")

######################################SEARCH FOR RECIEVE DATA IN CSV FILE #####################

flag=0
def searchdata():
	global flag
	flag=0
	global found1
	global answer
	years1=combosearchyear.get()
	years=combosearchyears.get()
	names=search.get()
	name=names.strip()
	try:
		if name!="" and name.isdigit()==False:
			f=open("list/"+years1+"  "+years+".csv","r")
			r=csv.reader(f)
			data=list(r)
			for line in data:
				if name.title() in line:					
					customername1.set(line[0])					
					fathername1.set(line[1])
					roomnumber1.set(line[3])
					mobilenumber1.set(line[4])
					fathermobilenumber1.set(line[5])
					branch1.set(line[6])
					year1.set(line[7])
					session1.set(line[8]+" to "+line[9])
					receivepayment()
					month1=line[10]
					month2=line[11]
					month3=line[12]
					month4=line[13]
					month5=line[14]
					month6=line[15]
					month7=line[16]
					month8=line[17]
					month9=line[18]
					month10=line[19]
					month11=line[20]
					month12=line[21]
					statuslist=[]
					for word in line[10:]:
						if word=="":
							statuslist.append("")
						elif word=="null":
							statuslist.append("null")
						else:
							statuslist.append("Paid")
					text.insert(END,f"\nJanuary\t\t {statuslist[0]}\t\t{month1}")
					text.insert(END,f"\nFebruary\t\t {statuslist[1]}\t\t{month2}")
					text.insert(END,f"\nMarch\t\t {statuslist[2]}\t\t{month3}")
					text.insert(END,f"\nApril\t\t {statuslist[3]}\t\t{month4}")
					text.insert(END,f"\nMay\t\t {statuslist[4]}\t\t{month5}")
					text.insert(END,f"\nJune\t\t {statuslist[5]}\t\t{month6}")
					text.insert(END,f"\nJuly\t\t {statuslist[6]}\t\t{month7}")
					text.insert(END,f"\nAugust\t\t {statuslist[7]}\t\t{month8}")
					text.insert(END,f"\nSeptember\t\t {statuslist[8]}\t\t{month9}")
					text.insert(END,f"\nOctober\t\t {statuslist[9]}\t\t{month10}")
					text.insert(END,f"\nNovember\t\t {statuslist[10]}\t\t{month11}")
					text.insert(END,f"\nDecember\t\t {statuslist[11]}\t\t{month12}")
					text.insert(END,"\n------------------------------------------------------------------------")
					sum=0
					for num in line[10:]:
						if num!='' and num!="null":		
							sum=sum+float(num)
					text.insert(END,f"\t TOTAL AMOUNT \t\t\tRs. {sum}")
					flag=1
					
			if flag==0:
				messagebox.showerror("Opps","Name "+name+" not found")	
		elif name!='' and name.isdigit()==True:	
			try:
				text.delete(1.0,END)
				with open("bills/"+str(name)+".txt","r")as f:
					data=f.readlines()
					for line in data:
						text.insert(END,f"{line}")
				empty()
			except:
				messagebox.showerror("Opps","Bill Not Found")
		else:
			messagebox.showerror("Opps","Please Enter Name")
	except:
		messagebox.showerror("Opps",years1+"  "+years+" file not found")

###################################ADD PAYMENT TO CSV TABLE###################################
def addpayment():
	billarea()
	years1=combosearchyear.get()
	years=combosearchyears.get()
	paymentmonth1=firstmonth.get()
	paymentmonth2=secondmonth.get()
	paymentmonth3=thirdmonth.get()	
	month1=combo5.get()
	m= 10 if month1=="January" else 11 if month1=="February" else 12 if month1=="March" else 13 if  month1=="April" else 14 if month1=="May" else 15 if month1=="June" else 16 if month1=="July" else 17 if month1=="August" else 18 if month1=="September" else 19 if month1=="October" else 20 if month1=="November" else 21 
	prev=m
	month2=combo6.get()
	month3=combo7.get()
	names=search.get()
	name=names.strip()	
	if paymentmonth1=='':
		messagebox.showwarning("Opps","Please Enter Amount")
	else:
		try:
			bill_data=text.get('1.0',END)
			with open("bills/"+str(x)+".txt","x")as f:
				f.write(bill_data)
			try:
				with open("list/"+years1+"  "+years+".csv","r",newline='') as f:
					r=csv.reader(f)
					data=list(r)
					list1=[]
					j=0
					i=1
					for line in data:
						if name.title() in line:
							for item in line:
								if item=="" and i==1:
									
									line[m]=paymentmonth1							
									i+=1
									m+=1
									for k in range(prev-1,9,-1):
										if line[k]=="":
											line[k]="null"									
								if item=="" and i==2:
									if m==22:
										break
									else:
										line[m]=paymentmonth2
										i+=1									
										m+=1								
								if item=='' and i==3:
									if m==22:
										break
									else:
										line[m]=paymentmonth3
										i+=1
										m+=1								
								j+=1							
						list1.append(line)				
					ans=messagebox.askyesno("Confirmation","Please Confirm Payment")
					if ans==True:
							with open("list/"+years1+"  "+years+".csv","w",newline='') as g:
									q=csv.writer(g)	
									for word in list1:
										q.writerow(word)
							messagebox.showinfo("Thanks","Payment Successful\nBill Number is:"+ str(x))								
					else:
						messagebox.showinfo("Thanks","Payment Cancel Successful")
						empty()
			except:
				messagebox.showerror("Opps","Please Fill Details")
		except:
			messagebox.showinfo("Opps","Bill No. is already exit please create another bill")

######################################EMPTY ENTRY##########################################
def empty():
				customername1.set('')
				fathername1.set('')
				roomnumber1.set('')
				mobilenumber1.set('')
				fathermobilenumber1.set('')
				branch1.set('')				
				session1.set('')
				amount.set('')
				year1.set('')
				firstmonth.set('')
				secondmonth.set('')
				thirdmonth.set('')
				combo5.set('')
				combo6.set('')
				combo7.set('')
				#search.set('')



################################### RECEIVE PAYMENT ###########################################	


search=StringVar()
customername1=StringVar()
fathername1=StringVar()
roomnumber1=StringVar()
mobilenumber1=StringVar()
fathermobilenumber1=StringVar()
branch1=StringVar()
year1=StringVar()
session1=StringVar()
firstmonth=StringVar()
secondmonth=StringVar()
thirdmonth=StringVar()
amount=StringVar()
def recieve_payment():
		leftframe2=Frame(width=width1-width1/3.3,height=height1-height1/5,bg="gray")
		leftframe2.place(x=0,y=height1/5)	
				
# select Year
		l12=Label(leftframe2,text="Select Year",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l12.place(x=5,y=10)
		year=["1st year","2nd year","3rd year","4th year"]
		global combosearchyear
		global combosearchyears
		combosearchyear=Combobox(leftframe2,width=8,font=("Arial",15),values=year)
		combosearchyear.place(x=120,y=10)

		years=list(range(2017,2036))
		combosearchyears=Combobox(leftframe2,width=6,font=("Arial",15),values=years)
		combosearchyears.place(x=240,y=10)
		
#search
		l13=Label(leftframe2,text="Name/Bill.No",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l13.place(x=380,y=10)
		e7=Entry(leftframe2,width=25,font=("Arial",15),textvariable=search)
		e7.place(x=510,y=10)
		searchbutton=Button(leftframe2,text="Search",font=("Arial",10,"bold"),activebackground="grey",bg="gray",command=searchdata)
		searchbutton.place(x=800,y=10)
		
#customer name
		l14=Label(leftframe2,text="Customer Name",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l14.place(x=15,y=70)
		name_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=customername1)
		name_entry.place(x=180,y=70)
#father name
		l15=Label(leftframe2,text="Father Name",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l15.place(x=450,y=70)
		fathername_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=fathername1)
		fathername_entry.place(x=650,y=70)
#branch
		l16=Label(leftframe2,text="Branch",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l16.place(x=15,y=110)
		branch_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=branch1)
		branch_entry.place(x=180,y=110)
#year
		l17=Label(leftframe2,text="Year",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l17.place(x=450,y=110)
		year_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=year1)
		year_entry.place(x=650,y=110)
#room
		l18=Label(leftframe2,text="Room No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l18.place(x=15,y=150)
		room_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=roomnumber1)
		room_entry.place(x=180,y=150)
#session
		l19=Label(leftframe2,text="Session",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l19.place(x=450,y=150)
		session_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=session1)
		session_entry.place(x=650,y=150)
#contact
		l20=Label(leftframe2,text="Contact No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l20.place(x=15,y=190)
		contact_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=mobilenumber1)
		contact_entry.place(x=180,y=190)
#father conrtact
		l21=Label(leftframe2,text="Father Contact No.",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l21.place(x=450,y=190)
		fathercontact_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=fathermobilenumber1)
		fathercontact_entry.place(x=650,y=190)

#month 1
		month=["January","February",'March','April','May','June','July','August','September','October','November','December']
		l22=Label(leftframe2,text="Month 1",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l22.place(x=15,y=230)
		global combo5
		combo5=Combobox(leftframe2,width=20,font=("Arial",15),values=month)
		combo5.place(x=180,y=230)

#amount 1
		l23=Label(leftframe2,text="Amount 1",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l23.place(x=450,y=230)
		month2_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=firstmonth)
		month2_entry.place(x=650,y=230)

#month 2
		l24=Label(leftframe2,text="Month 2",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l24.place(x=15,y=270)
		global combo6
		combo6=Combobox(leftframe2,width=20,font=("Arial",15),values=month)
		combo6.place(x=180,y=270)


#amount 2
		l25=Label(leftframe2,text="Amount 2",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l25.place(x=450,y=270)
		month2_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=secondmonth)
		month2_entry.place(x=650,y=270)

#month 3
		l26=Label(leftframe2,text="Month 3",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l26.place(x=15,y=310)
		global combo7
		combo7=Combobox(leftframe2,width=20,font=("Arial",15),values=month)
		combo7.place(x=180,y=310)


#amount 3
		l27=Label(leftframe2,text="Amount 3",font=("Arial",15,"bold"),width=15,bg="gray",anchor="w")
		l27.place(x=450,y=310)
		month3_entry=Entry(leftframe2,width=22,font=("Arial",15),textvariable=thirdmonth)
		month3_entry.place(x=650,y=310)

#total amount
		l28=Label(leftframe2,text="Total Amount",font=("Arial",20,"bold"),width=15,bg="gray",anchor="w")
		l28.place(x=400,y=380)
		total_entry=Entry(leftframe2,width=17,font=("Arial",20,'bold'),textvariable=amount)
		total_entry.place(x=650,y=380)		
		
#back button
		b5=Button(leftframe2,text="Back",width=18,font=("Arial",15,"bold"),bg="gray",anchor="center",activebackground="grey",command=home)
		b5.place(x=1,y=500)
		
		b6=Button(leftframe2,text="Generate Bill",width=18,font=("Arial",15,"bold"),bg="gray",anchor="center",activebackground="grey",command=billarea)
		b6.place(x=400,y=500)

		b7=Button(leftframe2,text="Submit",width=18,font=("Arial",15,"bold"),bg="gray",anchor="center",activebackground="grey",command=addpayment)
		b7.place(x=670,y=500)
		empty()
		search.set("")
		bill()


#########################this is for right frame [f3=bill frame]#################################

def bill():	
	f3=Frame(width=width1/3.3+2,height=height1-height1/5,bg="white")
	f3.place(x=width1-width1/3.3,y=height1/5)
	global text
	text=Text(f3,width=40,height=25,font=(20),padx=30,pady=40,wrap=WORD)
	text.place(x=0,y=55)

	l29=Label(f3,text="BILL AREA",width=23,font=("Arial",22,"bold"),bg='gray',bd=10,relief=RAISED)
	l29.place(x=0,y=0)


home()
t.mainloop()