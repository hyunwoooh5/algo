class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)
        sandwiches = deque(sandwiches)

        count = 0
        n = len(students)

        while count < n and len(students) != 0:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students[0])
                students.popleft()
                count += 1

        return len(students)
