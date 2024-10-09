import tkinter as tk
from customtkinter import *


class MyClass:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
    
    def greet(self):
        print(f"Hello, {self.name} fron {self.grade}{self.section}")


obj = MyClass('Samyog',12,'A')



obj.greet()
