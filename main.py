from tkinter import *
from tkinter import messagebox as msgbox
from KEEpydb import KEEpydb as database
from mylibraries import readtool
from PIL import ImageTk,Image
import time
import os
import CLIENT
#settingfile
SETTINGS=readtool.read('databaseCore/settings.txt',':')

class Main:
    def __init__(self,root):
        self.query=database.query('databaseCore','stellerx','')
        self.root=root
        self.width=SETTINGS['width']
        self.height=SETTINGS['height']
        self.root.geometry(f'{self.width}x{self.height}+0+0')
        self.root.maxsize(int(self.width),int(self.height))
        self.root.minsize(int(self.width),int(self.height))
        self.root.title('Steller X')
        self.backbutton=ImageTk.PhotoImage(Image.open(self.query.search('BACK BUTTON')[1]).resize((25,25), Image.ANTIALIAS))
        self.createacc=ImageTk.PhotoImage(Image.open(self.query.search('CREATE ACC')[1]).resize((int(self.width),int(self.height)), Image.ANTIALIAS))
        self.linknewacc=ImageTk.PhotoImage(Image.open(self.query.search('LINK NEW ACC')[1]).resize((150,150), Image.ANTIALIAS))
        self.nextButton=ImageTk.PhotoImage(Image.open(self.query.search('NEXT BUTTON')[1]).resize((350,95), Image.ANTIALIAS))
        self.statusButton=ImageTk.PhotoImage(Image.open(self.query.search('STATUS BUTTON')[1]).resize((70,70), Image.ANTIALIAS))
        self.homeButton=ImageTk.PhotoImage(Image.open(self.query.search('HOME BUTTON')[1]).resize((70,70), Image.ANTIALIAS))
        self.PROFILE=ImageTk.PhotoImage(Image.open(self.query.search('PROFILE')[1]).resize((int(self.width),int(self.height)), Image.ANTIALIAS))
        self.default_avatar=ImageTk.PhotoImage(Image.open(self.query.search('DEFAULT AVATAR')[1]).resize((150,150), Image.ANTIALIAS))
        self.settings_icon=ImageTk.PhotoImage(Image.open(self.query.search('SETTINGS ICON')[1]).resize((55,55), Image.ANTIALIAS))
        self.key_icon=ImageTk.PhotoImage(Image.open(self.query.search('KEY')[1]).resize((55,55), Image.ANTIALIAS))
        self.about_icon=ImageTk.PhotoImage(Image.open(self.query.search('ABOUT')[1]).resize((55,55), Image.ANTIALIAS))
        self.uidpng=ImageTk.PhotoImage(Image.open(self.query.search('uid')[1]).resize((55,55), Image.ANTIALIAS))
        self.default_boy=ImageTk.PhotoImage(Image.open(self.query.search('DEFAULT BOY')[1]).resize((40,40), Image.ANTIALIAS))
        self.refresh_button=ImageTk.PhotoImage(Image.open(self.query.search('REFRESH BUTTON')[1]).resize((70,70), Image.ANTIALIAS))
        self.icon=PhotoImage(file=self.query.search('iCON')[1])
        self.plus=ImageTk.PhotoImage(Image.open(self.query.search('PLUS')[1]).resize((25,25), Image.ANTIALIAS))
        self.bg=ImageTk.PhotoImage(Image.open(self.query.search('bg')[1]).resize((458,435), Image.ANTIALIAS))
        self.login_button=ImageTk.PhotoImage(Image.open(self.query.search('login')[1]).resize((175,35), Image.ANTIALIAS))
        self.letlogin_button=ImageTk.PhotoImage(Image.open(self.query.search('letconnect')[1]).resize((175,35), Image.ANTIALIAS))
        self.introicon=ImageTk.PhotoImage(Image.open(self.query.search('INTRO BG ICON')[1]).resize((150,150), Image.ANTIALIAS))
        self.techimghome=ImageTk.PhotoImage(Image.open(self.query.search('techimghome')[1]).resize((150,150), Image.ANTIALIAS))
        ##################### USER PROFILE ########################
        temp=os.listdir('databaseCore/profile_info/photo')
        self.profilephoto='databaseCore/profile_info/photo/'+temp[0]          
        self.root.iconphoto(False,self.icon)
        
        self.u,self.p=StringVar(),StringVar()
        self.newacc_condition=False
        
    def INTRO(self):
        frameINTRO=Frame(self.root,width=self.width,height=self.height,bg=SETTINGS['INTRO BG']).place(x=0,y=0)
        photo=ImageTk.PhotoImage(Image.open(SETTINGS['INTRO BG ICON']).resize((150,150), Image.ANTIALIAS))
        label=Label(frameINTRO, image=photo,bg='white')
        label.image=photo
        label.place(x=525,y=210)
        Label(frameINTRO,
                text='STELLER-X',bg='white',fg='black',
                font='verdana 35 bold').place(x=200,y=255)

    def Login(self):
        self.frameLOGIN=Frame(self.root,height=self.height,width=self.width,bg='white').place(x=0,y=0)
        self.header=Label(self.frameLOGIN,text='Welcome To',bg='white',font='verdana 14 ')
        self.header1=Label(self.frameLOGIN,text=SETTINGS['TITLE'],bg='white',font='verdana 16 bold')
        self.header.place(x=30,y=30)
        self.header1.place(x=125,y=30)
        image=Image.open(SETTINGS['INTRO BG ICON'])
        photo=ImageTk.PhotoImage(image.resize((200,200), Image.ANTIALIAS))
        label=Label(self.frameLOGIN, image=photo,bg='white')
        label.image=photo
        label.place(x=140,y=160)
        loginbgframe=Frame(self.frameLOGIN,bg='white')
        loginbgframe.place(x=360,y=100,width=400,height=350)     
        #login box
        global USERNAME,PASSWORD
        USERNAME=self.u
        PASSWORD=self.p
        Label(loginbgframe,
                text='Enter Auth ( login ! )',
                fg='black',
                bg='white',
                font='verdana 15').place(x=120,y=10)		
        e0=Entry(self.frameLOGIN,textvariable=USERNAME,fg='grey',font='verdana 11',bg='light yellow')
        e0.place(x=470,y=180-20,width=250,height=40)
        e1=Entry(self.frameLOGIN,textvariable=PASSWORD,fg='grey',font='verdana 11',bg='light yellow')
        e1.place(x=470,y=230-20,width=250,height=40)		
        if self.newacc_condition==False:
        	USERNAME.set(' Username')
        	PASSWORD.set(' Password')
        e0.bind('<Button-1>',lambda e:USERNAME.set(''))
        e1.bind('<Button-1>',lambda e:PASSWORD.set(''))
        #buttons
        self.loginButton=Button(self.frameLOGIN,
                           image=self.letlogin_button,
                           bg='aquamarine',
                           font='verdana 17',command=self.login__
                           )
        self.loginButton.image=self.letlogin_button	
        self.loginButton.place(x=500,y=300-20)
        self.signupButton=Label(loginbgframe,text='Sign Up',font='verdana 11',fg='black',bg='white')
        self.signupButton.place(x=195,y=230)
        self.signupButton.bind("<Button-1>",MainFunctions().CreateAccount)		
        forgetPassword=Label(self.frameLOGIN,text='forget password',bg='white',fg='black').place(x=245,y=790)
        
    def login__(self):
    	global USERNAME,PASSWORD
    	data=CLIENT.check(USERNAME.get(),PASSWORD.get())
    	if data!='Re-Check-Username-Or-Password':
    		data=data.split('#')
    		if data[2]!=None:
    			self.query.update('b2',str(data[2])) #name
    		if data[1]!=None:
    			self.query.update('b3',str(data[1])) #username
    		if data[11]!=None:
    			self.query.update('b4',str(data[11])) #age
    		if data[10]!=None:
    			self.query.update('b5',str(data[10])) #sex
    		if data[3]!=None:
    			self.query.update('b6',str(data[3]))
    			if data[4]!=None:
    				self.query.update('b7',str(data[4]))
    		self.query.update('b8','online')
    		self.query.save()
    		Screens().HomeScreen()
    	else:
    		msgbox.showwarning('alert','invalid Credentials !')
    def start(self):
        if self.query.get_cell('b8')=='online':
            Screens().HomeScreen()
        else:
            self.Login()

