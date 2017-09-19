# Starting a project: WINDOWS

Here are the steps you'll want to follow when starting a new project that will require python.

**Create a new virtual environment**

- Open up the command prompt and `cd` into the directory where your new project is going to live.
![command prompt cd process](img/cp-cd.png)
- Once you're there, use `mkdir` to create a directory with the name of your project
![command prompt mkdir process](img/cp-mkdir.png)
- `cd` into your newly created project directory
- Create your virtual environment and link it to your project directory with `mkvirtualenv [environment-name] -a ./`
-- `mkvirtualenv` is how we start the environment creation process
-- `[environment-name]` is the name of our environment. This can be anything you want, but I like to keep it similar if not the same as my project name
-- `-a` is a "parameter" of the `mkvirtualenv` function. It tells the virtual environment program which directory we want our virtual environment to sync to. `./` is the path of the directory that `-a` is talking about. So together, these two elements mean "sync my new virtual environment to the directory I'm currently standing in." If we wanted to sync our new virtual environment to a different directory, we could either supply a ABSOLUTE PATH or a RELATIVE PATH instead of the `./`.
![command prompt mkdir process](img/cp-virtualenv.png)

There are two ways to describe where files you're trying to reference live on your computer:
- You can specify the ABSOLUTE PATH of the file, which tells the computer to start from the root of your computer and work from there. You can find the ABSOLUTE PATH by entering this command into the command prompt `cd`.
- You can also specify a RELATIVE PATH of the file, which tells the computer to start from where you currently are and work from there. 

So, if you `cd` into a directory that looks like this:
![command prompt relative path](img/cp-relative-path.png)
- The ABSOLUTE PATH to the file `dogs.png` is `/Users/akanik/LPM/new_project/dogs.png`
- The RELATIVE PATH to the file `dogs.png` is `./dogs.png`
