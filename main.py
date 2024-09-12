# get_doc_info.py
import os
import csv
from PyPDF2 import PdfReader
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        info = pdf.metadata
        number_of_pages = len (pdf.pages)
        page1 = ""
        
        academic_advising = 0
        evaluation_committee = 0
        internships_DR_SP = 0
        work_supervision = 0
        course_credit_load = 0
        credit_load_reassignment = 0
        name = ''
        term = ''
        year = 0
        
       # print(info)
        for i in range (number_of_pages):
            page = pdf.pages[i]
            page1 += page.extract_text()
                 
        #Extract Name
        name_end = page1.find("Name") + 5
        cofo_email_start = page1.find("COFO ID") - 1
        print ("Name: " + page1[name_end:cofo_email_start])
        name = page1[name_end:cofo_email_start]
        
        #Extract Term
        term_end = page1.find("Term") + 4
        print ("Term: " + page1[term_end+2:term_end + 6])
        term = page1[term_end+2:term_end + 6]
        
        #Extract Year
        year_end = page1.find("Year") + 4
        print ("Year: " + page1[year_end+2:year_end + 6])
        year = page1[year_end+2:year_end + 6]
        
        #Number Advises
        num_advises = page1.find("Number of primary advises for this current semester:") + 53
        print ("Num Advisees: " + page1[num_advises:num_advises + 2])
        
        academic_advising = int(page1[num_advises:num_advises + 2])
        
        if academic_advising <= 9:
            credit_load_reassignment += 0
        elif academic_advising <= 24:
            credit_load_reassignment += 1
        elif academic_advising <= 40:
            credit_load_reassignment += 2
        else:
            credit_load_reassignment += 3

        
        #Number Student Workers
        num_stuWorkers = page1.find("Number of student workers supervised and claimed for credit-load reassignment:") + 79
        num_interns = page1.find("Number of Internships, Directed Readings, Special Problems thus far this academic year")
        print ("Num Studet Workers: " + page1[num_stuWorkers:num_interns - 1])
        work_supervision = int(page1[num_stuWorkers:num_interns - 1])
        
        if work_supervision == 0:
            credit_load_reassignment += 0
        elif work_supervision <= 4:
            credit_load_reassignment += 1
        elif work_supervision <= 8:
            credit_load_reassignment += 2
        else:
            credit_load_reassignment += 3
        
        #Number of Interns
        print ("Num of Internships, etc.: " + page1[num_interns + 114:num_interns + 115])
        internships_DR_SP = int(page1[num_interns + 114:num_interns + 115])
        
        if internships_DR_SP <= 4:
            credit_load_reassignment += 0
        elif internships_DR_SP <= 10:
            credit_load_reassignment += 1
        elif internships_DR_SP <= 20:
            credit_load_reassignment += 2
        else:
            credit_load_reassignment += 3
        
        #Course Load
        courseLoad1 = page1.find("C r e d i t s") + 14
        courseLoad2 = page1.find("\n2", courseLoad1)
        courseLoad3 = page1.find("\n3", courseLoad2)
        courseLoad4 = page1.find("\n4", courseLoad3)
        courseLoad5 = page1.find("\n5", courseLoad4)
        
        courseLoad_1 = (page1[courseLoad1:courseLoad2])
        try:
            print (courseLoad_1[-3])
            if "2" in courseLoad_1[10:-4]:
                print("2 sections")
                if int(courseLoad_1[-3]) != 6:
                    course_credit_load += int(courseLoad_1[-3]) * 2
                else:
                    course_credit_load += int(courseLoad_1[-3])
            elif "3" in courseLoad_1[10:-4]:
                print("3 sections")
                if int(courseLoad_1[-3]) != 9:
                    course_credit_load += int(courseLoad_1[-3]) * 3
                else:
                    course_credit_load += int(courseLoad_1[-3])
            elif "4" in courseLoad_1[10:-4]:
                print("4 sections")
                if int(courseLoad_1[-3]) != 12:
                    course_credit_load += int(courseLoad_1[-3]) * 4
                else:
                    course_credit_load += int(courseLoad_1[-3])
            else:
                print ("1 section")
                course_credit_load += int(courseLoad_1[-3])
        except IndexError:
            print("Index out of range! Check your indexing.")

        courseLoad_2 = (page1[courseLoad2:courseLoad3])
        try:
            print (courseLoad_2[-3])
            if "2" in courseLoad_2[10:-4]:
                print("2 sections")
                if int(courseLoad_2[-3]) != 6:
                    course_credit_load += int(courseLoad_2[-3]) * 2
                else:
                    course_credit_load += int(courseLoad_2[-3])
            elif "3" in courseLoad_2[10:-4]:
                print("3 sections")
                if int(courseLoad_2[-3]) != 9:
                    course_credit_load += int(courseLoad_2[-3]) * 3
                else:
                    course_credit_load += int(courseLoad_2[-3])
            elif "4" in courseLoad_2[10:-4]:
                print("4 sections")
                if int(courseLoad_2[-3]) != 12:
                    course_credit_load += int(courseLoad_2[-3]) * 4
                else:
                    course_credit_load += int(courseLoad_2[-3])
            else:
                print ("1 section")
                course_credit_load += int(courseLoad_2[-3])
        except IndexError:
            print("Index out of range! Check your indexing.")
            
        courseLoad_3 = (page1[courseLoad3:courseLoad4])
        try:
            print (courseLoad_3[-3])
            if "2" in courseLoad_3[10:-4]:
                print("2 sections")
                if int(courseLoad_3[-3]) != 6:
                    course_credit_load += int(courseLoad_3[-3]) * 2
                else:
                    course_credit_load += int(courseLoad_3[-3])
            elif "3" in courseLoad_3[10:-4]:
                print("3 sections")
                if int(courseLoad_3[-3]) != 9:
                    course_credit_load += int(courseLoad_3[-3]) * 3
                else:
                    course_credit_load += int(courseLoad_3[-3])
            elif "4" in courseLoad_3[10:-4]:
                print("4 sections")
                if int(courseLoad_3[-3]) != 12:
                    course_credit_load += int(courseLoad_3[-3]) * 4
                else:
                    course_credit_load += int(courseLoad_3[-3])
            else:
                print ("1 section")
                course_credit_load += int(courseLoad_3[-3])
        except IndexError:
            print("Index out of range! Check your indexing.")
        
        courseLoad_4 = (page1[courseLoad4:courseLoad5])
        try:
            print (courseLoad_4[-3])
            if "2" in courseLoad_4[10:-4]:
                print("2 sections")
                if int(courseLoad_4[-3]) != 6:
                    course_credit_load += int(courseLoad_4[-3]) * 2
                else:
                    course_credit_load += int(courseLoad_4[-3])
            elif "3" in courseLoad_4[10:-4]:
                print("3 sections")
                if int(courseLoad_4[-3]) != 9:
                    course_credit_load += int(courseLoad_4[-3]) * 3
                else:
                    course_credit_load += int(courseLoad_4[-3])
            elif "4" in courseLoad_4[10:-4]:
                print("4 sections")
                if int(courseLoad_4[-3]) != 12:
                    course_credit_load += int(courseLoad_4[-3]) * 4
                else:
                    course_credit_load += int(courseLoad_4[-3])
            else:
                print ("1 section")
                course_credit_load += int(courseLoad_4[-3])
        except IndexError:
            print("Index out of range! Check your indexing.")
        
        courseLoad_5 = (page1[courseLoad5:term_end - 5])
        try:
            print (courseLoad_5[-3])
            if "2" in courseLoad_5[10:-4]:
                print("2 sections")
                if int(courseLoad_5[-3]) != 6:
                    course_credit_load += int(courseLoad_5[-3]) * 2
                else:
                    course_credit_load += int(courseLoad_5[-3])
            elif "3" in courseLoad_5[10:-4]:
                print("3 sections")
                if int(courseLoad_5[-3]) != 9:
                    course_credit_load += int(courseLoad_5[-3]) * 3
                else:
                    course_credit_load += int(courseLoad_5[-3])
            elif "4" in courseLoad_5[10:-4]:
                print("4 sections")
                if int(courseLoad_5[-3]) != 12:
                    course_credit_load += int(courseLoad_5[-3]) * 4
                else:
                    course_credit_load += int(courseLoad_5[-3])
            else:
                print ("1 section")
                course_credit_load += int(courseLoad_5[-3])
        except IndexError:
            print("Index out of range! Check your indexing.")
            
        print("Total Course load: " + str(course_credit_load))
        print("Total Credit-Load Reassignment: " + str(credit_load_reassignment))
        
        return [name, term, year, academic_advising, work_supervision, internships_DR_SP, course_credit_load, credit_load_reassignment]
                
if __name__ == '__main__':
   # path = 'hall_clr.pdf'
   # path = 'CLR_Sample.pdf'
   with open('test.csv', 'w') as output_file:
       
       writer = csv.writer(output_file)
       
       header = ['Name', 'Term', 'Year', 'Number of Advisees', 'Work Supervision', 'Internships', 'Total Course Credit Load', 'Total Credit Load Reassignment']
       
       writer.writerow(header)
       
       files = [f for f in os.listdir('.') if os.path.isfile(f)]
       for f in files:
           if f.endswith('.pdf'):
               #get_info(f)
               writer.writerow(get_info(f))