class MainFunctions(Main):
	def __init__(self):
		super(MainFunctions,self).__init__(root)
		
	def CreateAccount(self,event):
		newFrame=Frame(self.root,width=self.width,height=self.height,bg='white').place(x=0,y=0)		
		backbutton=Label(newFrame,image=self.backbutton,bg='white')
		backbutton.image=self.backbutton
		backbutton.place(x=50,y=20)
		backbutton.bind("<Button-1>",lambda event : self.Login())	
		Label(newFrame,text='New',font='verdana 18 bold',bg='white').place(x=90,y=80)
		Label(newFrame,text='Account',font='verdana 18 bold',bg='white').place(x=90,y=115)
		linknewacc=Label(newFrame,image=self.linknewacc,bg='white')
		linknewacc.image=self.linknewacc
		linknewacc.place(x=99,y=170)		
		f=Frame(newFrame,width=300,height=350,bg='white')
		f.place(x=360,y=60)
		global fullName,userName
		fullName=StringVar()
		userName=StringVar()
		fullname=Entry(newFrame,textvariable=fullName,bg='light yellow',width=28)
		username=Entry(newFrame,textvariable=userName,bg='light yellow',width=28)
		fullname.place(x=390,y=130,height=30,width=235)
		username.place(x=390,y=200,height=30,width=235)		
		Label(newFrame,text='Full Name',font='verdana 11',fg='black',bg='white').place(x=390,y=100)
		Label(newFrame,text='User Name',font='vrrdana 11',fg='black',bg='white').place(x=390,y=175)			
		login_official=Label(newFrame,text='Already have an Account ?',font='verdana 9 bold',fg='black',bg='white')
		login_official.place(x=420,y=250)
		login_official.bind('<Button-1>',lambda event:Main().Home)
		Button(newFrame,text='Next',font='verdana 9',padx=90,pady=10,bg='green3',fg='black',command=self.c2).place(x=395,y=300)
		Label(newFrame,text='Step ( 1/3 )',
             font='default 14',bg='white',fg='black').place(x=125,y=365)
		nxticon=Label(newFrame,text='NEXT >',
             font='default 11',bg='white',fg='GREEN')
		nxticon.place(x=600,y=460)
		nxticon.bind('<Button-1>',lambda event:self.c2())
	
	def c2(self):
		global userName,fullName
		if userName.get()!='' and fullName.get()!='':
			if len(userName.get())>5:
				if CLIENT.abletomakeaccount(userName.get())=='true':
					self.CreateAccountSTEP2()
				else:
					msgbox.showwarning('Oops!','This Username is Already registered!\nwith STELLER X; Try to choose uniqe. ')
			else:
				msgbox.showinfo('Advise','UserName must be of minimum 5 charecters.')
		else:
			msgbox.showwarning('Note','To Proceed Please Fill All Fields Properly')
	def CreateAccountSTEP2(self):
		newFrame=Frame(self.root,width=self.width,height=self.height,bg='white')
		newFrame.place(x=0,y=0)
		f=Frame(newFrame,width=300,height=350,bg='white')
		f.place(x=360,y=60)	
		backbutton=Label(newFrame,image=self.backbutton,bg='white')
		backbutton.image=self.backbutton
		backbutton.place(x=50,y=20)
		backbutton.bind("<Button-1>",lambda event : self.CreateAccount((0)))		
		Label(newFrame,text='User',font='verdana 18 bold',bg='white').place(x=90,y=80)
		Label(newFrame,text='Credentials',font='verdana 18 bold',bg='white').place(x=90,y=115)	
		linknewacc=Label(newFrame,image=self.linknewacc,bg='white')
		linknewacc.image=self.linknewacc
		linknewacc.place(x=99,y=170)	
		global age,gender,email_address
		age=StringVar()
		gender=StringVar()
		email_address=StringVar()			
		age_=Entry(newFrame,textvariable=age,bg='light yellow')
		gender_=Entry(newFrame,textvariable=gender,bg='light yellow')
		email_=Entry(newFrame,textvariable=email_address,bg='light yellow')
		age_.place(x=400,y=134,height=30,width=235)
		gender_.place(x=400,y=210,height=30,width=235)
		email_.place(x=400,y=285,height=30,width=235)		
		Label(newFrame,text='Age',font='verdana 11',bg='white',fg='black').place(x=400,y=110)
		Label(newFrame,text='Gender',font='verdana 11',bg='white',fg='black').place(x=400,y=200-14)
		Label(newFrame,text='Email/Gmail/Mobile No',font='verdana 11',bg='white',fg='black').place(x=400,y=280-20)
		Button(newFrame,text='Next',font='verdana 9',padx=90,pady=10,bg='green3',fg='black',command=self.CreateAccountSTEP3).place(x=405,y=350)
		Label(newFrame,text='Step ( 2/3 )',
               font='default 14',bg='white',fg='black').place(x=125,y=365)
		nxticon=Label(newFrame,text='NEXT >',
               font='default 11',bg='white',fg='GREEN')
		nxticon.place(x=600,y=460)
		nxticon.bind('<Button-1>',lambda event:self.CreateAccountSTEP3())
	
	def c3(self):
		global age,gender,email_address
		if age.get()!='' and gender.get()!='' and email_address.get()!='':
			if age.get().isdigit()==False:
				msgbox.showwarning('Oops!','Go and see your Aadhar card and enter here\nhow old are you.')
			if int(age.get())==0:
				msgbox.showwarning('Uffffffff ! age Query','Hello Dear Jr. Einstien How are you you !')
			if int(age.get())<11:
				msgbox.showarning('Uffffffff !','Hope so You are over 11')
			if gender.get().lower() not in ['male','m','f','female']:
				msgbox.showwarning('Gender ?','please Try to fill (M/F/Male/Female)')
			if email_address.get().isdigit() and len(email_address.get()) not in [10,12]:
				msgbox.showinfo('Mobile No ?','Please Check your Mobile number.')
			if '@' not in list(email_address.get()) and len(email_address.get())>6:
				msgbox.showinfo('Mobile No ?','Please Check your Email Address Again\nand then Enter it.')
		elif age.get()=='':
			msgbox.showwarning('Fields ?','Fill All Fields properly to Proceed')
		elif gender.get()=='':
			msgbox.showwarning('Fields ?','Fill All Fields properly to Proceed')
		elif email_address.get()=='':
			msgbox.showwarning('Fields ?','Fill All Fields properly to Proceed')

		else:
			self.CreateAccountSTEP3()
				
	def CreateAccountSTEP3(self):
		newFrame=Frame(self.root,width=self.width,height=self.height,bg='white').place(x=0,y=0)
		newFrame=Frame(self.root,width=self.width,height=self.height,bg='white').place(x=0,y=0)
		createacc=Label(newFrame,image=self.createacc)
		createacc.image=self.createacc		
		backbutton=Label(newFrame,image=self.backbutton,bg='white')
		backbutton.image=self.backbutton
		backbutton.place(x=50,y=20)
		backbutton.bind("<Button-1>",lambda event : self.CreateAccountSTEP2())		
		Label(newFrame,text='User',font='verdana 18 bold',bg='white').place(x=90,y=80)
		Label(newFrame,text='Password',font='verdana 18 bold',bg='white').place(x=90,y=115)		
		linknewacc=Label(newFrame,image=self.linknewacc,bg='white')
		linknewacc.image=self.linknewacc
		linknewacc.place(x=99,y=170)	
		Label(newFrame,text='Step ( 3/3 )',
                font='default 14',bg='white',fg='black').place(x=125,y=365)	
		f=Frame(newFrame,width=300,height=350,bg='white')
		f.place(x=360,y=60)		
		global password,password2
		password=StringVar()
		password2=StringVar()		
		password1=Entry(newFrame,textvariable=password,bg='light yellow',width=28)
		password2=Entry(newFrame,textvariable=password2,bg='light yellow',width=28)
		password1.place(x=390,y=130,height=30,width=235)
		password2.place(x=390,y=200,height=30,width=235)		
		Label(newFrame,text='Create password',font='verdana 11',bg='white',fg='black').place(x=390,y=100)
		Label(newFrame,text='Confirm password',font='verdana 11',bg='white',fg='black').place(x=390,y=175)	
		Button(newFrame,text='Getting Started with New Account',bg='green3',fg='black',padx=20,pady=10,command=self.check_passordpossibilities).place(x=395,y=300)
		nxticon=Label(newFrame,text='NEXT >',font='default 11',bg='white',fg='GREEN')
		nxticon.place(x=600,y=460)
		nxticon.bind('<Button-1>',lambda event:self.check_passordpossibilities())
		
	def check_passordpossibilities(self):
		global password,password2
		if password.get()==password2.get():
			if len(password2.get())>6:
				self.createaccount__()
			else:
				msgbox.showinfo('Password Length','Password must be of 6 or more charecters')
		else:
			msgbox.showwarning('Password Match error','Password Not Match.')
		
	def createaccount__(self):
		global fullName,userName,age,gender,email_address,password,password2
		if password.get()!=password.get():
			msgbox.showwarning('Alert','Please Make Sure you are entering Password\nbothtimes same?')
		else:
			CLIENT.createacc([
				userName.get(),
				fullName.get(),
				email_address.get(),
				email_address.get(),
				password2.get(),
				'non-verified person',
				str(time.asctime()),
				'unknown IP',
				gender.get(),
				age.get()] )
			msgbox.showinfo('Stellerx','Account Created sucessfully ...\nTo Enjoy Stellerx Services Login ! your\nNew Account.')
			self.u.set(userName.get())
			self.p.set(password2.get())
			self.newacc_condition=True
			self.Login()
			
