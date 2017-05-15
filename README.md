# Continuous Web App Development & Deployment Using Virtualization
Creating an environment for continuous development is not a process that can be easily implemented well. For this project we will be focusing on creating an environment for continuous development and deployment for a Flask web application. This tutorial will follow the steps necessary through using a linux machine for local development work, git and github for version control, docker and docker cloud for image virtualization, flask web applications for web development, ansible for automatic machine configuration management, and Amazon Web Services for virtual machine hosting.


# Project Flow
The general outline of this project will follow setting up this structure.
![Alt text](/readme_images/Continuous Development.jpg)

There will be three iterations made to the web application as follows:

* Creating Our Home Page With A Metrics Page
* Adding a Secondary Page
* Add a Third Page


This process flow will allow the end state of the tutorial to show how the staging and development process will work after the tutorial. The staging website will have the home page, metrics page, and two sub pages. The production site will have the home page, metrics page, and just one sub page.





# Tools We Will Use

## Git
Git will be used for the version control of this project. Git will keep track of all of the changes that are made to the project within the repository.

You will first need to create an account on [www.github.com](www.github.command).


## Docker & Docker Cloud
Docker and Docker Cloud will be used to build images of a container with which we can house our Flask server.

## Flask
Flask is a lightweight python based web application that will be used to build our website. In essence, it is a lighter version of Django.

## Amazon Web Services
We will be using a virtual machine hosted by Amazon Web Services to host our site. Amazon Web Services is a flagship provider in this area and it is worth checking out all of their services. In this project the machine has already been setup beforehand.

## Ansible
We will utilize Ansible play-books to setup our virtual machine automatically.

## Prometheus

## .yml Files

# Creating Our Home Page (First Run)

This first run in creating our home page and metrics page will require the most time. This is because we will be setting up our github repository, setting up our docker cloud repository with rules, setting up ansible, and finally setting up the metrics page along with the home page. This will require iterations through the process of committing changes, building new docker images, and publishing them on the AWS instance.


### Setting Up The Git repository
Once you have an account created on Github, go to your repositories page. Click on the green 'new' button to create a new repository. Choose a name for your project. The project demonstrated here is called fproject. You can include a description, but do not check the box to 'initialize this repository with a README', that will be done locally. Click create repository and you will be taken to a screen that shows you how to setup your repository locally on your machine.

Now, you will have to install git onto your local machine. To do this, go to your terminal and run the command

`apt-get install git`

You should see some installation progress messages coming across the screen. This will be the same for installing any other program onto your machine or the virtual machine. To test if the program installed correctly you can simply type the name into the terminal like a command, for example the command `git` will return a git menu within the terminal. We will now add the github repository to the local machine.You should place your local git repository inside of a an easily reachable directory such as Documents or Home. You can navigate to this directory by typing in

`cd Documents`

in the terminal. This is where we will place the repository. The following commands will create a directory and then go into that directory.

`mkdir fproject`

`cd fproject`

Then, within this repository we will run the git command

`git init`

This initializes an empty git repository inside this directory.

Now, we will start creating our files for our first commit on the master branch. What we will have at the end of this first commit is a README.md file, a CHANGELOG.md file, a DOCKERFILE, and a simple shell script that will run a dummy test to make sure everything is working correctly.

To create the README.md file, use the command:

`touch README.md`

 To edit the file you can use an editor such as nano. The command to open the file in terminal is:

 `nano README.md`

We can also add our other files by doing

`touch CHANGELOG.md`

`touch DOCKERFILE `

`touch docker-compose.test.yml`

`touch run_test.sh`

our CHANGELOG.md will keep track of all of the changes we make to our project.
It will essentially be a log of revision numbers, such as 0.0.1 for our first commit.

We can open up the CHANGELOG.md file and update its contents in this way:

`nano CHANGELOG.md`

Enter someting such as:

 "`0.0.1 First Git Commit, setting up DOCKERFILE with a dummy test`"

`CTRL+x to save`


We will now setup our Dockerfile. This is the file that Docker will execute.

So, now we must add

~~~~
FROM ubuntu:xenial

WORKDIR /src

COPY . /src
~~~~
to our Dockerfile. These commands in the Dockerfile will take a copy of a Ubuntu image, COPY whatever is in our current directory to the source directory, and finally set our working directory to the source directory.

Now we can setup our docker-compose.test.yml
We will now setup our run_test.sh file.

`touch run_test.sh`

