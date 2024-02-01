# School Manager API

School Manager API is a RESTful web service that allows you to manage student information, courses, and student enrollments. **This project was developed with the aim of studying, improving and applying knowledge of Python, Django, Rest API, PostgreSQL and Docker. Although it is an educational project, it is fully functional**. It provides endpoints for creating, retrieving, updating, and deleting records in these three categories. This README provides an overview of the API and instructions on how to use it.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Practical Example School Manager API](#practical-example-school-manager-api)
  - [Running the Container](#running-the-container)
- [Authentication](#authentication)
- [Usage](#usage)
  - [Accessing Swagger UI](#accessing-swagger-ui)
  - [Accessing ReDoc](#accessing-redoc)
- [Endpoints](#endpoints)
  - [Students](#students)
  - [Courses](#courses)
  - [Enrollments](#enrollments)
- [Filters](#filters)
- [Examples](#examples)
- [Contributing](#contributing)

## Getting Started

### Prerequisites

- Python 3.11+
- Docker 24.0+

### Practical Example School Manager API

As previously mentioned, this project aims to demonstrate knowledge of languages and technologies. Below is a version of the API hosted on the Render website, in order to demonstrate how it works in practice:

- https://school-manager-api-ojvm.onrender.com/

### Running the Container

1. Clone this repository to your local machine:

    ```shell
    git clone https://github.com/school-manager-api.git
    ```

2. Change into the project directory:

    ```shell
    cd path/to/school-manager-api
    ```

3. Set enviroment variables:

    Add an .env file to set the enviroment variables.

    3.1. Set DJANGO_ENV:

    - Set the value of the DJANGO_ENV variable to "development" or "production", depending on which environment you are working in:

        ```
        DJANGO_ENV=replace_this_to_development_or_production
        ```
    
    3.2. Set SECRET_KEY:

    - Access the Python Interactive Shell and import the get_random_secret_key() function from django.core.management.utils:

        ```shell
        >>> from django.core.management.utils import get_random_secret_key
        ```

    - Generate the Secret Key in the Terminal using the get_random_secret_key() function:

        ```shell
        >>> print(get_random_secret_key())
        ```

    - Set django's SECRET_KEY:

        ```
        SECRET_KEY=replace_this_with_your_generated_secret_key
        ```
        
    3.3. Set the database variables:

    - By default, django uses the sqlite3 database, but it can be changed to another, such as PostgreSQL, which we will be using in this project. To simplify this configuration, the render website offers PostgreSQL management and hosting with internal and external connectivity, multiple storage and memory options and automated daily backups.

    - Once the PostgreSQL database has been created on the render website, to run locally, you need to copy the value defined in External Database URL and set it as the value of a DATABASE_URL environment variable.

        ```
        DATABASE_URL=replace_this_with_your_external_database_url
        ```
    
    - But if you're hosting the web service on render too, you need to copy the value defined in Internal Database URL

        ```
        DATABASE_URL=replace_this_with_your_internal_database_url
        ```
    
    Set the superuser variables:

    - Finally, you will need to set the DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD environment variables for the superuser settings, which will be used to create it.
    
        ```
        DJANGO_SUPERUSER_USERNAME=replace_this_with_your_username
        DJANGO_SUPERUSER_EMAIL=replace_this_with_your_email
        DJANGO_SUPERUSER_PASSWORD=replace_this_with_your_password
        ```

4. Run

    4.1. Locally:

    You can run the application detached from the terminal by adding the -d option. Inside the directory, run the following command in a terminal.

    ```shell
    docker compose up --build -d
    ```

    Open a browser and view the application at http://localhost:8000.

    In the terminal, run the following command to stop the application.

    ```shell
    docker compose down
    ```
    
    4.2. In production:

    Docker offers us a number of advantages for when we put a service into production, such as: portability, isolated environments, ease of deployment, etc. That's why we chose to use it.

    - Make sure you are logged in to Docker Hub:

        ```shell
        docker login
        ```
        This will ask for your Docker Hub credentials.

    - Build the Docker image:

        ```shell
        docker build -t your-user/your-repository:tag .
        ```
        - your-user: Your username on Docker Hub.
        - your-repository: Name of the repository you want to create.
        - tag: Version or tag of your image.

    - Upload the image to Docker Hub:

        ```shell
        docker push your-user/your-repository:tag
        ```

        This will send your image to Docker Hub, making it available for use.
     
## Authentication

The API uses Basic Authentication to secure endpoints. To access protected endpoints, you will need to include your credentials in the request headers. Make sure to use HTTPS in production for secure authentication.

On the other hand, since the practical example provided to demonstrate the api is for study purposes only, credentials will be provided, as no sensitive data will be exposed:

- user: admin
- password: password

## Usage

### Accessing Swagger UI

Swagger UI provides an interactive interface for exploring and testing the API endpoints. To access Swagger UI, open your web browser and go to:

-   ```http
    http://localhost:8000/swagger/
    ```
    if the API is running locally.

-   ```http
    https://school-manager-api-ojvm.onrender.com/swagger/
    ```
    if you want to access the practical example of the API hosted on render website.


### Accessing ReDoc

ReDoc is another documentation tool that provides a clean and responsive way to browse API documentation. To access ReDoc, open your web browser and go to:

-   ```http
    http://localhost:8000/redoc/
    ```
    if the API is running locally.

-   ```http
    https://school-manager-api-ojvm.onrender.com/redoc/
    ```
    if you want to access the practical example of the API hosted on render website.

ReDoc presents the API documentation in a visually appealing format, making it easy to understand and navigate.

## Endpoints

### Students

- **GET /students/**: Retrieve a list of all students.
- **GET /students/{student_id}/**: Retrieve details of a specific student.
- **POST /students/**: Create a new student record.
- **PUT /students/{student_id}/**: Update the details of a specific student.
- **DELETE /students/{student_id}/**: Delete a student record.

### Courses

- **GET /courses/**: Retrieve a list of all courses.
- **GET /courses/{course_id}/**: Retrieve details of a specific course.
- **POST /courses/**: Create a new course.
- **PUT /courses/{course_id}/**: Update the details of a specific course.
- **DELETE /courses/{course_id}/**: Delete a course.

### Enrollments

- **GET /enrollments/**: Retrieve a list of all student enrollments.
- **GET /enrollments/{enrollment_id}/**: Retrieve details of a specific enrollment.
- **POST /enrollments/**: Create a new student enrollment.
- **PUT /enrollments/{enrollment_id}/**: Update the details of a specific enrollment.
- **DELETE /enrollments/{enrollment_id}/**: Delete a enrollment.

## Filters

You can filter the results of GET requests using query parameters:

- **/students/?search=John**: Search for students with the name "John."
- **/enrollments/?student_id=1&course_id=2**: Filter enrollments for a specific student (ID 1) and course (ID 2).

## Examples

Here are some examples of using the API:

- **Create a new student**:

    ```http
    POST /students/
    Content-Type: application/json

    {
    "name": "John Doe",
    "cpf": "123.456.789-09",
    "birthday": "2000-01-01"
    }
    ```

- **Retrieve a list of courses:**:

    ```http
    GET /courses/
    ```

- **Update a enrollment:**:

    ```http
    PUT /enrollments/1/
    Content-Type: application/json

    {
    "period": "E"
    }
    ```

- **Delete a student:**:
    ```http
    DELETE /students/1/
    ```

## Contributing

### Tool

This project uses `Poetry` for environment management and library installation, so make sure you have Poetry installed for this contribution:

```sh
pipx install poetry
```

### Contributing Process

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

    ```
    git clone https://github.com/<your-user>/school-manager.git
    ```

3. Install dependencies.

    ```
    poetry install
    ```

4. Use Git Flow as your workflow to help organize the versioning of your code.

    Git Flow works with two main branches, Develop and Master, which last forever; and three supporting branches, Feature, Release and Hotfix, which are temporary and last until you merge with the main branches.
    So instead of a single Master branch, this workflow uses two main branches to record the project's history. The Master branch stores the official release history, and the Develop branch serves as a merge branch for features.
    Ideally, all commits in the Master branch are marked with a version number.
    - **Master/Main Branch**: where we have all the production code. All new features that are being developed, at some point, will be merged or associated with the Master. The ways to interact with this branch are through a Hotfix or a new Release.
    - **Develop Branch**: where the code for the next deployment is located. It serves as a timeline with the latest developments, this means that it has features which have not yet been published and which will later be associated with the Master branch.
    - **Feature Branch**: used for the development of specific features. It is recommended that these branches follow a naming convention, the most used convention is to start the branch name with feature, for example, "feature/feature-name". It is important to know that these feature branches are always created from the Develop branch. Therefore, when they are finished, they are removed after performing the merge with the Develop branch. If we have ten features to develop, we create ten independent branches. It is important to note that feature branches cannot have interaction with the master branch, only with the develop branch.
    - **Hotfix Branch**: created from the master to make immediate fixes found in the production system. When completed, it is deleted after merge with the master and develop branches. We have a hotfix branch for every hotfix we need to implement! The big difference between Feature Branches and Hotfix Branches is that Hotfixes are created from the Master Branch and when we finish them, they are merged into both the Master Branch and the Develop Branch. This is because the bug is in both environments. Also, when we close a Branch Hotfix, we have to create a tag with the new project version. This is because every change we make in the Branch Master needs a tag that represents it.
    - **Release Branch**: serves as a bridge for merge from Develop to Master. It works as a testing environment and is removed after the merge tests with the Master. If a bug is found and changes are made, it must also be synchronized with the Develop Release. Finally, when we close a Branch Release, we have to create a tag with the new release version of the software, so that we can have a complete history of the development.

5. Make the necessary changes to the codebase.

6. In case of changes to the project dependencies, generate a new requirements.txt file that will be used in docker.

    ```sh
    pip freeze > requirements.txt
    ```

7. Commit your changes with a descriptive commit message using the conventional commit format.

	```sh
	<type>[optional scope]: <description>
	[optional body]
	[optional footer]
	```

8. Push your branch to your forked repository on GitHub. For an example of a feature:

	```bash
	git push origin <feature/feature-name>
	```

9. Open a pull request from your branch to the main repository.

10. Wait for the maintainers to review your changes and address any feedback if necessary.

11. Once your changes are approved, they will be merged into the main repository.

If you have any questions or need assistance during the contribution process, feel free to open an [issue on the project's GitHub repository](https://github.com/Raulin0/school-manager/issues) and ask for help.
