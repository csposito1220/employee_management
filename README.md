<h1>SEI-Project 3-Employee Management</h1>
<h2>Web Description - Employee Management</h2>

<p>Employee Management is a webpage where company admins can create and manage their employees. Normal employess can sign up and view everyone in the company but are unable to edit any information. With this webpage, managers can list out all employees positions, skills, and their availability schedule and change it as needed. Managers can also then filter out their employees based on their skill and what position they hold in order to find an employee to fill in or to promote.</p>
<h2>Employee Management Picture</h2>
<h4>Welcome page</h4>

![image](https://github.com/sfaigon/employee_management/assets/55246409/e37858eb-ee31-49a0-81ec-30049787d464)

<p>There is a simple greeting with four options in the nav bar, an about page, sign up page, login page, and home page all the way on the right with the logo icon</p>

<h4>Admin Logged in</h4>

![image](https://github.com/sfaigon/employee_management/assets/55246409/e72b78cb-831d-457a-a1e8-13c9f5b7c803)

<p>Admins have options such as Create Employee, Add Skill, Add Position. The first page after log in is the employee index. Here all employees are listed and there is a filter option to select employees with certain skills or positions. </p>

<h4>Employee Detail</h4>

![image](https://github.com/sfaigon/employee_management/assets/55246409/95d88111-7d7b-4c87-bf2a-0b868790df17)

<p>Once and employee is clicked, their details show up. The employees position, age, years employed, availability, and avatar are shown on a card. Admins can edit and terminate employees . Below, the employees skills are shown and also a list of available new skills to learn. Admins can add and remove skills for an employee</p>

![image](https://github.com/sfaigon/employee_management/assets/55246409/e04abdf2-97a7-4f52-bf2f-128c5f9bfb70)

<h2>Admin Add Employee</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/4a9634ab-a661-4447-a9f3-95dfbb8c2f72)

<h2>Admin Add Skill</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/3f674990-6689-49e6-a55b-6625e3d79c7f)

<h2>All Skills</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/199981c3-4dd6-4bb2-9e24-5634e9d45d3b)

<h2>Admin Add Position</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/9a46ea1d-555a-42b8-aff9-9b6838c733fa)

<h2>All Positions</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/481e047f-ba05-409f-be6b-ccf159f00fef)

<h2>About Page</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/319c5ffd-1b71-4da5-94a4-3a247a8e28aa)

<h2>Normal User Sign in</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/fe2463ef-a588-4fc7-b94c-604f57691d26)

<p>Normal users that sign up do not have the ability to edit or create</p>

<h2>Some Code Snippets</h2>

![image](https://github.com/sfaigon/employee_management/assets/55246409/3458db16-a387-4d7b-aa26-5e8ec63bc16e)

<p> This is the code behind the filtering function for employee lookup based upon the skills that they have and what position they hold in the company.</p>

![image](Photo-code.png)

<p> This is the code behind adding a photo as an avatar for the employees. The choose and upload photo functionality is hidden once a profile picture is chosen.</p>

![Alt text](image.png)

<p> This code makes sure that people signing up are not given superuser status, which limits what functions they will have access to.</p>

<h2>Next Steps</h2>

<ul>
    <li>When someone signs up or and employee is created, a user is created that corelates with eachother.</li>
    <li>A user that does not have superuser status will only be able to edit their own details page.</li>
    <li>Filtered employee list shows up as a modal.</li>
