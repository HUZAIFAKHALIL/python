
# db/seed_data.py
import sys
import os
# Add the parent directory (project root) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from config import DATABASE

def seed_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Seed default data for Study_plan
    cursor.execute('''
        INSERT OR IGNORE INTO Study_plan (study_id, totalcredit, year) VALUES
        (1, 120, 2024),
        (2, 128, 2021);
    ''')

    # Seed default data for Users
    cursor.execute('''
        INSERT OR IGNORE INTO Users (user_id, username, email, password, isadmin) VALUES
        (1, 'fajr', 'fajr@university.com', 'password123', 0),
        (2, 'saja', 'saja@university.com', 'password123', 0),
        (3, 'maha', 'maha@university.com', 'password123', 0),
        (4, 'olla', 'olla@university.com', 'password123', 0),
        (5, 'sara', 'sara@university.com', 'password123', 0),
        (6, 'fatma', 'fatma@university.com', 'password123', 0),
        (7, 'aisha', 'aisha@university.com', 'password123', 0),
        (8, 'haya', 'haya@university.com', 'password123', 0),
        (9, 'hamda', 'hamda@university.com', 'password123', 0),
        (10, 'alya', 'alya@university.com', 'password123', 0),
        (11, 'noora', 'noora@university.com', 'adminpass123', 1),
        (12, 'reem', 'reem@university.com', 'adminpass123', 1),
        (13, 'Ahmed', 'ahmed@company.com', 'admin123', 1),
        (14, 'Ali', 'ali@company.com', 'manager123', 1),
        (15, 'Muneera', 'muneera@company.com', 'tech123', 1),
        (16, 'Ghada', 'ghada@company.com', 'support123', 1);
    ''')

    # Seed default data for Advisors
    cursor.execute('''
        INSERT OR IGNORE INTO Advisors (advisor_id, name, specialization, user_id) VALUES
        (1, 'Dr. Ali Ahmed', 'Computer Science', NULL),
        (2, 'Dr. Sara Khan', 'Mathematics', NULL),
        (3, 'noora', 'Computer Science', 11),
        (4, 'reem', 'Computer Engineering', 12);
    ''')

    # Seed default data for Students
    cursor.execute('''
        INSERT OR IGNORE INTO Students (student_id, ssn, major, study_id, user_id) VALUES
        (1, '123-45-0001', 'Computer Science', 1, 1),
        (2, '123-45-0002', 'Computer Science', 1, 2),
        (3, '123-45-0003', 'Computer Science', 1, 3),
        (4, '123-45-0004', 'Computer Engineering', 2, 4),
        (5, '123-45-0005', 'Computer Engineering', 2, 5),
        (6, '123-45-0006', 'Computer Engineering', 2, 6),
        (7, '123-45-0007', 'Computer Science', 1, 7),
        (8, '123-45-0008', 'Computer Science', 1, 8),
        (9, '123-45-0009', 'Computer Engineering', 2, 9),
        (10, '123-45-0010', 'Computer Engineering', 2, 10);
    ''')

    # Seed default data for It_staff
    cursor.execute('''
        INSERT OR IGNORE INTO It_staff (staff_id, permissions, user_id) VALUES
        (1, 'Admin', 11),
        (2, 'Manager', 12),
        (3, 'Technician', 13),
        (4, 'Support', 14);
    ''')

    # Seed default data for Courses (CS Study Plan - First Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (151, 'Programming Concepts', 'Introduction to problem solving techniques using pseudo-code and flowcharts; basic programming concepts including variables, operations, control structures, arrays, functions, and file processing.', 3, 1),
        (101, 'General Chemistry I', 'Basic concepts of general chemistry.', 3, 1),
        (103, 'Experimental General Chemistry I', 'Laboratory course accompanying General Chemistry I.', 1, 1),
        (191, 'General Physics for Engineering I', 'Fundamentals of mechanics, waves, and thermodynamics.', 3, 1),
        (192, 'Experimental General Physics for Engineering I', 'Lab experiments related to mechanics and thermodynamics.', 1, 1),
        (1011, 'Calculus I', 'Differentiation and integration of functions of one variable.', 3, 1),
        (1021, 'Calculus II', 'Continuation of Calculus I: integration techniques and applications.', 3, 1),
        (231, 'Linear Algebra', 'Matrix theory, systems of linear equations, eigenvalues, and eigenvectors.', 3, 1),
        (202, 'English Language I Post Foundation', 'Academic English communication skills development.', 3, 1),
        (203, 'English Language II Post Foundation', 'Advanced academic writing and reading skills.', 3, 1),
        (121, 'History of Qatar', 'Overview of Qatar’s political, economic, and social history.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Second Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (200, 'Computer Ethics', 'Introduction to ethical issues in computing and professional responsibilities.', 1, 1),
        (205, 'Discrete Structures for Computing', 'Fundamentals of discrete mathematics used in computer science, including logic, sets, relations, functions, and combinatorics.', 3, 1),
        (303, 'Data Structures', 'Covers abstract data types and data structures such as lists, stacks, queues, trees, and graphs; includes implementation and analysis.', 4, 1),
        (323, 'Design and Analysis of Algorithms', 'Techniques for algorithm design, including divide-and-conquer, dynamic programming, greedy algorithms, and complexity analysis.', 3, 1),
        (351, 'Fundamentals of Database Systems', 'Introduction to database concepts, data models, SQL, and database design using ER modeling.', 4, 1),
        (263, 'Computer Architecture and Organization I', 'Structure, components, and operation of digital computers including instruction sets, memory hierarchy, and assembly language.', 3, 1),
        (193, 'General Physics for Engineering II', 'Continuation of Physics I, focusing on electricity, magnetism, and optics.', 3, 1),
        (194, 'Experimental General Physics for Engineering II', 'Laboratory experiments related to electricity, magnetism, and optics.', 1, 1),
        (100, 'Arabic Language I', 'Development of Arabic language proficiency in reading and writing.', 3, 1),
        (2001, 'Probability and Statistics for Engineers', 'Introduction to probability theory, statistical inference, and applications in engineering.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Third Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (310, 'Software Engineering', 'Covers software development life cycle, software process models, requirements analysis, design, implementation, testing, and maintenance.', 4, 1),
        (355, 'Data Communication and Computer Networks I', 'Networking concepts including OSI and TCP/IP models, protocols, and communication media.', 4, 1),
        (380, 'Cybersecurity Fundamentals', 'Information security including threats, vulnerabilities, cryptography, and secure system design.', 3, 1),
        (350, 'Web Development Fundamentals', 'Client-side and server-side web development technologies, including HTML, CSS, JavaScript, and introductory web frameworks.', 3, 1),
        (405, 'Operating Systems', 'Process management, memory management, file systems, and concurrency.', 4, 1),
        (3001, 'Numerical Methods', 'Numerical techniques and algorithms for solving mathematical problems using computing tools.', 3, 1),
        (111, 'Islamic Culture', 'Overview of Islamic beliefs, practices, and contributions to science and culture.', 3, 1),
        (3004, 'Natural Science/Mathematics Package', 'Elective course selected from approved Natural Science or Mathematics offerings.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Fourth Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (493, 'Senior Project I', 'Capstone project focusing on design and initial implementation.', 3, 1),
        (499, 'Senior Project II', 'Continuation of Senior Project I, focusing on implementation, testing, and presentation.', 3, 1),
        (307, 'Introduction to Project Management and Entrepreneurship', 'Project management principles and entrepreneurial thinking.', 2, 1),
        (3011, 'Principles of Management', 'Planning, organizing, leading, and controlling concepts.', 3, 1),
        (3002, 'Humanities/Fine Arts Package', 'Elective course from approved Humanities or Fine Arts offerings.', 3, 1),
        (3003, 'Social/Behavioral Sciences Package', 'Elective course from approved Social or Behavioral Sciences offerings.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Major Elective and Free Elective Courses)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (312, 'Mobile Application Development', 'Building and deploying mobile applications on various platforms.', 3, 1),
        (356, 'Web Applications Design and Development', 'Advanced web application development with modern frameworks.', 3, 1),
        (360, 'Data Science Fundamentals', 'Introduction to data analysis, machine learning, and big data processing.', 3, 1),
        (373, 'Computer Graphics', 'Rendering techniques, geometric modeling, and visualization.', 3, 1),
        (381, 'Applied Cryptography', 'Cryptographic algorithms and their applications in security.', 3, 1),
        (393, 'Modeling and Simulation', 'Techniques and tools for modeling and simulating real-world systems.', 3, 1),
        (399, 'Practical Training', 'Industry-based training experience in computing.', 3, 1),
        (403, 'Artificial Intelligence', 'Fundamentals of AI, including problem-solving, reasoning, and learning.', 3, 1),
        (433, 'Multimedia Systems', 'Technologies and applications in multimedia data processing.', 3, 1),
        (434, 'Game Design and Development', 'Principles of game design and development with modern engines.', 3, 1),
        (451, 'Database Management Systems', 'Advanced database management concepts and techniques.', 3, 1),
        (453, 'Data Mining', 'Extracting patterns and knowledge from large datasets.', 3, 1),
        (460, 'Machine Learning', 'Concepts and algorithms in supervised and unsupervised learning.', 3, 1),
        (465, 'Parallel Computing', 'Techniques for parallel processing and distributed systems.', 3, 1),
        (466, 'Information Retrieval', 'Techniques for retrieving relevant information from large datasets.', 3, 1),
        (480, 'Computer Vision', 'Image processing and visual pattern recognition.', 3, 1),
        (488, 'Wireless Networks and Applications', 'Fundamentals of wireless communication systems and protocols.', 3, 1),
        (497, 'Special Topics in Computing', 'Advanced and emerging topics in computer science.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Humanities/Fine Arts Package)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (110, 'General Geography', 'Principles of general geography, including geographical thinking and methodologies.', 3, 1),
        (241, 'Geography of Qatar', 'Insight into the geographical factors affecting Qatar.', 3, 1),
        (217, 'Islamic Civilization', 'Overview of Islamic civilization and its contributions.', 3, 1),
        (222, 'The Gulf in Modern Period', 'Historical developments in Gulf countries over the past five centuries.', 3, 1),
        (110, 'Introduction to Philosophy', 'An overview of philosophical problems and methods.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Social/Behavioral Sciences Package)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (200, 'Education and Societal Problems', 'Awareness of basic educational concepts and social issues.', 3, 1),
        (203, 'Family Relationships', 'Understanding family functions and dynamics.', 3, 1),
        (201, 'Introduction to Psychology', 'Basic principles of psychology including behavioral science.', 3, 1),
        (205, 'Social Psychology', 'Study of how thoughts, feelings, and behaviors are influenced by others.', 3, 1),
        (102, 'Honors Freshman for Social Sciences', 'Preparing honors students for social sciences.', 3, 1),
        (101, 'Political and Social Thoughts', 'Exploration of central philosophical problems and social transformations.', 3, 1),
        (103, 'Introduction to International Relations', 'Frameworks for understanding international relations and conflicts.', 3, 1),
        (206, 'Globalization', 'Exploring political, economic, and cultural phenomena related to globalization.', 3, 1),
        (103, 'Media and Society', 'Understanding the role of media in shaping social values.', 3, 1),
        (201, 'Fundamentals of Psychology', 'Scientific study of human behavior and mental processes.', 3, 1),
        (206, 'Introduction to Social Psychology', 'Impact of social interaction on individual thoughts and behaviors.', 3, 1),
        (120, 'Introduction to Sociology', 'Study of society and social interactions.', 3, 1),
        (121, 'Introduction to Anthropology', 'Exploring human culture, behavior, and social structures.', 3, 1),
        (101, 'Introduction to Social Work and Welfare', 'History and philosophy of social work.', 3, 1),
        (361, 'Society and Human Rights', 'Exploring human rights concepts and their social implications.', 3, 1),
        (200, 'Innovation, Leadership and Civic Engagement', 'Developing leadership and civic responsibility skills.', 3, 1);
    ''')

    # Seed default data for Courses (CS Study Plan - Natural Science/Mathematics Package)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (101, 'Biology I', 'Introduction to fundamental biological concepts.', 3, 1),
        (110, 'Human Biology', 'Study of human body systems and their functions.', 3, 1),
        (101, 'General Chemistry I', 'Basic chemistry concepts and laboratory practices.', 3, 1),
        (101, 'Principles of Geology', 'Understanding geological concepts and processes.', 3, 1),
        (100, 'Science for Life', 'Basic scientific concepts with real-life applications.', 3, 1),
        (101, 'Calculus I', 'Differentiation, integration, and their applications.', 3, 1),
        (103, 'Intermediate Algebra', 'Algebraic concepts and techniques.', 3, 1),
        (104, 'Basic Geometry and Measures', 'Basic geometry concepts and measurement techniques.', 3, 1),
        (105, 'Mathematics in Society', 'Applying mathematical reasoning in everyday situations.', 3, 1);
    ''')

    # Seed default data for Courses (CE Study Plan - First Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (151, 'Programming Concepts', 'Introduction to problem-solving techniques using pseudo-code and flowcharts; basic programming concepts including variables, operations, control structures, arrays, functions, and file processing.', 3, 2),
        (205, 'Discrete Structures for Computing', 'Fundamentals of discrete mathematics used in computer science, including logic, sets, relations, functions, and combinatorics.', 3, 2),
        (107, 'Engineering Skills and Ethics', 'Introduction to essential engineering skills and professional ethics.', 3, 2),
        (251, 'Object-Oriented Programming', 'Fundamentals of object-oriented programming, including classes, inheritance, polymorphism, and encapsulation.', 4, 2),
        (101, 'General Chemistry I', 'Basic concepts of general chemistry.', 3, 2),
        (103, 'Experimental General Chemistry I', 'Laboratory course accompanying General Chemistry I.', 1, 2),
        (191, 'General Physics for Engineering I', 'Fundamentals of mechanics, waves, and thermodynamics.', 3, 2),
        (192, 'Experimental General Physics for Engineering I', 'Lab experiments related to mechanics and thermodynamics.', 1, 2),
        (1011, 'Calculus I', 'Differentiation and integration of functions of one variable.', 3, 2),
        (1021, 'Calculus II', 'Continuation of Calculus I: integration techniques and applications.', 3, 2),
        (202, 'English Language I Post Foundation', 'Academic English communication skills development.', 3, 2),
        (203, 'English Language II Post Foundation', 'Advanced academic writing and reading skills.', 3, 2),
        (121, 'History of Qatar', 'Overview of Qatar’s political, economic, and social history.', 3, 2),
        (111, 'Islamic Culture', 'Overview of Islamic beliefs, practices, and contributions to science and culture.', 3, 2);
    ''')

    # Seed default data for Courses (CE Study Plan - Second Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (261, 'Digital Logic Design', 'Design and analysis of digital circuits and systems.', 4, 2),
        (351, 'Signals and Systems', 'Fundamental concepts of signal processing and system analysis.', 3, 2),
        (201, 'Electric Circuits', 'Analysis of electrical circuits and network theorems.', 3, 2),
        (231, 'Fundamental of Electronics', 'Introduction to semiconductor devices and electronic circuits.', 3, 2),
        (211, 'Calculus III', 'Vector calculus and functions of multiple variables.', 3, 2),
        (263, 'Computer Architecture and Organization I', 'Understanding the internal architecture and organization of a computer system.', 3, 2),
        (193, 'General Physics for Engineering II', 'Continuation of Physics I, focusing on electricity, magnetism, and optics.', 3, 2),
        (194, 'Experimental General Physics for Engineering II', 'Laboratory experiments related to electricity, magnetism, and optics.', 1, 2),
        (200, 'Probability and Statistics for Engineers', 'Introduction to probability theory and statistical methods for engineering applications.', 3, 2),
        (100, 'Arabic Language I', 'Development of Arabic language proficiency in reading and writing.', 3, 2);
    ''')

    # Seed default data for Courses (CE Study Plan - Third Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (355, 'Data Communication and Computer Networks I', 'Networking concepts including OSI and TCP/IP models, protocols, and media.', 4, 2),
        (364, 'Microprocessor Based Design', 'Design and programming of microprocessor-based systems.', 4, 2),
        (363, 'Computer Architecture and Organization II', 'Advanced concepts in computer architecture.', 3, 2),
        (457, 'Data Communication and Computer Networks II', 'Advanced networking topics, including routing and switching.', 3, 2),
        (370, 'Computer Engineering Practicum', 'Hands-on experience in computer engineering projects.', 1, 2),
        (476, 'Digital Signal Processing', 'Techniques for processing discrete-time signals.', 4, 2),
        (405, 'Operating Systems', 'Concepts of operating systems including process management, memory management, and file systems.', 4, 2),
        (360, 'Engineering Economics', 'Economic analysis of engineering projects.', 3, 2),
        (217, 'Mathematics for Engineers', 'Advanced mathematical techniques used in engineering.', 3, 2),
        (300, 'Numerical Methods', 'Numerical methods for solving engineering problems.', 3, 2);
    ''')

    # Seed default data for Courses (CE Study Plan - Fourth Year)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (498, 'Design Project I', 'Capstone project focusing on problem-solving and solution implementation.', 3, 2),
        (499, 'Design Project II', 'Continuation of Design Project I, focusing on testing and final presentation.', 3, 2),
        (462, 'Computer Interfacing', 'Interfacing techniques for microprocessors and embedded systems.', 3, 2),
        (3002, 'Humanities/Fine Arts Package', 'Elective course selected from approved Humanities or Fine Arts offerings.', 3, 2),
        (3003, 'Social/Behavioral Sciences Package', 'Elective course selected from approved Social or Behavioral Sciences offerings.', 3, 2);
    ''')

    # Seed default data for Courses (CE Study Plan - Elective Courses)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (312, 'Mobile Application Development', 'Developing and deploying mobile applications on various platforms.', 3, 2),
        (385, 'Computer Security', 'Principles and practices of computer security, including encryption and authentication.', 3, 2),
        (480, 'Computer Vision', 'Image processing and visual pattern recognition.', 3, 2),
        (488, 'Wireless Networks and Applications', 'Wireless communication systems and protocols.', 3, 2),
        (399, 'Practical Training', 'Industry-based training experience.', 3, 2),
        (470, 'Modern Computer Organization', 'Advanced topics in computer organization.', 3, 2),
        (471, 'Selected Topics in Computer Engineering', 'Emerging topics in computer engineering.', 3, 2),
        (474, 'Artificial Neural Networks', 'Deep learning concepts and neural network architectures.', 3, 2),
        (481, 'Modeling and Simulation of Digital Systems', 'Modeling techniques for digital systems.', 3, 2),
        (482, 'Multimedia Networks', 'Technologies for multimedia networking and applications.', 3, 2),
        (483, 'Introduction to Robotics', 'Robotic systems and control techniques.', 3, 2),
        (485, 'Fundamentals of Digital Image Processing', 'Techniques for processing and analyzing digital images.', 3, 2),
        (487, 'Hardware Software Co-Design', 'Design and implementation of hardware-software systems.', 3, 2);
    ''')

    # Seed default data for Courses (CE Study Plan - Social/Behavioral Sciences Package)
    cursor.execute('''
        INSERT OR IGNORE INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
        (103, 'Introduction to International Relations', 'Analytical and theoretical frameworks for understanding international relations, conflicts, diplomacy, and global terrorism.', 3, 2),
        (101, 'Political and Social Thoughts', 'Philosophical problems and transformations of Western Europe over the past 500 years.', 3, 2),
        (201, 'Introduction to Psychology', 'Basic principles and methods of psychology including behavioral science.', 3, 2),
        (205, 'Social Psychology', 'Study of how thoughts, feelings, and behaviors are influenced by social interactions.', 3, 2),
        (203, 'Family Relationships', 'Understanding family dynamics, roles, and family growth in the life cycle.', 3, 2),
        (200, 'Education and Societal Problems', 'Awareness of educational concepts and their relationship with societal problems.', 3, 2),
        (207, 'Introduction to Sociology', 'Study of social behavior, structures, and institutions.', 3, 2),
        (210, 'Human Development', 'Examination of human growth and development across the lifespan.', 3, 2),
        (300, 'Organizational Behavior', 'Understanding behavior in organizational settings, focusing on individual and group processes.', 3, 2),
        (400, 'Social and Cultural Anthropology', 'Study of human societies and cultures and their development.', 3, 2);
    ''')

    # Seed default data for Course_prerequisite (CS Study Plan)
    cursor.execute('''
        INSERT OR IGNORE INTO Course_prerequisite (course_id, pre_id) VALUES
        (251, 151),
        (203, 202),
        (1021, 1011),
        (231, 1011),
        (193, 191),
        (194, 192),
        (205, 151),
        (303, 251),
        (323, 303),
        (351, 303),
        (263, 303),
        (200, 1021),
        (310, 251),
        (350, 251),
        (405, 303),
        (380, 303),
        (355, 303),
        (300, 1021),
        (493, 310),
        (499, 493),
        (499, 350),
        (499, 405),
        (307, 310),
        (312, 151),
        (356, 350),
        (360, 200),
        (403, 323),
        (451, 351),
        (453, 451),
        (460, 360);
    ''')

    # Seed default data for Course_prerequisite (CE Study Plan)
    cursor.execute('''
        INSERT OR IGNORE INTO Course_prerequisite (course_id, pre_id) VALUES
        (251, 151),
        (203, 202),
        (1021, 1011),
        (193, 191),
        (261, 191),
        (201, 191),
        (205, 151),
        (303, 251),
        (263, 261),
        (351, 201),
        (211, 1021),
        (405, 303),
        (323, 303),
        (351, 303),
        (363, 263),
        (364, 263),
        (355, 261),
        (457, 355),
        (300, 211),
        (476, 351),
        (380, 405),
        (498, 370),
        (499, 498),
        (462, 364),
        (474, 303),
        (474, 200),
        (488, 355),
        (485, 300),
        (470, 263),
        (481, 300),
        (483, 261),
        (399, 0),
        (480, 476),
        (480, 303),
        (487, 364),
        (482, 355),
        (471, 0);
    ''')

    # Seed default data for Time_Slots
    cursor.execute('''
        INSERT OR IGNORE INTO Time_Slots (slot_id, advisor_id, available_date, time_slot, is_booked) VALUES
        (1, 1, '2025-01-10', '10:00 AM - 11:00 AM', 0),
        (2, 1, '2025-01-10', '11:00 AM - 12:00 PM', 0),
        (3, 2, '2025-01-11', '02:00 PM - 03:00 PM', 0),
        (4, 1, '2025-03-25', '10:00-10:30', 0),
        (5, 1, '2025-03-25', '10:30-11:00', 0),
        (6, 2, '2025-03-26', '12:00-12:30', 0),
        (7, 2, '2025-03-26', '12:40-1:10', 0);
    ''')

    # Seed default data for Appointments
    cursor.execute('''
        INSERT OR IGNORE INTO Appointments (appointment_id, student_id, slot_id, advisor_id, timestamp) VALUES
        (1, 1, 4, 1, '2025-03-25 10:00:00'),
        (2, 5, 6, 2, '2025-03-26 12:00:00');
    ''')

    # Seed default data for Study_plan_details (CS Study Plan - 2024)
    cursor.execute('''
        INSERT OR IGNORE INTO Study_plan_details (study_id, course_id, status) VALUES
        (1, 151, 'Core'),
        (1, 205, 'Core'),
        (1, 107, 'Core'),
        (1, 251, 'Core'),
        (1, 101, 'Core'),
        (1, 103, 'Core'),
        (1, 191, 'Core'),
        (1, 192, 'Core'),
        (1, 1011, 'Core'),
        (1, 1021, 'Core'),
        (1, 202, 'Core'),
        (1, 203, 'Core'),
        (1, 231, 'Core'),
        (1, 121, 'Core'),
        (1, 111, 'Core'),
        (1, 310, 'Core'),
        (1, 355, 'Core'),
        (1, 380, 'Core'),
        (1, 350, 'Core'),
        (1, 405, 'Core'),
        (1, 3001, 'Core'),
        (1, 493, 'Core'),
        (1, 499, 'Core'),
        (1, 307, 'Core'),
        (1, 3011, 'Core'),
        (1, 3002, 'Humanities/Fine Arts Package'),
        (1, 3003, 'Social/Behavioral Sciences Package'),
        (1, 100, 'Natural Science/Mathematics Package'),
        (1, 300, 'Elective'),
        (1, 312, 'Elective'),
        (1, 356, 'Elective'),
        (1, 360, 'Elective'),
        (1, 373, 'Elective'),
        (1, 381, 'Elective'),
        (1, 393, 'Elective'),
        (1, 403, 'Elective'),
        (1, 433, 'Elective'),
        (1, 434, 'Elective'),
        (1, 451, 'Elective'),
        (1, 453, 'Elective'),
        (1, 460, 'Elective'),
        (1, 465, 'Elective'),
        (1, 466, 'Elective'),
        (1, 480, 'Elective'),
        (1, 488, 'Elective'),
        (1, 497, 'Elective');
    ''')

    # Seed default data for Study_plan_details (CE Study Plan - 2021)
    cursor.execute('''
        INSERT OR IGNORE INTO Study_plan_details (study_id, course_id, status) VALUES
        (2, 151, 'Core'),
        (2, 205, 'Core'),
        (2, 107, 'Core'),
        (2, 251, 'Core'),
        (2, 101, 'Core'),
        (2, 103, 'Core'),
        (2, 191, 'Core'),
        (2, 192, 'Core'),
        (2, 1011, 'Core'),
        (2, 1021, 'Core'),
        (2, 202, 'Core'),
        (2, 203, 'Core'),
        (2, 121, 'Core'),
        (2, 111, 'Core'),
        (2, 261, 'Core'),
        (2, 351, 'Core'),
        (2, 201, 'Core'),
        (2, 231, 'Core'),
        (2, 211, 'Core'),
        (2, 263, 'Core'),
        (2, 193, 'Core'),
        (2, 194, 'Core'),
        (2, 200, 'Core'),
        (2, 100, 'Core'),
        (2, 355, 'Core'),
        (2, 364, 'Core'),
        (2, 363, 'Core'),
        (2, 457, 'Core'),
        (2, 370, 'Core'),
        (2, 476, 'Core'),
        (2, 405, 'Core'),
        (2, 360, 'Core'),
        (2, 217, 'Core'),
        (2, 300, 'Core'),
        (2, 498, 'Core'),
        (2, 499, 'Core'),
        (2, 462, 'Core'),
        (2, 3002, 'Humanities/Fine Arts Package'),
        (2, 3003, 'Social/Behavioral Sciences Package'),
        (2, 474, 'Elective'),
        (2, 488, 'Elective'),
        (2, 485, 'Elective'),
        (2, 470, 'Elective'),
        (2, 481, 'Elective'),
        (2, 483, 'Elective'),
        (2, 399, 'Elective'),
        (2, 480, 'Elective'),
        (2, 487, 'Elective'),
        (2, 482, 'Elective'),
        (2, 471, 'Elective');
    ''')

    # Seed default data for student_enroll
    cursor.execute('''
        INSERT OR IGNORE INTO student_enroll (student_id, course_id, grade, date) VALUES
        (1, 151, 'A', '2024-02-10'),
        (1, 205, 'B+', '2024-03-01'),
        (1, 251, 'A', '2024-03-15'),
        (1, 101, 'B', '2024-04-05'),
        (1, 310, 'A', '2024-05-10'),
        (1, 355, 'B+', '2024-05-25'),
        (2, 303, 'B+', '2024-03-20'),
        (2, 323, 'A', '2024-04-01'),
        (2, 350, 'B', '2024-04-20'),
        (2, 380, 'C+', '2024-05-05'),
        (2, 405, 'A', '2024-05-15'),
        (3, 493, 'A', '2024-06-01'),
        (3, 499, 'B+', '2024-06-15'),
        (3, 300, 'A', '2024-07-01'),
        (3, 360, 'B', '2024-07-20'),
        (4, 261, 'B+', '2024-02-10'),
        (4, 351, 'A', '2024-03-05'),
        (4, 201, 'B', '2024-03-25'),
        (4, 231, 'C', '2024-04-10'),
        (4, 211, 'A', '2024-04-25'),
        (4, 263, 'B', '2024-05-10'),
        (5, 355, 'B+', '2024-02-20'),
        (5, 364, 'C+', '2024-03-05'),
        (5, 457, 'A', '2024-03-25'),
        (5, 476, 'B', '2024-04-10'),
        (5, 405, 'A', '2024-04-20'),
        (6, 498, 'A', '2024-05-10'),
        (6, 499, 'B', '2024-05-25'),
        (6, 462, 'C', '2024-06-05'),
        (6, 470, 'B+', '2024-06-20'),
        (7, 300, 'A', '2024-02-15'),
        (7, 312, 'B+', '2024-03-01'),
        (7, 356, 'C', '2024-03-20'),
        (7, 403, 'B', '2024-04-05'),
        (7, 460, 'A', '2024-04-20'),
        (8, 433, 'B+', '2024-05-01'),
        (8, 434, 'A', '2024-05-15'),
        (8, 451, 'B', '2024-06-01'),
        (8, 453, 'C+', '2024-06-20'),
        (9, 474, 'A', '2024-02-10'),
        (9, 480, 'B+', '2024-03-01'),
        (9, 487, 'C+', '2024-03-20'),
        (9, 488, 'F', '2024-04-05'),
        (10, 485, 'B', '2024-05-01'),
        (10, 481, 'A', '2024-05-15'),
        (10, 482, 'C', '2024-06-01'),
        (10, 399, 'D+', '2024-06-20');
    ''')

    # Seed default data for Student_Update
    cursor.execute('''
        INSERT OR IGNORE INTO Student_Update (student_id, update_id, description) VALUES
        (1, 1, 'Failed Calculus II and will retake next semester'),
        (2, 2, 'Enrolled in Senior Project I as a graduating senior'),
        (3, 3, 'Resigned from the elective course - Data Science Fundamentals'),
        (4, 4, 'Registered for elective course - Wireless Networks and Applications'),
        (5, 5, 'Failed Data Structures and retaking it in the current semester'),
        (6, 6, 'Taking Senior Project II after completing Senior Project I successfully'),
        (7, 7, 'Dropped Multimedia Networks elective due to schedule conflict'),
        (8, 8, 'Registered for elective course - Computer Vision'),
        (9, 9, 'Failed Operating Systems and will retake it in the next term'),
        (10, 10, 'Taking the final elective requirement with Mobile Application Development'),
        (9, 11, 'Graduation delayed due to not completing credit hour requirements'),
        (10, 12, 'Completed graduation requirements and is now eligible to graduate');
    ''')

    # Seed default data for Course_Update
    cursor.execute('''
        INSERT OR IGNORE INTO Course_Update (update_id, course_id, timestamp, description) VALUES
        (1, 151, '2024-02-01 10:00:00', 'Updated course content for Programming Concepts'),
        (2, 205, '2024-03-10 12:00:00', 'Added new topics to Discrete Structures'),
        (3, 310, '2024-04-15 09:30:00', 'Software Engineering course outline updated'),
        (4, 405, '2024-05-20 14:45:00', 'Operating Systems syllabus revised'),
        (5, 350, '2024-06-05 13:00:00', 'Updated web development frameworks covered'),
        (6, 493, '2024-07-18 11:10:00', 'New guidelines for Senior Project I'),
        (7, 499, '2024-08-22 15:25:00', 'Senior Project II requirements updated'),
        (8, 355, '2024-09-10 10:15:00', 'Networking protocols added to syllabus'),
        (9, 476, '2024-10-05 12:40:00', 'Updated DSP course content'),
        (10, 451, '2024-11-01 14:30:00', 'Database Management Systems improvements');
    ''')

    cursor.execute('''
    INSERT OR IGNORE INTO faq (faqID, question, answer) VALUES
    (101, 'What are the office hours?', 'Office hours are from 9 AM to 5 PM, Monday to Friday.'),
    (102, 'How do I book an appointment?', 'You can book an appointment through the "Book Appointment" section on the dashboard.'),
    (103, 'What is the deadline for course registration?', 'Course registration closes one week before the semester starts.'),
    (104, 'How do I reset my password?', 'Use the "Forgot Password" link on the login page.'),
    (105, 'Where can I find the study plan?', 'The study plan is available in the student dashboard under "Academic Plan".'),
    (106, 'Who is my academic advisor?', 'Your advisor is listed in the "Advisor" section of your profile.'),
    (107, 'Can I change my major?', 'Yes, submit a major change request via the registrar’s office.'),
    (108, 'What are the prerequisites for Senior Project I?', 'Completion of Software Engineering and 90 credit hours.'),
    (109, 'How do I appeal a grade?', 'Submit a grade appeal form to the academic office within two weeks of grade release.'),
    (110, 'Are there tutoring services available?', 'Yes, tutoring is available through the Academic Resource Center.'),
    (201, 'How do I schedule advising sessions?', 'Use the advisor portal to set available time slots.'),
    (202, 'What documentation is needed for student updates?', 'Submit updates via the advisor dashboard with relevant documentation.'),
    (203, 'How do I approve a student’s study plan?', 'Review and approve plans in the "Student Plans" section of the advisor portal.'),
    (204, 'Can I access student transcripts?', 'Transcripts are available in the advisor dashboard under "Student Records".');
''')


    # Seed default data for Browse_Student
    cursor.execute('''
        INSERT OR IGNORE INTO Browse_Student (student_id, brows_date, faq_id) VALUES
        (1, '2024-01-15 10:30:00', 101),
        (2, '2024-02-10 14:45:00', 102),
        (3, '2024-03-05 09:20:00', 103),
        (4, '2024-04-12 11:00:00', 104),
        (5, '2024-05-18 16:25:00', 105),
        (6, '2024-06-20 13:15:00', 106),
        (7, '2024-07-25 08:50:00', 107),
        (8, '2024-08-14 15:30:00', 108),
        (9, '2024-09-07 17:40:00', 109),
        (10, '2024-10-01 12:05:00', 110);
    ''')

    # Seed default data for Browse_Adviser
    cursor.execute('''
        INSERT OR IGNORE INTO Browse_Adviser (advisor_id, brows_date, faq_id) VALUES
        (1, '2024-01-20 09:30:00', 201),
        (2, '2024-02-25 11:15:00', 202),
        (3, '2024-03-30 14:00:00', 203),
        (4, '2024-04-28 16:45:00', 204);
    ''')

    conn.commit()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()