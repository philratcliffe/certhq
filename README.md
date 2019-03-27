# CertHQ
Central store and API for certificate information

# Running CertHQ in Production (AWS Elastic Beanstalk)
eb init (this will set the default values for the EB app - call it certhq)

eb create (create an environment to run the app in - e.g certhq staging)
 
# Running CertHQ in Development
Set the settings environmental variable:

export DJANGO_SETTINGS_MODULE='config.settings.local'

# React Frontend
See this [guide](https://www.digitalocean.com/community/tutorials/how-to-build-a-modern-web-application-to-manage-customer-information-with-django-and-react-on-ubuntu-18-04)

## Setting up React
Install nodejs and npm
cd frontend and run npm install

## Running React frontend
$ npm start
