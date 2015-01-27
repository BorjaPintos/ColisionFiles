import random, math, os, hashlib, sys

outputdebug = False 
colisionList = {}

def debug(msg):
    if outputdebug:
        print msg

class Node():
    def __init__(self, key, path):
        self.key = key
        self.path = path
        self.left = None 
        self.right = None 

class Colision():
    def __init__(self, md5, path):
        self.count = 1
        self.md5 = md5
        self.path = []
        self.path.append(path)
    
    def update(self, path):
        self.count = self.count + 1
        self.path.append(path)

    def __str__(self):
     return "Repeat: " + str(self.count) + "\n" + "Hash :" + self.md5 + "\n" + "Paths :" + str(self.path) + "\n"

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0;

                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key, path):
        tree = self.node
        result=None
        newnode = Node(key, path)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            result = self.node.left.insert(key, path)

            
        elif key > tree.key: 
            result = self.node.right.insert(key, path)
   
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            result = tree.path
            
        self.rebalance() 

        return result
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 
        

    def insertPath(self, path):
        global colisionList
        if os.path.isdir(path):
            list = os.listdir(path)
            for f in list:
                filepath = os.path.join(path,f)
                self.insertPath(filepath)
        else:
            md5 = hashlib.md5(open(path).read()).hexdigest()
            colisionPath = self.insert(md5,path)
            if colisionPath!=None:
                c = colisionList.get(md5)
                if (c==None):
                    c = Colision(md5,colisionPath)
                    colisionList[md5] = c
                c.update(path);


# Usage example
if __name__ == "__main__": 

    if len(sys.argv) < 2:
        print "Usage: python "+ sys.argv[0] + " <PATH>"
        exit(0);
    else:
        print sys.argv[1]
        tree = AVLTree()
        tree.insertPath(sys.argv[1])

        for key, c in colisionList.items():
            print c
    
