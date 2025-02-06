#i didnt understand, completed together in class.
MATRIX_STRING = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''
#steps 
# 1 create 2d list 
# 2 decript with for loop to check isalpha
# replace non characters by space
# output should be stiring 
matrix=[]

# for i in range(len(MATRIX_STRING)):
#     #row= list(Marix_string[i:i+3])
#     Marix_string
#     print(row)
#     matrix.append(row)
# print(matrix)
rows=MATRIX_STRING.split('\n')
#print(rows)
for row in rows:
    matrix.append(list(row))
#print(matrix)
for column in matrix:
    column_0=[column[0] for column in matrix]
    column_1=[column[1] for column in matrix]
    column_2=[column[2] for column in matrix]
column_matrix=[]
column_matrix.append(column_0)
column_matrix.append(column_1)
column_matrix.append(column_2)
#print (column_matrix)
#ourput stiring put ok 
output_string =''
for col_list in column_matrix:
    #print(sublist)
    for i in range(len(col_list)):
        #print(char)
        if col_list[i].isalpha():
            output_string+= col_list[i]
        else:
            if len(output_string) !=0 and output_string[-1]!=' ':
                output_string+=' '
print(output_string)