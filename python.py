from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r

class Square(Shape):
    def __init__(self, s):
        self.s = s
    
    def area(self):
        return self.s * self.s
    
    def perimeter(self):
        return 4 * self.s

def main():
    while True:
        print("\n1. Circle")
        print("2. Square")
        print("3. Exit")
        
        choice = input("Choose shape: ")
        
        if choice == '1':
            r = float(input("Enter radius: "))
            circle = Circle(r)
            print(f"Area: {circle.area()}")
            print(f"Perimeter: {circle.perimeter()}")
        
        elif choice == '2':
            s = float(input("Enter side length: "))
            square = Square(s)
            print(f"Area: {square.area()}")
            print(f"Perimeter: {square.perimeter()}")
        
        elif choice == '3':
            print("Bye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()