In our run_test.sh file we will place the two lines.

~~~~
#!/bin/bash

echo "Hi"
~~~~

What these lines do is call bash from the shell script. The echo command will simply print out hi to the screen when executed. But, we need to make this shell script executable. To do this, run the command

`chmod +x run_test.sh`


The last file to update here is the docker-compose.test.yml file.

In this file we will place

~~~~
sut:
 build: .
 command: ./run_test.sh
~~~~

This yml file acts as a way of listing out the tests which an automated docker build should run. In this file, we will be running our run_test.sh test.

### Pushing our Github repository to Github and Docker Cloud.

Next we will push our changes to our github repository.
But first, we're going to set up our rules in our Docker cloud repository to build images from our Master git branch and our future git tags. To do this, we will have to create our docker cloud repository, syn our github repository with it, and then setup our build rule.

To setup our Docker Cloud Repository, on the docker site click on the "+" sign at the top of the page. On that page, put in the repository name, a description, and then click on the github icon under build settings. Select your github name from the organization drop down, and then your repository (fproject in this case). Scroll down and you will see the "build rules" section. There is one already setup for Master Branch, so click on the blue add icon and under source type select "tag", source "/^[0-9.]+$/", and Docker tag "release-{sourceref}".When you complete this, on the next page you should see a "Github Ping" test with a check-mark if completed successfully. These build rules are automatically set to create these builds automatically when the commits are pushed to github.

Now that we have our files set up, it's time to add our files to our local git repository, commit those changes, and then push them to the online repository. so, inside of our main directory we will run the commands.

`git add *`

Which makes the files within this directory ready for a commit.

`git commit -m "First commit, created README, CHANGELOG, Dockerfile, and run_test files."`

This creates a commit of files that are now ready to be pushed. The -m flag allows you to enter a message.

`git remote add origin https://github.com/tinkhamgreg/fproject.git`

This takes our local github repository and tells github.com that the repository we created earlier is the origin repository for our local repository.

`git push -u origin master`

This pushes our local commit to the master branch on github.com because we are still on our master branch locally.

If you go to your repository on cloud.docker.com you should see your Build in 'master" pending or starting. If you click on your build you can see the log output from docker cloud.

If successfull, you will see a "success" build status.


### Implementing Flask

From now on, we will do all of our new work in a different branch. So, for this next step we will cut a branch called flask, which will end with us having a home page and ready to implement ansible and prometheus. To cut the branch we can run

`git checkout -b "flask"`

which will automatically put us on the flask branch that we created with the -b flag.

At this stage, we need to make changing to some of our existing files. The first will be the Dockerfile. Our new Dockerfile will also have these commands after the `WORKDIR /src` command.

~~~~
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install Flask
COPY . /src
EXPOSE 8080
EXPOSE 8081

~~~~


What these new commands do is tell the Ubuntu image to update itself. The, to install python 3. After that pip3 will be installed. Finally, Flask will be installed using pip. We move the copy command so that everything is copied after we setup our environment. The expose commands expose the ports we will be using to publish the websites. 8080 will be used for the production site and 8081 will be used for the staging site.


Next, we will make changes to our run_test.sh file. We will now run the tests

~~~~
echo "Running Flask Unit Tests"
python3 fproject_test.py
~~~~

This will allow us to set up a page for specific tests in the fproject_test.py file that we will create next. To do this, use the touch command.

`touch fproject_test.py`

At this point we will also want to create the fproject.py file and our templates file using

`touch fproject.py`
`touch templates`


We will make changes to the fproject.py file first. Open up the file using the in terminal nano text editor and we will enter the following lines of code:

~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def run_flask():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
~~~~

What this code will do is import Flask from flask, and import a render_template module that will use special stying templates in our html files. Then, the code specifies the realtive directory "/" for the app. After that, the run_flask(): function returns our index.html page (the homepage). The if statement at the bottom turns on debugging and tells the operating system to listen to all public IP addresses.

Now we can move onto editing the fproject_test.py file. In this file we will have

~~~~
import unittest

import fproject


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
         pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Check that the page contains the desired phrase
        assert b'Continuous Development' in rv.data

if __name__ == '__main__':
    unittest.main()
~~~~

There is a lot here, but much like the other file we are importing the unittest module and fproject file, and creating a class with three functions. These three functions setup the test client, provide a tear down function, and test the home page. The home page is tested by asserting that the contents, in this case 'Looking At Liquidity' will appear on the page when published.


