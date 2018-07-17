import random
def func():
    A=random.choice(["Apple","Orange","Grape","Banana","Guava"])   #隨機挑選1種水果

    if A!="Apple":                                                 #若A不是Apple，則發生ValueError
      raise ValueError('Catch the wrong stuff!!')
    
    try:
      print(A)
    except Exception:
        print('Catch the wrong stuff!!')
func()                                   #function call
