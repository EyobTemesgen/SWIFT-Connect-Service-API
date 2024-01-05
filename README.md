# SWIFT Connect Onboarding Service  

## Overview
Haron Computer is transitioning from manual onboarding processes to an electronic process for onboarding business customers onto their SWIFT Connect service. This README provides an overview of the requirements, design, technology stack, and instructions for setting up and running the project.
## Here are key questions to ask during requirements gathering and design flow for the web and CRM module parts
## Understanding Current Process:
o	How does the current manual onboarding process work, systematically?
o	What pain points or bottlenecks exist in the current process?
o	What are the key success metrics for the onboarding process?
## Web Application:
o	What information do potential customers need to provide during registration?
o	What service options and customizations should be available for selection?
o	What validation rules need to be applied to submitted data?
o	How will customers track the progress of their requests?
o	What support resources should be available on the web application?
## CRM Module:
o	How will requests be organized and assigned to managers?
o	What data fields and information are essential for managers to review?
o	What communication channels should be available within the CRM (email, chat, calls)?
o	What are the different stages of the onboarding process, and how will statuses be updated?
o	What integrations are needed with other systems (payment gateways, SWIFT API)?
o	What reports and analytics are needed to track onboarding performance?
## Security:
o	What authentication methods will be used for user logins?
o	How will sensitive data be protected (encryption, access controls)?
o	What measures will be taken to prevent unauthorized access and data breaches?
## User Experience:
o	What are the target user groups and their technical skill levels?
o	What are the usability goals for both the web application and CRM module?
o	How can the interfaces be designed to be intuitive and user-friendly?
## Integration:
o	How will data flow between the web application and CRM module?
o	What APIs or integration points are needed to connect with payment systems or SWIFT API?
## Scalability and Performance:
o	How many users and requests are expected to be handled by the system?
o	What are the performance goals in terms of loading times and responsiveness?
o	How can the system be designed to scale with increasing demand?
## Maintenance and Support:
o	Who will be responsible for maintaining and updating the system?
o	What procedures will be in place for troubleshooting and resolving issues?
o	How will user feedback be collected and incorporated into future improvements?

## Requirements Gathering & Design Flow

### User Profiles
- Admin/Manager: Responsible for overseeing and managing the onboarding process.
- Business Customer: Engages with the web interface to submit onboarding requests.
- CRM User: Handles request processing and verification in the CRM module.

### Requirements
#### Functional Requirements
- Web Interface:
  - User authentication and authorization
  - Form to collect business customer details and requirements
  - Submission process and confirmation
- CRM Module:
  - Request management dashboard for CRM users
  - Verification workflow for submitted requests
  - Integration with existing CRM functionalities

#### Non-functional Requirements
- Security measures for data protection
- Scalability to handle increasing onboarding requests
- User-friendly interfaces with intuitive design

### Wireframe - CRM Module Onboarding Request Processing Screens
 open the following link and play it to see the sample wireframe design for onboarding request form
https://www.figma.com/file/qmiRiKbfmkQnD0xqdKCnUg/SWIFT-Connect-Service?type=design&node-id=0%3A1&mode=design&t=JvLBMt9WB4xYb3yz-1

## Technology Stack
- Python Django: Backend development and business logic implementation
- HTML/CSS/JavaScript (Bootstrap framework): Frontend development for the web interface
- SQL: Database for storing onboarding requests and customer data

## Setting Up & Running the Project
1. Clone the SWIFT-Connect-Service-API repository: `https://github.com/EyobTemesgen/SWIFT-Connect-Service-API.git`
2. Set up the Python environment and dependencies. (install python, create virtual environment and activate virtual environment)
3. Start the Django development server, (python manage.py run server)
4. Access the web interface and CRM module SWIFT Connectivity module.
   ![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/c638c60b-edcb-49d6-bf1d-3b68b0451ade)

![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/825108fc-d349-4de4-ab13-df1f2b2ef71f)


![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/f6ffe5b6-842f-42a5-a840-a8d3807e6f4b)

![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/e3551fb3-2836-45fc-af5e-96996b7b5fbc)

![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/6c158bc4-1622-4374-aa71-453cbdf61326)

![image](https://github.com/EyobTemesgen/SWIFT-Connect-Service-web/assets/111111244/3aaa4c24-710b-460d-8822-6dcd5b6c11a4)