### Adding HTML Files
Finally, we will add our template directory and include in it our home page html file. To do this, we use the commands

`mkdir templates`

`cd templates`

`touch index.html`

Inside of the index.html file we will place

~~~~
<!DOCTYPE html>
<html>
<head>
	<h1>Continuous Development</h1>
</head>
<body>
</body>
</html>
~~~~

This places a basic html page inside of the file with a header reading "Continuous Development". This is what our assert function will find when it scans the page.


We're now ready to test our changes on DockerCloud. But first, we must update our CHANGELOG, tag these new changes so DockerCloud will test them properly, and push our tags up to Github. So, now that we have added new functionality to our website we can update the changelog to 1.0.0. We will mark this new version with "Implemented flask, created home page."

We can now add all the files to the git tree using `git add *` and then do our normal `git commit -m " "` command. Then, we will tag the commit by using:

`git tag 1.0.1` Then we can push this tag by using

`git push --tags origin flask`

which pushes these tags to our flask branch on github.

You should now see your new "1.0.0" tag building on DockerCloud. When successful, it will be time to merge this Flask branch into our master branch. This way, we can update our master branch with a version that we know has completed the necessary tests.


### Creating A Pull request

To do this, we will issue a pull request. On the github.com make your way to your repository's page. Then select the "tags" pane from the drop down menu, select the flask branch. Click on the green Create new pull request" button. You will be taken to a screen where you can make comments to the pull request's thread. After this, the pull request will remain open and our tests will run in Docker Cloud. Once successfully completed we can now merge the pull request into master. To do this, click on the "Merge pull request" button on the bottom of the pull request's page. Remember, you can access your pull requests any time by clicking on the Pull Requests tab on your Github page.

Now, we should update our local master branch on our machine. To do this use the commands:

`git checkout master`

`git pull origin master`

This tells git to switch to our master branch, and then pull down the master branch we just merged with the flask branch on Github.com.

### Ansible Creation

We will now move onto our next phase, which is using ansible to setup our environments automatically. This will
be a large part of the repository, and there is a lot of information contained within the ansible directory we will create. So, let's start with that by cutting a new ansible branch, then creating the ansible directory

Within the ansible directory we will now create four files and one directory.

* ansible.cfg
* configure-host.yml
* deploy-website-production.yml
* deploy-website-staging.yml
* DIRECTORY roles

We will now go through the list and go through what goes into each file and why.

* ansible.configured

~~~~
[localhost]
~~~~

This tells ansible to use the localhost IP address, 127.0.0.1.

* configure-host.yml

~~~~
---
# This playbook configures the local machine to run docker.

- name: Install the community edition of docker
  hosts: localhost
  become: true
  roles:
    - docker
~~~~
As told in our introduction, these yml files are what make up ansible playbooks. Going through the file, you can see the playbook sets up the host, localhost, which is our machine, to run the docker role that we will setup after setting these playbook files.

* deploy-website-production.yml

~~~~
---
---
# Runs the production website playbook.
- name: Deploy the production version of your website based on the previous tag$
  hosts: localhost
  become: true
  vars:
    fproject_environment: production
    fproject_image_version: release-1.0.6
    fproject_host_port: 8080
    fproject_container_port: 5000
  roles:
    - fproject
~~~~

There is a lot going on in this playbook but the concept remains the same. We tell ansible to use the fproject role that we will create and to use these variables underneath "vars:". These variables include the environment to use, production, the image version (which we update to 2.0.1), which will match our git tag, the host_port, or the port of the virtual machine we will use, and the container port, 5000, which is the port number that docker will use to connect with the virtual machine. The release numbers are not relevant now as we are not getting ready to use our metrics page and home page for deployment.


* deploy-website-production.yml

~~~
---
---
#Playbook for staging website.
- name: Deploy the staging version of your website based on the newest tag of y$
  hosts: localhost
  become: true
  vars:
    fproject_environment: staging
    fproject_image_version: release-1.0.5
    fproject_host_port: 8081
    fproject_container_port: 5000
  roles:
    - fproject
~~~~

This playbook does the same as the production playbook but for the staging site. You'll notice this is operating on the 8081 port and a working release behind (1.0.4).


### Editing Our roles

We will now work on our roles. In the roles directory we will need two sub directory roles. One for fproject and one for docker. We will start by creating two sub directories inside of the docker directory. These will be named "handlers" and "tasks". Inside of the handlers directory we will have a main.yml file. In this file we will have

