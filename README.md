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


###Requirements


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

COPY . /src

WORKDIR /src
~~~~
to our Dockerfile. These commands in the Dockerfile will take a copy of a ubuntu image, COPY whatever is in our current directory to the source directory, and finally set our working directory to the source directory.

Now we can setup our docker-compose.test.yml
We will now setup our run_test.sh file.

`touch run_test.sh`

In our run_test.sh file we will place the two lines.

~~~~
#!/bin/bash

echo "Hi"
~~~~

What these lines do is call bash from the shell script. The echo command will simply print out hi to the screen when executed. Next we will push our changes to our github repository.

But first, we're going to set up our rules in our Docker cloud repository to build images from our Master git branch and our future git tags. To do this, we will have to create our docker cloud repository, syn our github repository with it, and then setup our build rule.

To setup our Docker Cloud Repository, on the docker site click on the "+" sign at the top of the page. On that page, put in the repository name, a description, and then click on the github icon under build settings. Select your github name from the organization drop down, and then your repository (fproject in this case). Scroll down and you will see the "build rules" section. There is one already setup for Master Branch, so click on the blue add icon and under source type select "tag", source "/^[0-9.]+$/", and Docker tag "release-{sourceref}".When you complete this, on the next page you should see a "Github Ping" test with a check-mark if completed successfully. These build rules are automatically set to create these builds automatically when the commits are pushed to github.

Now that we have our files set up, it's time to add our files to our local git repository, commit those changes, and then push them to the online repository. so, inside of our main directory we will run the commands.

`git add *`

Which adds all of the files within this directory to the git blob.

`git commit -m "First commit, created README, CHANGELOG, Dockerfile, and run_test files."`

This creates a commit of files that are now ready to be pushed. The -m flag allows you to enter a message.

`git remote add origin https://github.com/tinkhamgreg/fproject.git`

This takes our local github repository and tells github.com that the repository we created earlier is the origin repository for our local repository.

`git push -u origin master`

This pushes our local commit to the master branch on github.com because we are still on our master branch locally.

If you go to your repository on cloud.docker.com you should see your Build in 'master" pending or starting.




### Docker
Creating the first
### Flask
one web page

### SSHing Into The Amazon Virtual Machine
Our virtual machine has already been configured with git and ansible, as well as port 8080 and 8081 already open. So, in order to login to it we need two things, the IP address and the private key given.

The private key file **should not** be placed inside of the git repository. It should remain in a directory on your local machine that you can easily locate. In the same directory (such as Documents) is a good place. To ssh into the machine we would run the following command where gtinkham.key is the name of the key file, gtinkham the username, and the numbers following the @ symbol the ip address.

 `ssh -i gtinkham.key gtinkham@52.53.194.21`

 You may be asked if you wish to connect to the virtual machine. Type in yes. You should then see something such as:

`tinkham@ip-172-31-6-169:~$ `

in your terminal. You have successfully logged into the machine.

### Setting up our virtual machine with Ansible



# Second Run
subpage <- production

# Third Run
sub page

sub page <- staging
