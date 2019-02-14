
# coding: utf-8

# In[1]:


import numpy as np

# # Allowed moves = right, down, up diagonal left

#Logic used
'''       
    start [n,n]
    
    do ->    right [n+1,n]=1 only if mat[n+1,n]==0 AND ma[n+1,n] exists else next,
             down  [n,n+1]=1 only if mat[n,n+1]==0 AND ma[n,n+1]exists else next,
         upper diag left [n-1,n-1]=1 only if mat[n-1,n-1]==0 AND ma[n-1,n-1] exists else next loop.
             

'''


# In[196]:


def find(y,x,matx,sol):
    if y>=0 and x>=0:
        
        matx[y,x]=1

        print('Position',y,x)

        print('matrix \n',matx)
        print('----------------')
    #right
        if 0 <= y+1 <= n-1 and x<=n-1 and matx[y+1,x]== 0:
            matx[y+1,x] = 1
            sol.append('right')
            return find(y+1,x,matx,sol)
    #down        
        elif 0 <= x+1 <= n-1 and y<=n-1 and matx[y,x+1]==0:
            matx[y,x+1]= 1
            sol.append('down')
            return find(y,x+1,matx,sol)

    #diagonal upleft
        elif 0 <= y-1<=n-1 and x-1<=n-1 and matx[y-1,x-1]==0:
            matx[y-1,x-1]= 1
            sol.append('diagonal upper left')
            return find(y-1,x-1,matx,sol)

        elif np.array_equal(matx,np.ones((n,n))):

            print('***************** This is a solution*****************',
                '\n..................................................',
                '\n** Starting position=',a,b,'\n',
                  '**Steps = ',sol,'**\n',
                  '******************************************************') 
        else:
            print('try other')


# In[202]:


n = 3
for a in range(0,n):
    for b in range(0,n):
                print(a,b) 
                mat = np.zeros((n,n))
                solu = ['a']
                print('------------------------------------------------------------------------------------')
                print('Trying for y=',a,'and x=',b)
                print('------------------------------------------------------------------------------------')
                find(a,b,mat,solu)
                print('-------------------------')