~~~~
---
# Run apt-get update
- name: apt-get update
  apt:
    update_cache: yes
    cache_valid_time: 1800
~~~~

All this file does is tell docker to get update just like in our Dockerfile.

Now, back in our tasks directory under the docker directory we will need four files.

* install.yml

~~~~
---
# Install the docker service
- name: install docker dependencies
  apt:
    pkg: '{{ item }}'
    update_cache: yes
    cache_valid_time: 1800
  with_items:
    - apt-transport-https
    - ca-certificates  
    - curl
    - software-properties-common

# Add docker's GPG key
- name: Setup docker repository key
  apt_key:
    id: 0EBFCD88
    url: https://download.docker.com/linux/ubuntu/gpg
    state: present
  notify: apt-get update

# Determine what version of ubuntu is running

- name: Get release
  command: lsb_release -c -s
  register: release

# Here we add docker's repository to allow the system to do an apt-get install of
# official docker packages.
- name: Add docker repo
  apt_repository:
    repo: deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ release.stdout }} stable
    state: present
    filename: docker
  notify: apt-get update

# Install the docker service.  Fix the name of the package.
- name: Install the latest version of docker community edition
  apt:
    pkg: docker-ce
    update_cache: yes
    cache_valid_time: 1800
~~~~

There is a lot going on here, but the #comments do a good job of explaining. Basically, we are installing docker, using a special key for docker to allow the installation, installing docker packages, and then finally installing the docker service.

* main.yml

~~~~
---
# Include a series of tasks for setting up a docker service

- include: install.yml
- include: user.yml
- include: service.yml
~~~~

This main.yml file acts as a listing of what files to include in the docker installation.


* service.yml

~~~~
---
# This should ensure that the docker service is running.
- name: Ensure docker service is started
  service:
    name: docker
    state: reloaded
~~~~
This yml file tells ansible to make sure that the docker service is running.

* user.yml
~~~~
---
- name: Adding user to group docker
  user:
    name: "{{ 'student_usernamexxxxxxx' }}"
    group: docker
    append: yes
~~~~

This file adds your username to the linux group on the docker container.

Now that we have our tasks set up, we can now add a file to our handlers directory. In this directory we need a main.yml file. In this file we will have:
~~~~
---
# This is the handler that run apt-get update                   
- name: apt-get update
  apt:
    update_cache: yes
    cache_valid_time: 1800
~~~~

This handler runs the apt-get update task. Now our Docker role is all set we can setup our fproject role.

### Setting up our Project role

Now, in our fproject directory we will create two subdirectories, tasks and vars. Inside of the tasks directory we will just need one main.yml file. Inside of this file will be the contents:

~~~~
---
# Install docker python package.
- name: Ensure python docker-py package is installed
  pip:
    name: docker-py

# Starts or restarts the container.
- name: Start/Restart the container
  docker_container:
    name: "fproject-{{ fproject_environment }}"
    image: "{{ fproject_image }}:{{ fproject_image_version }}"
    command: "{{ fproject_command }}"
    state: started
    ports:
     - "{{ fproject_host_port }}:{{ fproject_container_port }}"

# This checks that the container that is started.
- name: verify that webserver is running
  uri:
    url: "http://52.53.194.21:{{ fproject_host_port }}"
    method: GET
~~~~

In this file we are having ansible install the docker python package, start our docker container, and check that our webserver is running. Now we will need to add a file to the vars directory under fproject. This will be another main.yml file with the contents:

~~~~
---
# Here we define variables in a key: value setting
# that will be used in the fproject role.
fproject_image: gtinkham/fproject
fproject_command: python3 fproject.py
~~~~

In this file we are defining variables that we called in our tasks file. Notice how we use the variables more than once in the tasks file.

We have now successfully added all of the files to ansible that we need. We will now try to test this out in the docker cloud.

We will do this by adding all of our files to the git tree, commiting the files, tagging the commit as 2.0.1, and pushing our tags to github. Be sure to be in the top directory of the project before adding all of the files. When the tests pass successfully, create a pull request, wait for its finish, and then  confirm the pull request and merge into the master branch. We can once again checkout the master branch locally and pull down the newly merged master branch from Github.com.

*Disclaimer!!!
While we just updated our repository with our ansible documents, we will not be fully testing this functionality until we go and place our docker container on our Amazon Virtual Machine. The next step after implementing the metrics page.

### Implementing The Metrics Page

