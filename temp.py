class box:
    x=int(input())
    y=int(input())
    z=int(input())
    
    def area (x,y):
        print(x*y)
        return(x*y)
        
    def volume (x,y,z):
        print(x*y*z)
        return (x*y*z)
box.area(box.x,box.y)
box.volume(box.x,box.y,box.z)
print (box.x)