def is_course_schedule_possible(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    
    for prereq in prerequisites:
        course, prereq_course = prereq
        graph[course].append(prereq_course)
    
    def depth_first_search(course):
        if visited[course] == 1:
            return False
        if visited[course] == 2:
            return True
        
        visited[course] = 1
        
        for neighbor in graph[course]:
            if not depth_first_search(neighbor):
                return False
        
        visited[course] = 2
        return True
    
    visited = [0] * num_courses
    
    for i in range(num_courses):
        if not depth_first_search(i):
            return False
    
    return True

print(is_course_schedule_possible(2, [[0, 1], [1, 0]]))
print(is_course_schedule_possible(3, [[1, 0], [0, 2]]))
