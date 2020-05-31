from tkinter import *
import sqlite3

top=Tk()
top.title("Mainpage")
top.geometry("400x400")
top.iconbitmap("address.ico")




def click():
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	c.execute(" INSERT INTO addresses VALUES (:first_name, :last_name, :city, :state, :country, :pin_code)",

			{
				"first_name": f_name.get(),
				"last_name": l_name.get(),
				"city": city_name.get(),
				"state": s_name.get(),
				"country": country_name.get(),
				"pin_code": p_num.get(),


			})

	conn.commit()
	conn.close()



	f_name.delete(0,END)
	l_name.delete(0,END)
	city_name.delete(0,END)
	s_name.delete(0,END)
	country_name.delete(0,END)
	p_num.delete(0,END)

def all():
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	c.execute("SELECT *, oid FROM addresses")
	re=c.fetchall()
	w=''
	for i in re:
		for j in i:
			w+=str(j)+" "
		l=Label(de,text=w).pack()
		w=''

	conn.commit()
	conn.close()

def single():
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	c.execute("SELECT *, oid FROM addresses")
	re=c.fetchall()
	for i in re:
		if i[0]==en.get():
			ls=Label(de,text=i).pack()


	conn.commit()
	conn.close()


def detail():
	
	global en,de
	de=Toplevel()
	de.geometry("600x600")
	de.title("Detail")
	de.iconbitmap("address.ico")
	l=Label(de,text="Enter first name whose detail you want").pack()
	en=Entry(de)
	en.pack()
	db=Button(de,text="Click to find detail",command=single,padx=30,pady=15)
	db.pack()
	db1=Button(de,text="click to find all details",command=all,padx=30,pady=15)
	db1.pack()
	db2=Button(de,text="Back to main page",command=de.destroy,padx=30,pady=15)
	db2.pack()
	d=Entry()
def go():
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	r=ze.get()
	c.execute("DELETE FROM addresses WHERE oid="+r)
	ze.delete(0,END)
	y=Label(de1,text="Deleted successfully").pack()
	conn.commit()
	conn.close()

def delete():
	global de1,ze
	de1=Toplevel()
	de1.geometry("600x600")
	de1.title("Delete entry")
	de1.iconbitmap("address.ico")
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	c.execute("SELECT *, oid FROM addresses")
	re=c.fetchall()
	w=''
	for i in re:
		for j in i:
			w+=str(j)+" "
		l=Label(de1,text=w).pack()
		w=''
	z=Label(de1,text="enter id you want to delete").pack()
	ze=Entry(de1)
	ze.pack()
	zb=Button(de1,text="Enter",command=go).pack()
	zb1=Button(de1,text="Back to main page",command=de1.destroy).pack()

	conn.commit()
	conn.close()

	

def entry():
	root=Toplevel()
	root.title("Address Book new entry")
	root.iconbitmap('address.ico')
	root.geometry("400x400")
	global f_name,l_name,city_name,country_name,s_name,p_num
	

	f=Label(root,text="First name",padx=40).grid(row=0,column=0)
	f_name=Entry(root,width=40,borderwidth=5)
	f_name.grid(row=0,column=1)

	l=Label(root,text="Last name").grid(row=1,column=0)
	l_name=Entry(root,width=40,borderwidth=5)
	l_name.grid(row=1,column=1)

	city=Label(root,text="City").grid(row=2,column=0)
	city_name=Entry(root,width=40,borderwidth=5)
	city_name.grid(row=2,column=1)

	s=Label(root,text="State").grid(row=3,column=0)
	s_name=Entry(root,width=40,borderwidth=5)
	s_name.grid(row=3,column=1)

	contry=Label(root,text="Country").grid(row=4,column=0)
	country_name=Entry(root,width=40,borderwidth=5)
	country_name.grid(row=4,column=1)

	p=Label(root,text="PIN").grid(row=5,column=0)
	p_num=Entry(root,width=40,borderwidth=5)
	p_num.grid(row=5,column=1)



	but=Button(root,text="Enter",padx=60,command=click).grid(row=6,column=0,columnspan=2)
	but1=Button(root,text="Back to main page",padx=60,command=root.destroy).grid(row=7,column=0,columnspan=2)

	root.mainloop()

