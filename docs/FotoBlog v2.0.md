# FotoBlog v2.0
## Instructions
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A simple web application that allows you to uploads photos, maintain a database with references to them, list them with their metadata, and more.

- Installation on vscode
- Cloning v.2.0
- ✨Magic ✨ Happens  ✨!


## Installation

FotoBlog requires [vscode IDE](https://code.visualstudio.com/) v1.75.1 to run.

Clone Git Tag by using the following syntax to clone a v2.0 tag:

```sh
git clone -b [tag_name] [repository_url]
git clone -b v2.0 https://github.com/giljr/fotoblog.git
```
The command clones tag v2.0 from the specified repository URL.

For development environments...

```sh
pip install -r requirements.txt
python ./manage.py migrate --run-syncdb
python ./manage.py runserver
```
You can now browse to the following link to start exploring the sample.
```sh
http://localhost:8000/
```

## Screeshots

The screenshots are available in this directory:
```sh
docs/fotoblog_v2:
```

## Step by Step


**1 >** The sample app will open the: 
```sh
00_sign_in_page.png
```

**2 >** Click 'Sign Up Now!' and the app will open the:
```sh
00_sing_up_page.png;
```
**3 >** As soon as you  loged in, the:
```sh
'Upload a Photo' 
``` 
will be opened;

**4 >** Choose a photo and submit in this form : 
```sh
01_upload_photo.png;
```
**5 >** You will see a page like this one: 
```sh
02_home.png; 
```
## Django Admin 
Also supports the **Django admin** which is available.
Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000/admin
```

#####  With virtualenv
We recommend and support the usage of virtualenv. All you need to do is create a new virtualenv (if necessary):


```sh
python -m venv ENV
```

And then just activate it:

```sh
source ENV/bin/activate
```
Import all the dependencies:
```sh
run pip freeze > requirements
```

Now you can go ahead with the instructions above.

@author: Gilberto Jr
@site: jungletronics
@url: https://medium.com/jungletronics
@date: feb, 2023
## License

MIT

**Free Software, 2023 Jungletronics!**
