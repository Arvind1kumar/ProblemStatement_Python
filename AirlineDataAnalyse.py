def Experiment(filepath):
    List=[]
    # file reading 
    with open(filepath,'r') as file:  
      ls=file.readlines()[1:]
      List=[value.split('"')[1] for value in ls]

    # most frequent count
    maxvalue,minvalue=max(List, key = List.count),min(List, key = List.count)
    maxcount,mincount=0,0
    for element in List:
      if element==maxvalue:
        maxcount+=1
      elif element==minvalue:
        mincount+=1
    return dict({maxvalue:maxcount,minvalue:mincount})
    
data=Experiment(filepath='airlines.csv')
print(data)