class Screens(Main):
    def __init__(self):
        super().__init__(root)
    def ComposeMail(self):
        global Content,to,title
        f2=Frame(self.root,bg='black',width=int(self.width),height=int(self.height)-30).place(x=0,y=0)
        l=Label(f2,text='↩',font='verdana 20 bold',bg='black',fg='white')
        l.place(x=20,y=10)
        l.bind('<Button-1>',lambda e:self.HomeScreen())
        Frame(f2,bg='white').place(x=20,y=50,width=840,height=1)
        Label(f2,text='S T E L L E R  X',bg='black',fg='cyan',font='verdana 15').place(x=60,y=10)
        Label(f2,text='M A I L',bg='black',fg='cyan',font='verdana 12').place(x=100,y=55)     
        Label(f2,text='To',fg='white',bg='black',font='verdana 12').place(x=40,y=90)
        Label(f2,text='Subject',fg='white',bg='black',font='verdana 12').place(x=40,y=120)
        to=StringVar()
        Entry(f2,textvariable=to,font='verdana 13',bg='black',fg='white',relief='flat').place(x=80,y=90,width=500)
        title=StringVar()
        title.set('(Untitled!)')
        Entry(f2,textvariable=title,font='verdana 13',bg='black',fg='white',relief='flat').place(x=80+50,y=120,width=500-50)
        Content=Text(f2,bg='black',fg='white',font='verdanaa 20')
        Content.place(x=40,y=150,height=400-20,width=830)
        Button(f2,text='Send',bg='black',relief=SUNKEN,fg='cyan',font='verdana 11',command=self.Send).place(x=768,y=530,width=100)
        #Button(f2,text='B',bg='black',fg='lawn green').place(x=20,y=530,width=30)
        global status
        status.config(text='')
        status.place(x=10,y=570)

    def Send(self):
        global status,Content,to,title
        status.config(text='Status > Preparing to send ..')
        self.root.update_idletasks()
        time.sleep(1.5)
        if title.get()=='':
        	title.set('(untitled)')
        status.config(text='Status > Sending ...')
        mail=Content.get(1.0,'end-1c')
        toMail=to.get()
        toName=CLIENT.fetch_username_to_name(toMail)
        myName=self.query.get_cell('b2')
        myUsername=self.query.get_cell('b3')
        if CLIENT.send(myUsername,myName,toMail,toName,title.get(),mail)==True:
        	status.config(text='Status > Sent')
    
    def viewmail(self,username,time,title,message):
    	self.root.config(bg='white')
    	f1=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)).place(x=0,y=0)
    	Label(self.root,text='Steller Mail',bg='white',font='verdana 20 bold').place(x=70,y=20)
    	l=Label(f1,text='↩',font='verdana 20 bold',fg='black',bg='white')
    	l.place(x=20,y=20)
    	l.bind('<Button-1>',lambda e:self.HomeScreen())
    	Frame(f1,bg='black').place(x=20,y=80,width=840,height=2)
    	Label(f1,text=username,bg='white',font='verdana 13').place(x=20,y=95)
    	Label(f1,text=title,bg='white',font='verdana 13').place(x=20,y=130)
    	Label(f1,text=time,bg='white',font='verdana 13').place(x=20,y=130+130-95)
    	Message=Text(f1,font='verdana 12')
    	Message.place(x=20,y=205,width=840,height=300)
    	Message.insert(1.0,message)
    	Message.config(state='disabled')
    	Button(f1,text='Back',bg='violet',fg='white',command=self.HomeScreen).place(x=20,y=550,width=840)
    	
		
    def HomeScreen(self):
        self.where=StringVar()
        self.root.config(bg='white')
        f1=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)).place(x=0,y=0)
        icon=Label(f1,image=self.introicon,bg='white')
        icon.image=self.introicon
        icon.place(x=20,y=40)
        searchvar=StringVar()
        searchvar.set('Search')
        search=Entry(f1,bg='black',textvariable=searchvar,fg='white',font='verdana 11',justify = CENTER)
        search.bind('<Button-1>',lambda e:searchvar.set(''))
        search.place(x=230,y=18,height=40,width=610)    
        profilephoto=ImageTk.PhotoImage(Image.open(self.profilephoto).resize((40,40), Image.ANTIALIAS))
        _profile=Label(f1,image=profilephoto,bg='white')
        _profile.image=profilephoto
        _profile.bind('<Button-1>',lambda e:Settings().Profile())
        _profile.place(x=844,y=16)
        Button(f1,text='Compose + ',font='verdana 11',command=self.ComposeMail).place(x=25,y=270,width=180)
        Button(f1,text='All',font='verdana 11',bg='forest green',fg='black',command=self.HomeScreen).place(x=25,y=310,width=180)
        Button(f1,text='Inbox',font='verdana 11',command=self.inboxScreen).place(x=25,y=350,width=180)
        Button(f1,text='Outbox',font='verdana 11',command=self.outboxScreen).place(x=25,y=390,width=180)
        Button(f1,text='Settings',font='verdana 11',command=Settings()._Settings).place(x=25,y=430,width=180)
        global panel #tells about which menu entrance is currently displaying
        self.inboxlist=Listbox(f1)
        self.inboxlist.place(x=230,y=100,height=440,width=635)
        list=CLIENT.recieve_all(self.query.get_cell('b3'))#os.listdir('databaseCore/inbox')
        list.pop(-1)
        global msg_trigger
        msg_trigger=StringVar()
        if list==[]:
        	Label(f1,text='No Mails Recieved !',bg='white',fg='red',font='verdana 30').place(x=260,y=250)
        for i in list:
        	i_=i.split('#')
        	self.inboxlist.insert(END,i_[0]+' : '+i_[0]+' > '+i_[2])
        pannel=Label(f1,text=' [All] Count:'+str(self.inboxlist.size()),bg='white',fg='red',font='verdana 11') #data for no of values/messages
        pannel.place(x=230,y=70)
        self.where.set('all')
        #self.inboxlist.bind('<Double-1>',lambda e:self.seemsg())
        self.scrollbar=Scrollbar(f1)
        self.inboxlist.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.inboxlist.yview)
        self.scrollbar.place(x=230+635+5,y=100,height=440)
        global username,stelleraddress
        username=Label(f1,text=self.query.get_cell('b2'),bg='white',font='verdana 14')
        stelleraddress=Label(f1,text=self.query.get_cell('b3'),bg='white',font='verdana 10')
        username.place(x=20,y=210)
        stelleraddress.place(x=20,y=235)       
        global status
        status=Label(self.root,text='Status > Active',bg='white',font='verdana 10')
        status.place(x=10,y=570)
        
    def seemsg(self):
    	global msg_trigger
    	msg_trigger.set(self.inboxlist.get(self.inboxlist.curselection()))
    	d=msg_trigger.get()
    	if self.where.get()=='inbox':
    		message_=CLIENT.get_msg_recv(self.query.get_cell('b3'),d)
    		self.viewmail(self.query.get_cell('b3'),d.split('#')[-1],d.split('#')[-2],message_)
    	elif self.where.get()=='outbox':
    		message_=CLIENT.get_msg_recvout(self.query.get_cell('b3'),d)
    		self.viewmail(self.query.get_cell('b3'),d.split('#')[-1],d.split('#')[-2],message_)
    	elif self.where.get()=='all':
    		message_=CLIENT.get_msg_recvall(self.query.get_cell('b3'),d)
    		self.viewmail(self.query.get_cell('b3'),d.split('#')[-1],d.split('#')[-2],message_)
    				
    def inboxScreen(self):
        global msg_trigger
        self.root.config(bg='white')
        f1=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)).place(x=0,y=0)
        icon=Label(f1,image=self.introicon,bg='white')
        icon.image=self.introicon
        icon.place(x=20,y=40)
        searchvar=StringVar()
        searchvar.set('Search')
        search=Entry(f1,bg='black',textvariable=searchvar,fg='white',font='verdana 11',justify = CENTER)
        search.bind('<Button-1>',lambda e:searchvar.set(''))
        search.place(x=230,y=18,height=40,width=610)
        profilephoto=ImageTk.PhotoImage(Image.open(self.profilephoto).resize((40,40), Image.ANTIALIAS))
        _profile=Label(f1,image=profilephoto,bg='white')
        _profile.image=profilephoto
        _profile.bind('<Button-1>',lambda e:Settings().Profile())
        _profile.place(x=780,y=16)
        Button(f1,text='Compose + ',font='verdana 11',command=self.ComposeMail).place(x=25,y=270,width=180)
        Button(f1,text='All',font='verdana 11',command=self.HomeScreen).place(x=25,y=310,width=180)
        Button(f1,text='Inbox',bg='forest green',fg='black',font='verdana 11',command=self.inboxScreen).place(x=25,y=350,width=180)
        Button(f1,text='Outbox',font='verdana 11',command=self.outboxScreen).place(x=25,y=390,width=180)
        Button(f1,text='Settings',font='verdana 11',command=Settings()._Settings).place(x=25,y=430,width=180)
        global panel #tells about which menu entrance is currently displaying
        self.inboxlist=Listbox(f1)
        self.inboxlist.place(x=230,y=100,height=440,width=635)
        self.scrollbar=Scrollbar(f1)
        self.inboxlist.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.inboxlist.yview)
        self.scrollbar.place(x=230+635+5,y=100,height=440)      
        list=CLIENT.recieve_inbox(self.query.get_cell('b3'))#os.listdir('databaseCore/inbox')
        list.pop(-1)
        if list==[]:
        	Label(f1,text='No Mails Recieved !',bg='white',fg='red',font='verdana 30').place(x=260,y=250)
        for i in list:
        	self.inboxlist.insert(END,str(i))
        pannel=Label(f1,text=' [Inbox] Count:'+str(self.inboxlist.size()),bg='white',fg='red',font='verdana 11') #data for no of values/messages
        pannel.place(x=230,y=70)
        self.where.set('inbox')
        self.inboxlist.bind('<Double-1>',lambda e:self.seemsg())
        global username,stelleraddress
        username=Label(f1,text=self.query.get_cell('b2'),bg='white',font='verdana 14')
        stelleraddress=Label(f1,text=self.query.get_cell('b3'),bg='white',font='verdana 10')
        username.place(x=20,y=210)
        stelleraddress.place(x=20,y=235)       
        global status
        status=Label(self.root,text='Status > Active',bg='white',font='verdana 10')
        _profile.place(x=844,y=16)

    def outboxScreen(self):
        self.root.config(bg='white')
        f1=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)).place(x=0,y=0)
        icon=Label(f1,image=self.introicon,bg='white')
        icon.image=self.introicon
        icon.place(x=20,y=40)
        searchvar=StringVar()
        searchvar.set('Search')
        search=Entry(f1,bg='black',textvariable=searchvar,fg='white',font='verdana 11',justify = CENTER)
        search.bind('<Button-1>',lambda e:searchvar.set(''))
        search.place(x=230,y=18,height=40,width=610)
        profilephoto=ImageTk.PhotoImage(Image.open(self.profilephoto).resize((40,40), Image.ANTIALIAS))
        _profile=Label(f1,image=profilephoto,bg='white')
        _profile.image=profilephoto
        _profile.bind('<Button-1>',lambda e:Settings().Profile())
        _profile.place(x=844,y=16)
        Button(f1,text='Compose + ',font='verdana 11',command=self.ComposeMail).place(x=25,y=270,width=180)
        Button(f1,text='All',font='verdana 11',command=self.HomeScreen).place(x=25,y=310,width=180)
        Button(f1,text='Inbox',font='verdana 11',command=self.inboxScreen).place(x=25,y=350,width=180)
        Button(f1,text='Outbox',bg='forest green',fg='black',font='verdana 11',command=self.outboxScreen).place(x=25,y=390,width=180)
        Button(f1,text='Settings',font='verdana 11',command=Settings()._Settings).place(x=25,y=430,width=180)
        global panel #tells about which menu entrance is currently displaying
        self.inboxlist=Listbox(f1)
        self.inboxlist.place(x=230,y=100,height=440,width=635)
        list=CLIENT.recieve_outbox(self.query.get_cell('b3'))#os.listdir('databaseCore/inbox')
        global msg_trigger
        list.pop(-1)
        if list==[]:
        	Label(f1,text='No Mails Sent!',bg='white',fg='red',font='verdana 30').place(x=260,y=250)

        for i in list:
        	self.inboxlist.insert(END,str(i))
        pannel=Label(f1,text=' [Outbox] Count:'+str(self.inboxlist.size()),bg='white',fg='red',font='verdana 11') #data for no of values/messages
        pannel.place(x=230,y=70)
        self.where.set('outbox')
        self.inboxlist.bind('<Double-1>',lambda e:self.seemsg())
        self.scrollbar=Scrollbar(f1)
        self.inboxlist.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.inboxlist.yview)
        self.scrollbar.place(x=230+635+5,y=100,height=440)       
        global username,stelleraddress
        username=Label(f1,text=self.query.get_cell('b2'),bg='white',font='verdana 14')
        stelleraddress=Label(f1,text=self.query.get_cell('b3'),bg='white',font='verdana 10')
        username.place(x=20,y=210)
        stelleraddress.place(x=20,y=235)
     
