-- SQLite_other_queries.sql
-- Inserting test data

INSERT INTO Study_plan (study_id, totalcredit, year) VALUES
(1, 120, 2024),
(2, 128, 2021);

INSERT INTO Users (user_id, username, email, password, isadmin) VALUES
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
(12, 'reem', 'reem@university.com', 'adminpass123', 1);
(11, 'Ahmed', 'ahmed@company.com', 'admin123', 1),
(12, 'Ali', 'ali@company.com', 'manager123', 1),
(13, 'Muneera', 'muneera@company.com', 'tech123', 1),
(14, 'Ghada', 'ghada@company.com', 'support123', 1);


INSERT INTO Advisors (advisor_id, name, specialization, user_id) VALUES
(1, 'noora', 'Computer Science', 11),
(2, 'reem', 'Computer Engineering', 12);

INSERT INTO Students (student_id, ssn, major, study_id, user_id) VALUES
(1, '123-45-0001', 'fajr', 1, 2),
(2, '123-45-0002', 'saja', 1, 2),
(3, '123-45-0003', 'maha', 1, 2),
(4, '123-45-0004', 'olla', 1, 2),
(5, '123-45-0005', 'sara', 1, 2),
(6, '123-45-0006', 'fatma', 1, 2),
(7, '123-45-0007', 'aisha', 1, 2),
(8, '123-45-0008', 'haya', 1, 2),
(9, '123-45-0009', 'hamda', 1, 2),
(10,'123-45-0010', 'alya', 1, 2);

INSERT INTO It_staff (staff_id, permissions, user_id) VALUES
(1, 'Admin', 11),
(2, 'Manager', 12),
(3, 'Technician', 13),
(4, 'Support', 14);


-- Insert into CS Stduy plan 
-- First Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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



-- Second Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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



-- Third Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
(310, 'Software Engineering', 'Covers software development life cycle, software process models, requirements analysis, design, implementation, testing, and maintenance.', 4, 1),
(355, 'Data Communication and Computer Networks I', 'Networking concepts including OSI and TCP/IP models, protocols, and communication media.', 4, 1),
(380, 'Cybersecurity Fundamentals', 'Information security including threats, vulnerabilities, cryptography, and secure system design.', 3, 1),
(350, 'Web Development Fundamentals', 'Client-side and server-side web development technologies, including HTML, CSS, JavaScript, and introductory web frameworks.', 3, 1),
(405, 'Operating Systems', 'Process management, memory management, file systems, and concurrency.', 4, 1),
(3001, 'Numerical Methods', 'Numerical techniques and algorithms for solving mathematical problems using computing tools.', 3, 1),
(111, 'Islamic Culture', 'Overview of Islamic beliefs, practices, and contributions to science and culture.', 3, 1);
(3004, 'Natural Science/Mathematics Package', 'Elective course selected from approved Natural Science or Mathematics offerings.', 3, 1),




-- Fourth Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
(493, 'Senior Project I', 'Capstone project focusing on design and initial implementation.', 3, 1),
(499, 'Senior Project II', 'Continuation of Senior Project I, focusing on implementation, testing, and presentation.', 3, 1),
(307, 'Introduction to Project Management and Entrepreneurship', 'Project management principles and entrepreneurial thinking.', 2, 1),
(3011, 'Principles of Management', 'Planning, organizing, leading, and controlling concepts.', 3, 1),
(3002, 'Humanities/Fine Arts Package', 'Elective course from approved Humanities or Fine Arts offerings.', 3, 1),
(3003, 'Social/Behavioral Sciences Package', 'Elective course from approved Social or Behavioral Sciences offerings.', 3, 1);


-- Major Elective and Free Elective Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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

--Packages courses 
-- Humanities/Fine Arts Package (0 - 3 Credit Hours)
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
(110, 'General Geography', 'Principles of general geography, including geographical thinking and methodologies.', 3, 1),
(241, 'Geography of Qatar', 'Insight into the geographical factors affecting Qatar.', 3, 1),
(217, 'Islamic Civilization', 'Overview of Islamic civilization and its contributions.', 3, 1),
(222, 'The Gulf in Modern Period', 'Historical developments in Gulf countries over the past five centuries.', 3, 1),
(110, 'Introduction to Philosophy', 'An overview of philosophical problems and methods.', 3, 1);