Implementing the metrics page will require changing a few files that we have already created as well as creating one new file.

First, we will make an addition to our DockerFile. At the end of the file after we tell docker to install Flask, we must tell it to:

`RUN pip3 install prometheus_client`

We must also remove the EXPOSE commands as ansible will be handling that functionality.
Now that Docker will install the prometheus_client, we need to create a prometheus_metrics.py file to create a metrics page within Flask.  Within this page we will have the contents:

~~~~
import time
from flask import request
from flask import Response
from prometheus_client import Summary, Counter, Histogram
from prometheus_client.exposition import generate_latest
from prometheus_client.core import  CollectorRegistry
from prometheus_client.multiprocess import MultiProcessCollector

_INF = float("inf")
# Create a metric to track time spent and requests made.
REQUEST_TIME = Histogram(
    'app:request_processing_seconds',
    'Time spent processing request',
    ['method', 'endpoint'],
    buckets=tuple([0.0001, 0.001, .01, .1, 1, _INF])
)
REQUEST_COUNTER = Counter(
    'app:request_count',
    'Total count of requests',
    ['method', 'endpoint', 'http_status']
)


def setup_metrics(app):
    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def increment_request_count(response):
        request_latency = time.time() - request.start_time
        REQUEST_TIME.labels(request.method, request.path
            ).observe(request_latency)

        REQUEST_COUNTER.labels(request.method, request.path,
                response.status_code).inc()
        return response

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype="text/plain")
~~~~

What this python file does is import all of the relevant packages for prometheus, as well as some for calculating metrics such as time and Histogram. Then, it sets up a histogram and counter for the site statistics. Then, the setup_metrics function takes in an app, in this case fproject, and sets a time that can be referenced when pages are viewed. A counter is then incremented. Finally, the @app.route('/metrics') gives a url for the metrics page and the metrics() function displays the latest responses.

We also need to make changes to our fproject.py file so that our website renders the metrics page.

Inside of the fproject.py file we will add:

~~~~
from prometheus_metrics import setup_metrics
setup_metrics(app)
~~~~
underneath the `app = Flask(__name__)` line. This tells python to import the metrics and to run our application through the setup_metrics.

We are now ready to test these changes in docker cloud. Once again we will add this files to the git tree, commit them, tag the commit, and push the tag to Github.com.


## Hosting Our First Webserver on AWS

We now will take our website and place it on our AWS virtual machine. But first, we must login to the machine.

## SSHing Into The Amazon Virtual Machine
Our virtual machine has already been configured with git and ansible, as well as port 8080 and 8081 already open. So, in order to login to it we need two things, the IP address and the private key given.

The private key file **should not** be placed inside of the git repository. It should remain in a directory on your local machine that you can easily locate. In the same directory (such as Documents) is a good place. To ssh into the machine we would run the following command where gtinkham.key is the name of the key file, gtinkham the username, and the numbers following the @ symbol the ip address.

 `ssh -i gtinkham.key gtinkham@52.53.194.21`

 You may be asked if you wish to connect to the virtual machine. Type in yes. You should then see something such as:

`tinkham@ip-172-31-6-169:~$ `

in your terminal. You have successfully logged into the machine.

## Setting Up Our Virtual Machine

### Cloning Github Repository

The first thing we need to do is clone our github repository onto this machine. We can use the command:

`git clone https://github.com/tinkhamgreg/fproject.git`

to clone the fproject repository.

We will at this stage also cut a github branch for our initial AWS work in case we run into errors.

`git checkout -b aws`

### Setting Up Ansible

Now, we need to change some of the images for our staging and production environment. We want to use the two latest for production and staging, and set them up to feed our newest iterations as we go. If you remember, these will be inside of the ansible -> deploy-website-staging and deploy-website-production files. Update these so that our newest revision is in staging and our second newest is in production. Now, we will run the ansible configuration file. To do this, use the command:

`ansible-playbook configure-host.yml -v --extra-vars "student_username=xxxxxxx"`

where xxxxxxx should be replaced with the username you logged into the AWS with.

You will see lots of output on the screen, hopefully in yellow and green. If you see an error in red you should be able to look through the text and see where the error occurred, whether this be in the handler or tasks. Now, we are ready to deploy our two ansible playbooks, production and staging. To do this, we will go to our ansible directory and run:

`ansible-playbook deploy-website-production.yml -v`

