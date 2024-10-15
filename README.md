# msds460-assignment2
network models - project management

The Project Plan (version 8)

Developed by Thomas W. Miller. Revised September 17, 2024.

After many years of working for others, you have decided to start your own data science and software engineering firm. You will offer your services to other organizations as a sole proprietor and independent contractor. A first step in obtaining clients is often to respond to requests for proposal. 

This assignment concerns a development project. Suppose a group of restaurant owners in Marlborough, Massachusetts is requesting a project proposal. They want to know how fast you can develop a new software product and how much it will cost.

You need to propose a consumer-focused recommendation system for more than one hundred restaurants in Marlborough, Massachusetts, as shown in the enclosed file: restaurants-v001.json Download restaurants-v001.json. Data for the project will consist of Yelp reviews of these restaurants. This list of restaurants should be updated monthly, with Yelp reviews updated daily. Given the limitations of open-source Yelp reviews, it is likely that a contract will be obtained to access large quantities of Yelp data through its GraphQL API.

The client requires selected software components for the project. In particular, the client asks that the product recommendation system be implemented using Alpine.js and Tailwind on the frontend, a GraphQL API, and a Go web and database server on the backend. Go, Python, or R may be employed for recommender system analytics on the backend, with persistent storage provided by PostgreSQL, EdgeDB, or PocketBase. The system should be accessible from any modern web browser and may be hosted on a major cloud platform such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). 

While you expect to be involved in all aspects of the recommender system, you realize that the nature of the project calls for a software development team. You will need to hire people to fill various roles, including frontend developer, backend developer, data engineer, and database administrator, while you fill data science and project management roles.  

The project consists of the eight general tasks, and one of these general tasks, develop product prototype, comprises eight software development subtasks. An Excel spreadsheet shows fifteen tasks with their immediate predecessors: project-plan-v003.xlsx Download project-plan-v003.xlsx  Numerous columns are defined for workers assigned to the project. These columns may prove useful in activity/task scheduling in the future, but they are not used in the critical path analysis itself. Entries in these columns can be integers indicating the numbers of workers of each type assigned to the activity.

Determine best-case, expected, and worst-case estimates for the number of hours needed for each of the sixteen tasks. Also, determine an hourly rate associated with each worker role. These rates can be hourly rates (excluding benefits) that you would expect people in the roles to earn. Assume that all members of the team, like yourself, are working as independent contractors.

Deliverables (150 points total, 30 points for each part)

Paper (pdf file). The paper/write-up should be submitted as a pdf file (double-spaced, 4 pages max). Think of the paper as comprising the methods and results sections of a written research report. If you like, provide a paragraph on methods and a paragraph about results for each part of this assignment. 

Program code (text link to GitHub repository). Key information from the paper should also be included in the README.md markdown file of a public GitHub repository.  The GitHub repository should include text files for the program code (.py extension for Python), and program output (.txt extension). Excel files should also be included in the GitHub repository. Include the web address text (URL) for the GitHub repository in the comments form of the assignment posting. You should be providing a link to a separate repository that can be cloned. It should end with the .git extension.

Uploads are restricted to files with pdf, md, and txt extensions.

Part 1: Problem setup.  Describe the work that you have completed, posting the updated Excel spreadsheet of tasks, completion times, per-hour costs, and persons responsible. Describe any areas of uncertainty regarding project components, time, or cost estimates. Draw a directed graph diagram for the project. Note tasks that can be completed in parallel.
Part 2: Model specification. Specify a linear programming model for the project plan. Show how time and cost estimates play into the specification. In specifying the objective function, you can make the simplifying assumption that all contributors to the project charge the same hourly rate. That is, a minimum total time solution will be the same as a minimum total cost solution.
Part 3: Programming. Implement the linear programming problem using Python PuLP or AMPL. Provide the program code and output/listing as plain text files, posting within a GitHub repository dedicated to this assignment. 
Part 4: Solution. Solve the project plan using best-case, expected, and worst-case time estimates with a minimum-time or minimum-cost objective. Describe your solution. Identify the critical path for the project under each scenario. Construct Gantt charts for the best-case, expected, and worst-case solutions. Note that Microsoft provides Gantt chart templates for Excel Links to an external site..
Part 5: Overview. Write a brief overview of the project for the prospective client. Ignoring costs associated with software licensing and cloud hosing, what would you charge for the project? When would you expect to be delivering the product prototype? How soon could you deliver the product prototype if additional independent contractors were added to the mix?
Note. Critical path analysis, as we are using it in this assignment, assumes that there are no resource constraints. This is an unrealistic assumption for most projects.  Suppose that each member of the project team is able to work on a subset of the activities and that each member of a hypothetical project team is able to work a limited number of hours each day. Note that adding constraints of this type would require an integer programming or mixed integer programming approach to the critical path/scheduling problem. Alternatively, we could approach the problem using discrete event simulation. 

Do not address resource constraints in developing the project plan for this assignment. Stick to a straightforward critical path analysis. 
