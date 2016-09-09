# How To Use Heroku

This project shows you how to deploy a Python project to Heroku.

The code that comes with this project is working example of a small Python project that can be easily deployed to Heroku. To see the project in action, https://blooming-tor-8165.herokuapp.com/ .

Here are the basic steps to create a Heroku app.

 - Install Heroku
 - Create a Python script
 - Add some Heroku-specific files
 - Add it to a Git repository
 - Deploy to Heroku



## INSTALL HEROKU

The complete instructions for using Python with Heroku are here: https://devcenter.heroku.com/articles/getting-started-with-python#introduction . Everything I'm writing here is just commentary.

Sign up for Heroku: https://signup.heroku.com/dc

Make sure you have **homebrew**, **pip**, and **setuptools** installed. These should come with Python, but if they didn't, see the above link.

Here are some commands I ended up using, on Mac OS, to get past some installation issues. Maybe they'll be usefull to someone else.

    $ sudo chown -R `whoami`:admin /usr/local/
    $ sudo easy_install setuptools
    $ sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    $ sudo pip install virtualenv


## CREATE A PYTHON SCRIPT

It's probably going to be something that responds to a web request.

If you're too lazy to look at the other files in this project, here's what a simple website might look like:

    import web
    import datetime
    
    urls = (
      '/', 'index'
    )
    
    class index:
      def GET(self):
        return "The time is:", datetime.datetime.now()
    
    if __name__ == "__main__":
      app = web.application(urls, globals())
      app.run()


## ADD SOME HEROKU-SPECIFIC FILES

When you deploy an app to Heroku, it looks for three specific files. See my attached app for an example.

 - **Procfile**: This is the actual command(s) to run the app. Something like "web: python generate_rss_feed.py $PORT"

 - **requirements.txt**: This is a list of libraries and versions needed by your app. Each line looks like "web.py==0.37". I recommend running "pip freeze > requirements.txt" to generate the basic file, and then deleting all the lines you don't need.

 - **runtime.txt**: This is the version of python you need. Heroku doesn't have a lot of options, you'll probably use "python-2.7.9".


## ADD IT TO A GIT REPOSITORY

This is the simple part. Just create a local git repo for your project. If you're unfamiliar with **git**, just do this in the root folder of your project.

    $ git init
    $ git add .
    $ git commit -m'init'

And then everytime you change some files, do this.

    $ git add .
    $ git commit -m'updates'


## DEPLOY TO HEROKU

You deploy an app to Heroku via git. It's easy to set up. Just run this in the root folder of your project:

    $ heroku create

This does two things. First it creates a spot for app on Heroku's servers, you can see it on your dashboard at https://dashboard.heroku.com/ . Second it creates information about the that space as a remote repository in your project's .git/config file.

To actually deploy, you just push your code to the heroku server.

    $ heroku login

You have to this, just once, before you deploy.

    $ git push heroku master

It will tell you if you're successful or not. If not, it helpfully tells you almost nothing why. If you want to learn what really happened, go to your dashboard, go into your project, and check the logs.

One possible error: This will only deploy what is checked in to Git. If you have stuff that isn't checked in to Git, check it in, and deploy again.

### There's a few other basic heroku commands you can use:

    $ heroku open

Open the website with your app. (Will go to a browser window.)

    $ heroku logs --tail

See your logs live.

    $ heroku local web

Launch the app on your computer.


## CAVEATS

A lot of people want to use or modify an external file with Heroku. You can't realy do this, since Heroku doesn't have a filesystem. Instead you *can* have a website that dynamically creates the file everytime it is called, like you cane make the website respond to /my_feed.xml and create it on the fly. *Or* you can store files on Amazon's S3 service, which has a limited free trial.


## CREDITS

Justin McGuire &mdash; <jm@landedstar.com> &mdash; <a href="https://twitter.com/landedstar">@landedstar.com</a> &mdash; http://landedstar.com


## LICENSE

MIT

