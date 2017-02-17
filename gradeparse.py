from bs4 import BeautifulSoup
import mechanize
import getpass

br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in=br.open("https://www.iitm.ac.in/viewgrades/")
br.select_form(nr=0)

print "\n"

br["rollno"]=raw_input("Enter username : ")
br["pwd"]=getpass.getpass("Enter password : ")
login=br.submit()

links=[]
for link in br.links() : 
    links.append(link)


request=br.click_link(links[1])
response=br.follow_link(links[1])

str=response.read()

soup=BeautifulSoup(str,'html.parser')

a=soup.findAll("tr")
b=[]
for i in a : 
	b.append(i.findAll("td"))

number=[]
coursenumber=[]
coursename=[]
coursetype=[]
credits=[]
grade=[]
attendance=[]

b=b[3:]

for j in b :
    if(len(j)==7) : 
    	number.append(j[0])
    	coursenumber.append(j[1])
        coursename.append(j[2])
        coursetype.append(j[3])
        credits.append(j[4])
        grade.append(j[5])
        attendance.append(j[6])

number1=[]
coursenumber1=[]
coursename1=[]
coursetype1=[]
credits1=[]
grade1=[]
attendance1=[]

for t in number : 
    number1.append(t.getText())

for t in coursenumber : 
    coursenumber1.append(t.getText())

for t in coursename : 
    coursename1.append(t.getText())

for t in coursetype : 
    coursetype1.append(t.getText())

for t in credits :
    credits1.append(t.getText())

for t in grade :
    grade1.append(t.getText())

for t in attendance : 
    attendance1.append(t.getText())

dict1=[]
for p in range(0,len(number)):
        d={}
        d["Number"]=number1[p]
        d["CourseNumber"]=coursenumber1[p]
        d["CourseName"]=coursename1[p]
        d["CourseType"]=coursetype1[p]
        d["Credits"]=credits1[p]
        d["Grade"]=grade1[p]
        d["Attendance"]=attendance1[p]
        dict1.append(d)

for k in dict1 : 
	print k,'\n'