def c1():
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	

	c.execute("""UPDATE addresses SET
			first_name= :first,
			last_name= :last,
			city= :city,
			state= :state,
			country= :country,
			pin_code= :pin

			WHERE oid= :oid""",
			{
				'first':f1_name.get(),
				'last':l1_name.get(),
				'city':c1ity_name.get(),
				'state':s1_name.get(),
				'country':c1ountry_name.get(),
				'pin':p1_num.get(),
				'oid':p1

			}
			)
	
	

	conn.commit()
	conn.close()


def d():
	up1=Toplevel()
	up1.title("Enter ID")
	up1.iconbitmap('address.ico')
	up1.geometry("400x400")
	global i1_name
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	
	i=Label(up1,text="ID",padx=40).grid(row=0,column=0)
	i1_name=Entry(up1,width=40,borderwidth=5)
	i1_name.grid(row=0,column=1)
	
	c.execute("SELECT *, oid FROM addresses")
	re=c.fetchall()
	
	w=''
	for i in re:
		for j in i:
			w+=str(j)+" "
		l=Label(up1,text=w).grid(row=3,column=0,columnspan=2)
		w=''

	conn.commit()
	conn.close()
	but12=Button(up1,text="Get details",padx=60,command=update).grid(row=1,column=0,columnspan=2)
	but123=Button(up1,text="Back to main page",padx=60,command=up1.destroy).grid(row=2,column=0,columnspan=2)


def update():
	up=Toplevel()
	up.title("Update Entry")
	up.iconbitmap('address.ico')
	up.geometry("400x400")
	global f1_name,l1_name,c1ity_name,c1ountry_name,s1_name,p1_num,i1_name,p1
	p1=i1_name.get()
	conn=sqlite3.connect('data_base1.db')
	c=conn.cursor()
	c.execute("SELECT *, oid FROM addresses")
	re=c.fetchall()
	

	w=''
	for i in re:
		for j in i:
			w+=str(j)+" "
		l=Label(up,text=w).grid(row=10,column=0,columnspan=2)
		w=''

	
	
	c.execute("SELECT * FROM addresses WHERE oid="+p1)
	records=c.fetchall()

	f=Label(up,text="First name",padx=40).grid(row=2,column=0)
	f1_name=Entry(up,width=40,borderwidth=5)
	f1_name.grid(row=2,column=1)

	l=Label(up,text="Last name").grid(row=3,column=0)
	l1_name=Entry(up,width=40,borderwidth=5)
	l1_name.grid(row=3,column=1)

	city=Label(up,text="City").grid(row=4,column=0)
	c1ity_name=Entry(up,width=40,borderwidth=5)
	c1ity_name.grid(row=4,column=1)

	s=Label(up,text="State").grid(row=5,column=0)
	s1_name=Entry(up,width=40,borderwidth=5)
	s1_name.grid(row=5,column=1)

	contry=Label(up,text="Country").grid(row=6,column=0)
	c1ountry_name=Entry(up,width=40,borderwidth=5)
	c1ountry_name.grid(row=6,column=1)

	p=Label(up,text="PIN").grid(row=7,column=0)
	p1_num=Entry(up,width=40,borderwidth=5)
	p1_num.grid(row=7,column=1)

	for record in records:
		f1_name.insert(0,record[0])
		l1_name.insert(0,record[1])
		c1ity_name.insert(0,record[2])
		c1ountry_name.insert(0,record[3])
		s1_name.insert(0,record[4])
		p1_num.insert(0,record[5])


	conn.commit()
	conn.close()
	but1=Button(up,text="Enter",padx=60,command=c1).grid(row=8,column=0,columnspan=2)
	
	but11=Button(up,text="Back to main page",padx=60,command=up.destroy).grid(row=9,column=0,columnspan=2)

	




button=Button(top,text="New Entry",command=entry,padx=50,pady=20).pack()
button1=Button(top,text="Details",command=detail,padx=50,pady=20).pack()
button4=Button(top,text="Update Entry",command=d,padx=50,pady=20).pack()
button3=Button(top,text="Delete entry",command=delete,padx=50,pady=20).pack()
button2=Button(top,text="EXIT",command=top.quit,padx=50,pady=20).pack()




top.mainloop()



