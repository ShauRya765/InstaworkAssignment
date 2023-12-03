# Instawork Assignment

## Getting Started

### Prerequisites

- Python (3.11 recommended)
- pip
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ShauRya765/InstaworkAssignment.git
   cd InstaworkAssignment

## Create a virtual environment named 'venv' (or any other name of your choice)
python3 -m venv venv

## Activate the virtual environment

1. **For MAC:**
   ```bash 
      python3 -m venv venv
      source venv/bin/activate

2. **For Windows Command Prompt:**
   ```bash 
      python -m venv venv
      venv\Scripts\activate

3. **For Windows Powershell:**
   ```bash 
      python -m venv venv
      .\venv\Scripts\Activate

## Install project dependencies and runserver
1. ```bash 
   pip install -r requirements.txt
2. ```bash 
   python manage.py runserver

## Initial Steps to create Database
1. ```bash 
   python manage.py makemigrations
2. ```bash 
   python manage.py migrate

## Steps to create a superuser to view database
1. ```bash 
   python manage.py createsuperuser
   

**NOTE:**
If any of the above commands don't work, try to run them using **pip3** or **python3** instead of **pip** and **python**