-- Social/Behavioral Sciences Package (3 Credit Hours)
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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

-- Natural Science/Mathematics Package (3 Credit Hours)
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
(101, 'Biology I', 'Introduction to fundamental biological concepts.', 3, 1),
(110, 'Human Biology', 'Study of human body systems and their functions.', 3, 1),
(101, 'General Chemistry I', 'Basic chemistry concepts and laboratory practices.', 3, 1),
(101, 'Principles of Geology', 'Understanding geological concepts and processes.', 3, 1),
(100, 'Science for Life', 'Basic scientific concepts with real-life applications.', 3, 1),
(101, 'Calculus I', 'Differentiation, integration, and their applications.', 3, 1),
(103, 'Intermediate Algebra', 'Algebraic concepts and techniques.', 3, 1),
(104, 'Basic Geometry and Measures', 'Basic geometry concepts and measurement techniques.', 3, 1),
(105, 'Mathematics in Society', 'Applying mathematical reasoning in everyday situations.', 3, 1);


-- Prerequiste CS Study plan 
-- Year 1 → Year 2
-- OOP ← Programming Concepts
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (251, 151);  

-- English Language II Post Foundation ← English Language I Post Foundation
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (203, 202);  

-- Calculus II ← Calculus I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (1021, 1011);  

-- Linear Algebra ← Calculus I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (231, 1011);  

-- Physics II ← Physics I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (193, 191);  

-- Experimental General Physics II ← Experimental General Physics I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (194, 192);  

-- Discrete Structures ← Programming Concepts
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (205, 151);  




-- Year 2 → Year 2 & 3
-- Data Structures ← OOP
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (303, 251);  

-- Algorithms ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (323, 303);  

-- Database Systems ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (351, 303);  

-- Computer Architecture ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (263, 303);  

-- Probability and Statistics for Engineers ← Calculus II
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (200, 1021);  



-- Year 3 ← Year 2
-- Software Engineering ← OOP
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (310, 251);   

-- Web Development ← OOP
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (350, 251);  
-- Operating Systems ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (405, 303);  

-- Cybersecurity ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (380, 303);  

-- Data Communication and Computer Networks I ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (355, 303);  

-- Numerical Methods ← Calculus II
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (300, 1021);  




-- Year 4 ← Year 3
-- Senior Project I ← Software Engineering
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (493, 310);  

-- Senior Project II ← Senior Project I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (499, 493);  

-- Senior Project II ← Web Development OR Operating Systems
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (499, 350);  
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (499, 405);  

-- Project Management and Entrepreneurship ← Software Engineering
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (307, 310);  




--CS Electives  Prerequisites
-- Mobile Application Development ← Programming Concepts
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (312, 151);  

-- Web Applications Design and Development ← Web Development
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (356, 350);  

-- Data Science Fundamentals ← Probability and Statistics
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (360, 200);  

-- Artificial Intelligence ← Algorithms
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (403, 323);  

-- Database Management Systems ← Database Systems
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (451, 351);  

-- Data Mining ← Database Management Systems
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (453, 451);  

-- Machine Learning ← Data Science Fundamentals
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (460, 360);  





-- Insert into CE Stduy plan 
-- First Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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



-- Second Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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



-- Third Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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


-- Fourth Year Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
(498, 'Design Project I', 'Capstone project focusing on problem-solving and solution implementation.', 3, 2),
(499, 'Design Project II', 'Continuation of Design Project I, focusing on testing and final presentation.', 3, 2),
(462, 'Computer Interfacing', 'Interfacing techniques for microprocessors and embedded systems.', 3, 2),
(3002, 'Humanities/Fine Arts Package', 'Elective course selected from approved Humanities or Fine Arts offerings.', 3, 2),
(3003, 'Social/Behavioral Sciences Package', 'Elective course selected from approved Social or Behavioral Sciences offerings.', 3, 2);

-- Elective Courses
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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

--Package courses 
-- Social/Behavioral Sciences Package (CE Study Plan)
INSERT INTO Courses (course_id, course_name, description, credithours, study_id) VALUES
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

