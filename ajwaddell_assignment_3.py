# Personal Information Storage (strings using "")
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# Academic Data Organization (lists using "[]")
current_courses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list = [3, 3, 3, 3]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]

# Contact Information Storage (tuples using "()")
emergency_contact_tuple = ("Mom", "Hannah Smith", "704-555-0199")
home_address_tuple = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info_tuple = ("Instagram", "@jordan_codes", 312)
twitter_info_tuple = ("Twitter", "@jordandev", 127)
birthday_tuple = ("Birthday", 5, 22, 2006)

# Interest Tracking (sets using "{}")
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
career_interests_set = {"Software development", "Game development", "Web development", "Data science"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational Mapping (dictionary key-value pairs using "{}" and ":")
course_credits_dictionary = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors_dictionary = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms_dictionary = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget_dictionary = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject_dictionary = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory_dictionary = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

# Required Calculations (using data structures)

# a. Total current credits from credit_hours_list
total_current_credits = sum(credit_hours_list)

# b. Cumulative GPA from GPA history list (combined gpa ÷ number of gpas over time, rounded to 2 decimals)
cumulative_gpa = round(sum(gpa_history_list) / len(gpa_history_list), 2)

# c. Count of completed courses
count_of_completed_courses = len(completed_courses_list)

# d. Total weekly study hours from study_hours_per_subject_dictionary
total_weekly_study_hours = sum(study_hours_per_subject_dictionary.values())

# e. Academic load (total current credits + total weekly study hours combined)
academic_load = total_current_credits + total_weekly_study_hours

# f. Monthly budget total from all categories
monthly_budget_total = sum(monthly_budget_dictionary.values())

# g. Daily food budget (monthly food amount ÷ 30 days, rounded to 2 decimals)
daily_food_budget = round(monthly_budget_dictionary["Food"] / 30, 2)

# h. Annual budget projection (monthly budget total × 12)
annual_budget_projection = monthly_budget_total * 12

# i. Study cost per hour (books budget ÷ total study hours, rounded to 2 decimals)
study_cost_per_hour = round(monthly_budget_dictionary["Books"] / total_weekly_study_hours, 2)

# Analytics Calculations

# a. Total social media followers from platform tuples (indexing) = 312 (instagram) + 127 (twitter)
total_social_media_followers = instagram_info_tuple[2] + twitter_info_tuple[2]

# b. Skills count comparison (number of current skills vs. number of learning goals)
current_skills_count = len(current_skills_set)
skills_to_learn_count = len(skills_to_learn_set)

# c. Contact directory size analysis (number of contacts)
contact_directory_size = len(contact_directory_dictionary)

# d. Entertainment backlog management count (number of entertainment items)
entertainment_backlog_management_count = len(entertainment_backlog_set)

# e. Academic workload assessment (avg study hrs per credit, rounded to 2 decimals)
academic_workload_assessment = round(total_weekly_study_hours / total_current_credits, 2)

# ================================================================
#                   FORMATTED OUTPUT
# ================================================================

print("=" * 64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)

print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses_list)} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour\n")

print("Current Courses:")
print(f"COMP 163 - {course_credits_dictionary['COMP 163']} credits - {course_professors_dictionary['COMP 163']} - {course_rooms_dictionary['COMP 163']}")
print(f"MATH 150 - {course_credits_dictionary['MATH 150']} credits - {course_professors_dictionary['MATH 150']} - {course_rooms_dictionary['MATH 150']}")
print(f"ENG 101 - {course_credits_dictionary['ENG 101']} credits - {course_professors_dictionary['ENG 101']} - {course_rooms_dictionary['ENG 101']}")
print(f"HIS 105 - {course_credits_dictionary['HIS 105']} credits - {course_professors_dictionary['HIS 105']} - {course_rooms_dictionary['HIS 105']}\n")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget_dictionary['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget_dictionary['Entertainment']}")
print(f"Books: ${monthly_budget_dictionary['Books']}")
print(f"Transportation: ${monthly_budget_dictionary['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact_tuple[1]} ({emergency_contact_tuple[0]}) - {emergency_contact_tuple[2]}")
print(f"Home Address: {home_address_tuple[0]}, {home_address_tuple[1]} {home_address_tuple[2]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_directory_size} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {count_of_completed_courses}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_management_count} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("=" * 64)