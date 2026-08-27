#first i will create a file name experiment.txt
'''open("Experiment.txt","xt")'''
#-----------------------------------------------------------
file_handler=open("Experiment.txt","wt")
file_handler.write("""------------------About Myself--------------------
1: Name: Ayush Kumar
2: Age: 21
3: Course: BS Computer Science & Data Analytics
4: College: Indian Institute of Technology Patna.""")
#-------------------------------------------------------------
file_handler.close()
file_handler=open("Experiment.txt","rt")
print(file_handler.read())
file_handler.close()
#-------------------------------------------------------------
file_handler=open("Experiment.txt","at")
file_handler.write("\n5: Address: Delhi NCR\n")
file_handler.write("6: Experience: Intern India Space Academy\n")
file_handler.write("---------------------------------------------------")
file_handler.close()

