#!/usr/bin/env python
# coding: utf-8

# # LINKED LIST

# ### Implenetation of stack using linked list

# In[1]:


# considered top of stack as head of linked list


# In[8]:


class Linked_stack:
    class Node:
        __slot__='element,next'
        
        def __init__(self,element,nexte):
            self.element=element
            self.next=nexte
            
    def __init__(self):
        self.head=None
        self.size=0
     
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
    
    
    def push(self, val):
        new= self.Node(val, self.head)
        self.head=new
        self.size+=1
        
    def top(self):
        if self.is_empty():
            print("stack is empty")
            return
        return self.head.element
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return
        ans=self.head.element
        self.head=self.head.next
        self.size-=1
        return ans
    
    
        
        


# In[9]:


S=Linked_stack()


# In[10]:


S.top()


# In[11]:


S.push(10)


# In[12]:


S.top()


# In[13]:


S.push(20)


# In[14]:


S.top()


# In[15]:


S.is_empty()


# In[16]:


S.size


# In[17]:


S.head


# In[18]:


S.pop()


# In[19]:


S.pop()


# In[20]:


S.pop()


# ### implementation of queue using linked list

# ###### head- front deletion,   tail-read insertion

# In[1]:


class Linked_queue:
    class Node:
        __slot__='element,next'
        
        def __init__(self,element,nexte):
            self.element=element
            self.next=nexte
            
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
    
    def first(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.head.element
    
    def last(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.tail.element
    
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        answer=self.head.element
        self.head=self.head.next
        self.size-=1
        return answer
    
    def enqueue(self,val):
        new=self.Node(val,None)
        if self.is_empty():
            self.head=new
        else:
            self.tail.next=new
        self.tail=new    
        self.size+=1
        
    def display(self):
        start=self.head
        while start!=None:
            print(start.element, end=' ')
            start=start.next
        
        


# In[13]:


S=Linked_queue()


# In[14]:


S.first()


# In[15]:


S.head


# In[16]:


S.dequeue()


# In[17]:


S.enqueue(10)


# In[18]:


S.enqueue(20)


# In[19]:


S.display()


# ##### Circular implementation

# In[13]:


class CircularQueue:
    class Node:
        __slot__='element,next'
        
        def __init__(self,element,nexte):
            self.element=element
            self.next=nexte
    
    def __init__(self):
        self.tail=None
        self.size=0
      
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
    
    def first(self):
        if self.is_empty():
            print("queue is empty")
            return
        head=self.tail.next
        return head.element
    
        
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        head=self.tail.next
        if self.size==1:
            self.tail=None
        else:
            self.tail.next=head.next
        self.size-=1
        return head.element
    
    def enqueue(self,val):
        new=self.Node(val,None)
        if self.is_empty():
            new.next=new
        else:
            new.next=self.tail.next
            self.tail.next=new
        self.tail=new
        self.size+=1
        
    def rotate(self):
        if self.size>0:
            self.tail=self.tail.next
            
        
        
        
    


# In[14]:


S=CircularQueue()


# In[15]:


S.enqueue(10)


# In[16]:


S.enqueue(20)


# In[17]:


S.enqueue(30)


# In[18]:


S.first()


# In[19]:


S.tail.element


# In[25]:


S.rotate()


# In[11]:


S.tail.element


# ###  Doubly Linked List

# In[65]:


class DoublyLinkedList:
    class Node:
        def __init__(self, element):
            self.element=element
            self.prev=None
            self.next=None
            
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size==0
    
    def get_Node(self,index):
        current=self.head
        for i in range(index):
            if current is None:
                return None
            
            current=current.next
        return current
    
    def insert_at_beg(self,val):
        new=self.Node(val)
        if self.is_empty():
            self.head=new
            self.tail=new
            
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new
            
        self.size+=1    
    
    
    def insert_at_last(self,val):
        new=self.Node(val)
        if self.is_empty():
            self.tail=new
            self.head=new
            
        else:
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            
        self.size+=1    
            
    def insert_after(self,index, val):
        new=self.Node(val)
        prev_node= self.get_Node(index)
        new.next=prev_node.next
        new.prev=prev_node
        prev_node.next=new
        if new.next is not None:
            new.next.prev=new
        self.size+=1   
            
    def delete_node(self,index):
        node=self.get_Node(index)
        
        
        if node.prev is None:
            self.head=node.next
            
        else:
            node.prev.next=node.next
            
        if node.next is None:
            self.tail=node.prev
            
        else:
            node.next.prev=node.prev
          
        self.size-=1
            
    def display(self):
            current=self.head
            
            for i in range(self.size):
                
                print(current.element, end=' ')
                current=current.next
            
        
   


# In[66]:


S=DoublyLinkedList()


# In[67]:


S.insert_at_beg(10)


# In[68]:


S.insert_at_last(30)


# In[69]:


S.insert_after(0,20) # here index beg from 0


# In[70]:


S.display()


# In[71]:


S.get_Node(1).element


# In[72]:


S.display()


# In[73]:


S.get_Node(2).element


# In[74]:


S.display()


# In[75]:


S.delete_node(1)


# In[76]:


S.display()


# In[1]:


isinstance(10,int)


# 

# In[ ]:




