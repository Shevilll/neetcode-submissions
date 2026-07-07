from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

       count = 0
       students = deque(students)
       while students and sandwiches:
        if students[0] == sandwiches[0]:

        
            students.popleft()
            sandwiches.pop(0)
            count = 0
        else:
            student = students[0]
            students.popleft()
            students.append(student)
            count = count+1  
            if count == len(students):
                return len(students)

       return 0        
                 
 