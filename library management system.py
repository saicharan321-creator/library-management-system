import sys
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayavailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
      def lendbook(self,requestedbook):
            if requestedbook in self.availablebooks:
                  print("You can take the requested book now")
                  self.availablebooks.remove(requestedbook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addbook(self,returnedbook):
            self.availablebooks.append(returnedbook)
            print("Thanks for returning your requested book")
            

class Student:

      def requestbook(self):
            print("Enter the name of the book you'd like to take>>")
            self.book=input()
            return self.book

      def returnbook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

def main():            
      library=Library(["Beloved","Invisible Man","A Passage to india","The little prince","Wings of fire"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayavailablebooks()
            elif choice==2:
                        library.lendbook(student.requestbook())
            elif choice==3:
                        library.addbook(student.returnbook())
            elif choice==4:
                  print(sys.exit())
main()
