file=open('DEMO.txt')
print(file.read())
file.close()
#open the file in read mode
file_read=open('DEMO.txt','r')
print('File in read mode - ')
print(file_read.read())
file_read.close()           

file_write=open('DEMO.txt','w')
file_write.write('File in write mode - ')
file_write.write("Im arham ")
file_write.close()       

file_append=open('DEMO.txt','a')
file_append.write('File in append mode - ')
file_append.write("Im arham ")
file_append.close()     
