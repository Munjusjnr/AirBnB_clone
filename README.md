![A simple logo of airbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230716%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230716T132759Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c2c6d5242f8d7952e65dfc1c05fd254a22b1b74fea4d2dfade88ad8f069bcf2)
# Background Context
## Welcome to the AirBnB clone project!
### Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

	- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances.
	+ create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
	* create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`.
	- create the first abstracted storage engine of the project: File storage.
	+ create all unittests to validate all our classes and storage engine.

## What’s a command interpreter?
This project falls inline with a previous project done once before, which was the simple shell project. It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

	- Create a new object (ex: a new User or a new Place).
	* Retrieve an object from a file, a database etc….
	+ Do operations on objects (count, compute stats, etc…).
	- Update attributes of an object.
	* Destroy an object.

### Execution
This is an example of how to start and use the **console** in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
This is an example in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
