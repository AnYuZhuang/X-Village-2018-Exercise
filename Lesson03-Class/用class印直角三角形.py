class Shape:
     #edge=5
     def set_edge(self,edge_arg):
        self.edge_arg=edge_arg
     def display(self):
        i=1
        j=1
        while i<=self.edge_arg:
            while j<=self.edge_arg:
               if i<j:
                break
               print("*",end="\t")
               j+=1
            print('')
            j=1
            i+=1 
x=Shape()
x.set_edge(5)
x.display()