-- Prerequiste CE Study plan 
---- Year 1 → Year 2
-- OOP ← Programming Concepts
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (251, 151); 

-- English Language II Post Foundation ← English Language I Post Foundation
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (203, 202);  
-- Calculus II ← Calculus I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (1021, 1011);  

-- Physics II ← Physics I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (193, 191);  

-- Digital Logic Design ← Physics I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (261, 191);  

-- Electric Circuits ← Physics I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (201, 191);  

-- Discrete Structures ← Programming Concepts
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (205, 151);  




-- Year 2 → Year 2 & 3
-- Data Structures ← OOP
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (303, 251);  

-- Computer Architecture I ← Digital Logic Design
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (263, 261);  

-- Signals and Systems ← Electric Circuits
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (351, 201);  

-- Calculus III ← Calculus II
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (211, 1021);  

-- Operating Systems ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (405, 303);  

-- Algorithms ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (323, 303);  

-- Database ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (351, 303);  



-- Year 3 ← Year 2
-- Computer Architecture II ← Computer Architecture I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (363, 263);  

-- Microprocessor Design ← Computer Architecture I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (364, 263);  

-- Data Communication and Networks I ← Digital Logic Design
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (355, 261);  

-- Data Communication and Networks II ← Data Communication and Networks I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (457, 355);  

-- Numerical Methods ← Calculus III
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (300, 211);  

-- Digital Signal Processing ← Signals and Systems
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (476, 351);  

-- Cybersecurity ← Operating Systems
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (380, 405);  



-- Year 4 ← Year 3
-- Senior Project I ← Computer Engineering Practicum
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (498, 370);  

-- Senior Project II ← Senior Project I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (499, 498);  

-- Computer Interfacing ← Microprocessor Based Design
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (462, 364);  


-- CE Electives Prerequisites
-- Artificial Neural Networks ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (474, 303);

-- Artificial Neural Networks ← Probability and Statistics for Engineers
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (474, 200);

-- Wireless Networks and Applications ← Data Communication and Networks I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (488, 355);

-- Fundamentals of Digital Image Processing ← Numerical Methods
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (485, 300);

-- Modern Computer Organization ← Computer Architecture I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (470, 263);

-- Modeling and Simulation of Digital Systems ← Numerical Methods
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (481, 300);

-- Introduction to Robotics ← Digital Logic Design
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (483, 261);

-- Practical Training ← Completion of 60 Credit Hours
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (399, 0);  -- 0 indicates non-course prerequisite (credit hour requirement)

-- Computer Vision ← Digital Signal Processing
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (480, 476);

-- Computer Vision ← Data Structures
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (480, 303);

-- Hardware Software Co-Design ← Microprocessor Based Design
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (487, 364);

-- Multimedia Networks ← Data Communication and Networks I
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (482, 355);

-- Selected Topics in Computer Engineering ← Completion of 90 Credit Hours
INSERT INTO Course_prerequisite (course_id, pre_id) VALUES (471, 0);  -- 0 indicates non-course prerequisite

INSERT INTO Time_Slots (slot_id, advisor_id, available_date, time_slot) VALUES
(1, 1, '2025-03-25', '10:00-10:30'),
(2, 1, '2025-03-25', '10:30-11:00'),
(3, 2, '2025-03-26', '12:00-12:30'),
(4, 2, '2025-03-26', '12:40-1:10');

INSERT INTO Appointments (appointment_id, student_id, slot_id, advisor_id, timestamp) VALUES
(1, 1, 1, 1, '2025-03-25 10:00:00'),
(2, 5, 3, 2, '2025-03-26 12:00:00');


-- Inserting data into Study_plan_details table for CS Study Plan (2024)
INSERT INTO Study_plan_details (study_id, course_id, status) VALUES
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

-- Package Courses for CS Study Plan
(1, 3002, 'Humanities/Fine Arts Package'),
(1, 3003, 'Social/Behavioral Sciences Package'),
(1, 100, 'Natural Science/Mathematics Package'),

-- Elective Courses for CS Study Plan
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

