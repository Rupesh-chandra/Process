#!/usr/bin/env python
# coding: utf-8

# In[224]:


class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")
    

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    
    def area(self):
        """
        Returns area of the square
        """
        return round(self.side**2)
    
    def __str__(self):
        return 'Square with side ' + str(self.side)
    
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side
    

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    
    def area(self):
        """
        Returns approximate area of the circle
        """
        return round(3.14159*(self.radius**2))
    
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


# In[274]:


#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: length of base.
        height: height of triangle
        """
        self.base = float(base)
        self.height = float(height)
    
    def area(self):
        """
        Returns approximate area of the triangle 
        """
        return round(.5 * self.base * self.height,2)
    
    def __str__(self):
        """
        Describes this intance of Triangle.
        """
        return 'Triangle with a base of' + ' ' +str(self.base) + ' '+ 'and height of' + ' '+ str(self.height)
    
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and height.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height


# In[226]:



#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.members = []
        self.index = 0
    
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.members:
            self.members.append(sh)
            # print sh, "added to set."
    
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        for i in self.members:
            yield i
    
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        my_string = ""
        for each in self.members:
            # print each
            my_string += str(each) + "\n"
        return my_string
    
    


# In[251]:



#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the largest area.
    
    shapes: ShapeSet
    
    This is a sorting problem
    """
    result = (0,)
    for each in shapes:
        try:
            if each.area() > result[-1].area():
                result = (each,)
            elif each.area() == result[-1].area():
                result += (each,)
        except AttributeError:
            result = (each,)
    return result


# In[275]:



#
# Problem 4: Read shapes from a file into a ShapeSet
#


SHAPES_FILENAME = "shapes.txt"

def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file. Creates and returns a ShapeSet with the shapes found. 
    
    filename: string
    """
    ## TO DO
    inFile = open(filename, 'r')
    shape_set = ShapeSet()
    for line in inFile:
        obj_para = line.split(",")
        if obj_para[0] == "circle":
            shape = Circle(obj_para[1])
        if obj_para[0] == "square":
            shape = Square(obj_para[1])
        if obj_para[0] == "triangle":
            shape = Triangle(obj_para[1],obj_para[2])
        shape_set.addShape(shape)
    return shape_set

my_ss = readShapesFromFile(SHAPES_FILENAME)
print (my_ss)


# In[296]:


my_circle = Circle(7)
my_square = Square(22)
my_square2 = Square(11)
my_triangle = Triangle(10,15)
 
my_shapeset = ShapeSet()


# In[297]:


print(my_circle)
print(my_square)
print(my_square2)
print(my_triangle)


# In[315]:


your_circle = Circle(8)
your_square = Square(26)
your_square2 = Square(11)
your_triangle = Triangle(12,15)
 
my_shapeset = ShapeSet()


# In[316]:


print(your_circle)
print(your_square)
print(your_square2)
print(your_triangle)


# In[317]:


your_triangle.base = 45
print(your_triangle)


# In[319]:


your_triangle.height = 20
print(your_triangle)


# In[300]:


print (your_triangle == my_triangle)
print (your_square2 == my_square2)


# In[314]:


your_triangle.base = 45


# In[ ]:


print


# In[301]:


my_shapeset.addShape(Circle(2.25676))
my_shapeset.addShape(Square(4))
my_shapeset.addShape(Square(1))
my_shapeset.addShape(Triangle(1,1))


# In[313]:


print (my_shapeset.__str__())
findLargest(my_shapeset)


# In[310]:


def testFindLargest():
    ss = ShapeSet() 
    ss.addShape(Triangle(1.2,2.5)) 
    ss.addShape(Circle(4)) 
    ss.addShape(Square(3.6)) 
    ss.addShape(Triangle(1.6,6.4)) 
    ss.addShape(Circle(2.2)) 
    largest = findLargest(ss)
    print (largest)
    for e in largest: 
        print (e)
    
    
    ss = ShapeSet()
    ss.addShape(Triangle(3,8)) 
    ss.addShape(Circle(1)) 
    ss.addShape(Triangle(4,6)) 
    largest = findLargest(ss) 
    print (largest)
    for e in largest:
        print (e)

def testSamenes():
    t = Triangle(6,6)
    c = Circle(1)
    ss = ShapeSet()
    ss.addShape(t)
    ss.addShape(c)
    largest = findLargest(ss)
    print (largest)
    print (largest[0] is t)
    print (largest[0] is c)

testFindLargest()


# In[ ]:





# In[ ]:




