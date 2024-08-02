college_courses={
    "History":"Mr.Washigton",
    "Math":"Mr.Newton",
    "Science":"Mr.Einstein"
}

for  course,prof  in college_courses.items():
     print(f"The course {course} is being taught by {prof}.")
for _,prof in college_courses.items():
    print(f"The next professor is {prof}")