class Settings(Main):
    def __init__(self):
        super().__init__(root)
        
    def logout(self):
    	self.query.update('b2','0')
    	self.query.update('b3','0')
    	self.query.update('b4','0')
    	self.query.update('b5','0')
    	self.query.update('b6','0')
    	self.query.update('b7','0')
    	self.query.update('b8','offline')
    	self.query.save()
    	self.Login()
    	
    def _Settings(self):
        mainFrame=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)-30).place(x=0,y=0)
        Label(mainFrame,text='Application Settings',bg='white',fg='grey40',font='verdana 14').place(x=20,y=55)
        Button(mainFrame,text='< Back',bg='white',fg='grey40',font='verdana 10',command=Screens().HomeScreen).place(x=20,y=20)
        Button(mainFrame,text='LogOut',bg='white',fg='grey60',command=self.logout).place(x=20,y=120,width=700)
    def Profile(self):
        mainFrame=Frame(self.root,bg='white',width=int(self.width),height=int(self.height)-30).place(x=0,y=0)
        Label(mainFrame,text='My Profile',bg='white',fg='grey40',font='verdana 17').place(x=20,y=55)
        Button(mainFrame,text='< Back',bg='white',fg='grey40',font='verdana 10',command=Screens().HomeScreen).place(x=20,y=20)
        profilephoto=ImageTk.PhotoImage(Image.open(self.profilephoto).resize((200,200), Image.ANTIALIAS))
        _profile=Label(mainFrame,image=profilephoto,bg='white')
        _profile.image=profilephoto
        _profile.place(x=20,y=100)
        Label(mainFrame,text='Edit Profile',font='verdana 10',bg='white',fg='black').place(x=85,y=302)
        Label(mainFrame,text=self.query.get_cell('b2'),font='verdana 13 bold',bg='white',fg='black').place(x=50,y=330)
        Label(mainFrame,text='Username : '+self.query.get_cell('b3'),font='verdana 12',bg='white',fg='black').place(x=50,y=360)
        Label(mainFrame,text='Age : '+str(self.query.get_cell('b4')),font='verdana 12',bg='white',fg='black').place(x=50,y=390)
        Label(mainFrame,text='Sex : '+str(self.query.get_cell('b5')),font='verdana 12',bg='white',fg='black').place(x=50,y=420)
        Label(mainFrame,text='Contact : '+str(self.query.get_cell('b6')),font='verdana 12',bg='white',fg='black').place(x=50,y=450)
            
if __name__=='__main__':
    root=Tk()
    stellerx=Main(root)
    stellerx.INTRO()
    root.update_idletasks()
    time.sleep(1.5)
    stellerx.start()
    root.mainloop()