You will see similar output to running the configure playbook. But, on the last task you will see in the output the url of our production webserver. http://[your IP address]:8080 You can now go there in your intnernet browswer and see the site. Now, because we did not add the Prometheus integration into this image, we will not see the /metrics page. So,now we will run our staging playbook.

`ansible-playbook deploy-website-staging.yml -v`

You will see a very similar output but with the port number 8081 that we placed inside the ansible playbook.

## * If You Need To Make Changes To The Project From The Virtual Machine

If for some reason you meet an error while working on the AWS instance, you can also send your changes on the AWS branch to github and go through the process of testing them and then merging them into master. While creating this, I had to add a line to the fproject.py code. So, I made the changes, updated the image that would be used in staging (3.0.2 instead of 3.0.1), and pushed the changes to be tested in docker cloud.

In the future, we will create a separate branch for every page that we add. If you do this, you will have to reconfigure git with your email and username like we did on the local machine. Then, simply add, commit, tag, and push the changes.

You should now be able to go to your url such as `http://52.53.194.21:8081/metrics`

You have now completed the first run of the project. From here, we will update our home page, add two new sub-pages, and simulate the development environment that will be used for continuation.

# Adding Another Page and Adding More Content.

Now that we have our site setup for development, we can add another page and make some stylistic changes to the html.

To do this, we will work from our local machine. So, we need to checkout the master branch locally and pull down our latest version of master.

We are now going to add a second page, as well as create some style changes to our home page.

### Adding style

To add style, we are going to use the bootstrap framework for our css files. This will allow us to use some style sheets we like without rewriting the book on style sheets. We will use three directories from this template. From the bootstrap website we can download Bootstrap Here [http://getbootstrap.com/getting-started/#download](http://getbootstrap.com/getting-started/#download) Once downloaded, extract the files and go into the first directory, you'll then see directories for css, text, and js. We will place these a newly added style directory in our home directory of our project.

Following directions from [https://v4-alpha.getbootstrap.com/components/navbar/](https://v4-alpha.getbootstrap.com/components/navbar/) we can see how to easily implement a navbar is. In our navbar we will have three pages. Home, Using The Cloud, and Best Practices.

Inside of our index.html file you will notice that we include the css files in a different way than normal. The Jinja templates uses a built in function to set the relative url of files. So in this case we use:

`<link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">`

for our stylesheet. We can now add some other information to our home page such as pictures and text.

### Adding Our Second page

We Are now ready to create our second page. In the templates directory create another html file, in this case cloud.html.

The cloud.html file should include the same html as the index.html file but changes to the title as well as content in the <body>.

Now that we have made our second page we will need to create another test for it in fproject_test.py. This will be exactly the same as the one for index.html but needs to look for text on the cloud.html page.

We also need to add another function to render our cloud page inside of the fproject.py file. This way our test will actually have a page to look at.

### Putting Our Second Page and Style Changes on AWS
Now, we should make changes to our ansible deployment playbooks now, so that they are ready to pull the newer image as soon as we update our github repository on the machine.

So, now our staging image will be 3.0.3 and the production image will be 3.0.2. We can now add all of our new files to the git tree, commit them, tag them, and push the commits for testing.


After this, we can go to our aws instance again and use:

`git pull origin master`

to pull down our latest commit. We can now run our ansible playbooks again for staging and deployment. These steps are the same as the "Setting up Ansible" section above.

~~~~
ansible-playbook configure-host.yml -v --extra-vars "student_username=xxxxxxx"

ansible-playbook deploy-website-production.yml -v

ansible-playbook deploy-website-staging.yml -v
~~~~


# Adding Our Third page

Note now that the production environment will just have our basic site, with metrics. The staging site will have our navbar, both of the pages, and the metrics page. At this point it is clear our website could use some more styling. Our navbar is lacking and we still need to add our last page for our navbar. So we can make these changes locally again.

So, we will start by cutting our last branch, subpage2.

Again, we will create a new html file, in this case called best.html. Then we will add this page to the fproject.py file and fproject_test.py file so that Flask will render the page and we can check for its output.

After making those changes we will update our ansible playbooks once again to make changes to which images we will host on our webserver.  These will now reflect:

Production: 3.0.4
Staging: 3.0.5


We will then add our new files, commit the changes, tag the commit, and push the tags up to do our last docker cloud test, pull request test, and merge the two branches. Then, we can log back into the AWS instance and deploy our updated webservers. After updating these webservers in production we will see our last staging image and in production we will see our latest revision.
