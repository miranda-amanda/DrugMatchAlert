# DrugMatchAlert
#### Video Demo:  <[https://www.youtube.com/watch?v=xHgGgQVMI70](https://www.youtube.com/watch?v=xHgGgQVMI70)>
#### Description:
My web application serves as a tool to assess the potential risks associated with combining two types of medications or drugs. Upon accessing the index page, users encounter two input fields, allowing them to select a drug for each. Upon clicking 'verify,' the user receives an alert button, categorized as 'green alert,' 'yellow alert,' or 'red alert.' Clicking these buttons reveals an alert message detailing the potential risks associated with the specific drug combination selected. After clicking the green button, for instance, an alert message appears indicating that the combination typically poses minimal risks, indicating there are generally no significant risks when these drugs are used together. The Yellow button message indicates that there may be some risks associated with the combination in certain cases, which could affect their efficacy or lead to possible side effects. The Red button message indicates that the selected drug combination may present serious risks. This alert may appear if the user is attempting to take two of the same medications, which can lead to an excessive amount of the same type of medication, or if the combination of two different medications is known to be dangerous. This application always emphasizes the importance of seeking personalized advice from a healthcare provider for comprehensive guidance on medication interactions. It's crucial to note that while the application draws from extensive research, it cannot guarantee 100% accuracy.

This project utilizes Flask, a Python web framework, JavaScript, and SQL to create a user-friendly interface for querying a database of drug combinations and associated alerts.

Files and Functionality:
-app.py: This file contains the backend logic of the web application. It defines routes for handling user requests, such as verifying drug combinations, updating data, and retrieving drug information from the database. The file also includes functions for importing data from a CSV file into a SQLite database. Additionally, it interacts with the 'data.db' file, which serves as the SQLite database storing information about drug combinations and associated alerts.

-index.html: This HTML file serves as the frontend interface of the web application. It provides a form for users to select two drugs and verify their combination for potential interactions. The file also includes modal pop-ups to display alerts corresponding to different risk levels associated with drug combinations. Additionally, the web application utilizes data stored in the 'data.db' SQLite database to provide real-time information about drug interactions.

-data.db: This is the SQLite database file that stores information about drug interactions. It contains a table with combinations of drugs and their associated alerts, allowing the application to quickly retrieve and display relevant data to the user.

-data.csv: The database used in this project was created by me and, therefore, is relatively small and simple. It consists of three columns: the first two columns represent the types of drugs being combined, and the third column indicates the interaction or alert level associated with the combination of these two drugs. This structure allows the application to efficiently retrieve and display relevant information about drug interactions based on user input.

-JavaScript:is used within the index.html file to handle the user-side interactions and dynamic updates. When the user submits the form to verify a drug combination, JavaScript captures the input data and sends an AJAX request to the Flask backend. It then processes the JSON response and updates the page content accordingly, such as displaying the appropriate alert button and message. This enhances the user experience by providing a feedback without needing to reload the page.

Flask was chosen as the web framework for its simplicity and flexibility. It allows for rapid development of web applications with Python, making it a good choice for this project. SQLite was chosen as the database management system due to its lightweight nature and ease of use. It provides a simple solution for storing and querying drug combination data. Bootstrap was used to style the project, helping to create a clean and user-friendly interface. Additionally, a CSS file was utilized to further enhance the visual aesthetics and styling of the project.

Modal pop-ups were implemented to display alert messages corresponding to different risk levels associated with drug combinations. This design choice enhances user experience by providing clear and concise information about potential risks. The application’s overall design focuses on usability and accessibility, ensuring that users can easily navigate and understand the information provided.

In addition to utilizing some activities and lessons presented during the course, I also sought assistance from ChatGPT for certain parts of the code, as indicated within the comments. This was particularly helpful in overcoming difficulties and achieving the desired results.
