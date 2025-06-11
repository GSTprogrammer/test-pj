# Freelance API (Mini Upwork System)

A simple Django REST Framework-based API that allows:
- Clients to post projects
- Freelancers to send proposals
- Clients to accept/reject proposals (only one can be accepted per project)

##  Features

- Custom user model with roles: `client` and `freelancer`
- JWT Authentication with access & refresh tokens
- Clients can create projects
- Freelancers can submit proposals
- Clients can view proposals and accept/reject them
- One proposal can be accepted per project
- Protected access with custom permissions
- Paginated project listing
- API documentation using Swagger (drf-yasg)
- Unit test included

##  Installation

1. Clone the repo or unzip the project:
   ```bash
   git clone <your_repo_url>
   cd freelance-api



## DOCS

http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/


## TEST
python manage.py test


## Project Structure
freelance-api/
├── config/
│   └── settings.py, urls.py, ...
├── core/
│   └── models.py, views.py, serializers.py, urls.py, ...
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
