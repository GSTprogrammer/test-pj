# Freelance API (Mini Upwork System)

A simple Django REST Framework-based API that allows:
- Clients to post projects
- Freelancers to send proposals
- Clients to accept/reject proposals (only one can be accepted per project)

## 🔧 Features

- Custom user model with user type (client/freelancer)
- JWT Authentication (Simple JWT)
- Project creation (clients only)
- Proposal submission (freelancers only)
- View proposals for a project (owner only)
- Accept/Reject proposals
- Swagger API docs
- Pagination enabled
- Simple unit tests included

## 🛠️ Installation

```bash
git clone <repo_url>  # یا فایل زیپ رو ازبین ببرید
cd freelance_api
python -m venv venv
source venv/bin/activate  # یا venv\Scripts\activate در ویندوز
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
