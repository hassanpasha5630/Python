#Problem6 
#------------------------------------------------------------------------------------------------------------------------
# I am using the simialr logic of KML algorithm + prefix + pointer memorization this aslgo was referenced and leanred from 
# multiple websites including stackoverflow,blogs to understand the benifits of the inner+ recurssive function
# Reference: stackoverflow. To help with some syntax issues
# 
#------------------------------------------------------------------------------------------------------------------------


def occurance_of_string(strs, token):
    m, Memory = len(strs), {}
    length_of_token = len(token)
    #calling innerfunction to count 
    def count_occurance(i, j):
        if j == length_of_token:
            return 1
        elif i == m:
            return 0
        k = (i, j)
        if k not in Memory:
            if(strs[i] == token[j]):
              result = count_occurance(i+1, j) + count_occurance(i+1, j+1)
            else:
              result = count_occurance(i+1, j) + 0
            Memory[k] = result
        return Memory[k]
    return count_occurance(0, 0)


def usrinput():
  userinput = input("Enter input : as seq.txt :  ")
  return userinput

def file_reader(inputs):

  Output = [] 
  string_holder = [] 
  Temp = []
  input_file =  open(inputs,"r") 

  for x in input_file:
    
    final_string = x.replace(" ","")
    final_string = final_string.replace("\n","")
    string_holder.append(final_string)
  
  #Using innerfunciton as a safety net 
  def seq():  
    y= 0
    for x in string_holder :
        Output.append(occurance_of_string(x,"jointhenmiteam"))    
   
    y= 0
    for x in Output :
        #trailing zeros and get only the last 5 digits 
        print("Output: ", y,":",'{0:05d}'.format(abs(x)%100000))
        print('\n')
        y = y +1 


  #calling innerfunciton      
  seq()

#-----------------Main Function ---------------------------#

def main():
  inputs = usrinput()
  file_reader(inputs)

#----------------------------------------------------------#
main()