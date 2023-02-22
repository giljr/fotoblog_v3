# fotoblog_v3
## Fotoblog Fun Factory Archieve
Hi, this is all about [Django](https://www.djangoproject.com/) , a web framework for perfectionists with deadlines!
This is learning by doing: I am using openclassrooms, a leading E-learning Platform!:rocket:

Go to 
[Fotoblog Site Course](https://openclassrooms.com/en/courses/7107341-intermediate-django/)
```
A photography collective is looking 
for a way to share its work with the world. 

They want to be able to upload their photos online 
and also create blog posts about them. 

They have asked you, a Django developer, 
to build a web application that allows 
them to do just that. 

They need to have two tiers of users 
- subscribers and creators - and ensure that 
only the creators can create content. 

This content then needs to be shared in a social feed, 
with subscribers choosing which creators they want to follow.
```

I versioned every advance I made during the course (v3 here :).

For Version 2 please go to this [fotoblog_v2](https://github.com/giljr/fotoblog/)

Go to tags and download V3 working code package.

# FotoBlog v3.0
## Instructions - How To Install in vscode
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A simple web application that allows you to uploads photos, maintain a database with references to them, list them with their metadata, and more.

- Installation on vscode
- Cloning v.3.0
- ✨Magic ✨ Happens  ✨!


## Installation

FotoBlog requires [vscode IDE](https://code.visualstudio.com/) v1.75.1 to run.

Clone Git Tag by using the following syntax to clone a v3.0 tag:

```sh
git clone -b [tag_name] [repository_url]
git clone -b v3.0 https://github.com/giljr/fotoblog.git
```
The command clones tag v3.0 from the specified repository URL.

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

Bye!

Gilberto Jr

jaythree

date: feb23
