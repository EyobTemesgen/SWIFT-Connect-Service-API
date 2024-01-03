# SWIFT Connect Service Electronic Onboarding

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

### Wireframe - CRM Module Request Processing Screens
 open the following link and play it to see the sample wireframe design
https://www.figma.com/file/qmiRiKbfmkQnD0xqdKCnUg/SWIFT-Connect-Service?type=design&node-id=0%3A1&mode=design&t=JvLBMt9WB4xYb3yz-1

## Technology Stack
- Python Django: Backend development and business logic implementation
- HTML/CSS/JavaScript (Bootstrap framework): Frontend development for the web interface
- SQL: Database for storing onboarding requests and customer data

## Setting Up & Running the Project
1. Clone the SWIFT-Connect-Service-web repository: `https://github.com/EyobTemesgen/SWIFT-Connect-Service-web.git`
2. Clone SWIFT-Connect-Service-API repository:
3. Set up the Python environment and dependencies.
4. Create and configure the SQL database.
5. Run the necessary scripts to set up tables and initial data.
6. Start the development server.
7. Access the web interface and CRM module SWIFT Connectivity.
