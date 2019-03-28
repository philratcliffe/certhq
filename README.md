# CertHQ
Central store and API for certificate information

## Running CertHQ in AWS Elastic Beanstalk
Run **eb init** to initialise an EB app and set its default values.

```bash
$ eb init
```

Run **eb create** to create each environment you wish to run the aforementioned
app in.

## Settings
### Development
export DJANGO_SETTINGS_MODULE='config.settings.local'

### Production
export DJANGO_SETTINGS_MODULE='config.settings.prod'

## React Frontend
See this [guide](https://www.digitalocean.com/community/tutorials/how-to-build-a-modern-web-application-to-manage-customer-information-with-django-and-react-on-ubuntu-18-04) for details on running a React frontend.

## Setting up React
Install nodejs and npm
cd frontend and run

```bash
$ npm install
```

## Running React frontend

```bash
$ npm start
```
