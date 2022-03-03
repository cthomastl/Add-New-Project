from tkinter import*
import sqlite3

root = Tk()
root.title("Add a project")
# Database

# Create a datbase
conn = sqlite3.connect('add_project.db')
# Create Cursur
c = conn.cursor()



# c.execute("""CREATE TABLE project(project_name, vendor_name)""")
	

	
	# create submit button 
def submit():
	# Create a datbase
	conn = sqlite3.connect('add_project.db')
	# Create Cursur
	c = conn.cursor()

	c.execute("INSERT INTO project VALUES (:p_name, :v_name)",
{
				'p_name' : p_name.get(),
				'v_name' : p_name.get(),

})

	#Commit changes
	conn.commit()
	# Close Connection
	conn.close()
    
    # Insert into table


		# Clear text box 
	p_name.delete(0, END)
	v_name.delete(0, END)

def query():
		
# Create a datbase
	conn = sqlite3.connect('add_project.db')
# Create Cursur
	c = conn.cursor()
#Query DB 
	c.execute("SELECT * FROM project")
records = c.fetchall()
print(records)


#Commit changes
conn.commit()
	# Close Connection



	#Text box
p_name = Entry(root, width=30)
p_name.grid(row=0, column=1, padx=20)

v_name = Entry(root, width=30)
v_name.grid(row=1, column=1, padx=20)
    # Text box labels 
p_name_label = Label(root, text="Project Name")
p_name_label.grid(row=0, column=0)

p_name_label = Label(root, text="Vendor Name")
p_name_label.grid(row=1, column=0)

	# Submit button
submit_btn =Button(root, text="Add Project", command= submit)
submit_btn.grid(row=6,column =0, columnspan=2, pady =10, padx=10, ipadx = 100)

#Create a query button 
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit changes
conn.commit()
# Close Connection
conn.close()

root.mainloop()
