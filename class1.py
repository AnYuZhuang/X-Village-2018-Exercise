'''
class map:
    n="[*,*]"
    def set_map(self,n):

     def set_pattern(self,p):
       if p==1:
           print(n) 
       def display(self):

a=map()
a.set_pattern(1)
'''
class Map():
  n = 5
  
  def set_map(self,n):
    #test_list=[ ['*'] * n for i in range(n) ]
    #print(test_list)
    self.test_list=[]
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[1].append('*')
    self.test_list[1].append('*')
    self.test_list[1].append('*')
    self.test_list[1].append('*')
    self.test_list[1].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    #print(test_list)
    p=1
  def set_pattern(self,p):
    self.test_list=[]
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list.append([])
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[0].append('*')
    self.test_list[1].append('*')
    self.test_list[1].append('0')
    self.test_list[1].append('0')
    self.test_list[1].append('0')
    self.test_list[1].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('0')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[2].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[3].append('0')
    self.test_list[3].append('*')
    self.test_list[3].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    self.test_list[4].append('*')
    #print(test_list)

  def display(self):
    print(self.test_list)

my_map = Map()
my_map.set_map(5)
my_map.display()
my_map.set_pattern(1)
my_map.display()


