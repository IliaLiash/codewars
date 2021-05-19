class add(int):
    def __call__(self,n):
        return add(self+n)

add(1)(2)
add(1)(2)(3)