-- Inserting data into Study_plan_details table for CE Study Plan (2021)
INSERT INTO Study_plan_details (study_id, course_id, status) VALUES
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

-- Package Courses for CE Study Plan
(2, 3002, 'Humanities/Fine Arts Package'),
(2, 3003, 'Social/Behavioral Sciences Package'),

-- Elective Courses for CE Study Plan
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


-- Corrected data for student_enroll table for all students

-- Student 1 (CS Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(1, 151, 'A', '2024-02-10'),
(1, 205, 'B+', '2024-03-01'),
(1, 251, 'A', '2024-03-15'),
(1, 101, 'B', '2024-04-05'),
(1, 310, 'A', '2024-05-10'),
(1, 355, 'B+', '2024-05-25');

-- Student 2 (CS Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(2, 303, 'B+', '2024-03-20'),
(2, 323, 'A', '2024-04-01'),
(2, 350, 'B', '2024-04-20'),
(2, 380, 'C+', '2024-05-05'),
(2, 405, 'A', '2024-05-15');

-- Student 3 (CS Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(3, 493, 'A', '2024-06-01'),
(3, 499, 'B+', '2024-06-15'),
(3, 300, 'A', '2024-07-01'),
(3, 360, 'B', '2024-07-20');

-- Student 4 (CE Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(4, 261, 'B+', '2024-02-10'),
(4, 351, 'A', '2024-03-05'),
(4, 201, 'B', '2024-03-25'),
(4, 231, 'C', '2024-04-10'),
(4, 211, 'A', '2024-04-25'),
(4, 263, 'B', '2024-05-10');

-- Student 5 (CE Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(5, 355, 'B+', '2024-02-20'),
(5, 364, 'C+', '2024-03-05'),
(5, 457, 'A', '2024-03-25'),
(5, 476, 'B', '2024-04-10'),
(5, 405, 'A', '2024-04-20');

-- Student 6 (CE Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(6, 498, 'A', '2024-05-10'),
(6, 499, 'B', '2024-05-25'),
(6, 462, 'C', '2024-06-05'),
(6, 470, 'B+', '2024-06-20');

-- Student 7 (CS Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(7, 300, 'A', '2024-02-15'),
(7, 312, 'B+', '2024-03-01'),
(7, 356, 'C', '2024-03-20'),
(7, 403, 'B', '2024-04-05'),
(7, 460, 'A', '2024-04-20');

-- Student 8 (CS Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(8, 433, 'B+', '2024-05-01'),
(8, 434, 'A', '2024-05-15'),
(8, 451, 'B', '2024-06-01'),
(8, 453, 'C+', '2024-06-20');

-- Student 9 (CE Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(9, 474, 'A', '2024-02-10'),
(9, 480, 'B+', '2024-03-01'),
(9, 487, 'C+', '2024-03-20'),
(9, 488, 'F', '2024-04-05');

-- Student 10 (CE Student)
INSERT INTO student_enroll (student_id, course_id, grade, date) VALUES
(10, 485, 'B', '2024-05-01'),
(10, 481, 'A', '2024-05-15'),
(10, 482, 'C', '2024-06-01'),
(10, 399, 'D+', '2024-06-20');

-- Inserting data into Student_Update table
INSERT INTO Student_Update (student_id, update_id, description) VALUES
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



-- Inserting data into Course_Update table
INSERT INTO Course_Update (update_id, course_id, timestamp, description) VALUES
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



-- Inserting data into Browse_Student table
INSERT INTO Browse_Student (student_id, brows_date, faq_id) VALUES
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



-- Inserting data into Browse_Adviser table
INSERT INTO Browse_Adviser (advisor_id, brows_date, faq_id) VALUES
(1, '2024-01-20 09:30:00', 201),
(2, '2024-02-25 11:15:00', 202),
(3, '2024-03-30 14:00:00', 203),
(4, '2024-04-28 16:45:00', 204),
(5, '2024-05-15 10:30:00', 205),
(6, '2024-06-22 12:20:00', 206),
(7, '2024-07-18 13:50:00', 207),
(8, '2024-08-09 15:35:00', 208),
(9, '2024-09-02 17:25:00', 209),
(10, '2024-10-11 08:45:00', 210);
