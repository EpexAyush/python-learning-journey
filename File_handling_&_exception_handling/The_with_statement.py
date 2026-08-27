'''This is simply opening a file manually without the with statement.'''
#Opening a file
file_handler=open("Experiment.txt","rt")
#Reading all content
content=file_handler.read()
#Closing a file
file_handler.close()  #also we are closing a file manually.
print(content)

'''Using the with statement we can do this same thing and also code will be more readable and we don't have to required to close file manually.'''
with open("Experiment.txt","rt") as file_handler:
    content=file_handler.read()
#file will close automatically as we move out from the with statement code block.

print(content)

#-----------------------------------------------------------------------------------------------------
#creating a new file using a with statement
with open("Experiment_2.txt","wt") as fh:
    cont=fh.write("This is a new file named as Experiment_2.txt created on 28 August 2026 at 12:15 AM.")