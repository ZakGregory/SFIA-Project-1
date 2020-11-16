# League Of Legends Fanstasy League, aka. League Fantasy League!

The brife: To create a CRUD application using the tools covered up to this point in the couse, using Python, Flask, SQL and Jenkins.

The app is an esports based fantasy league where users can create their own teams and compete with their favriote players.

### User Stories

In order to create an minimum viable product (MVP) users stories are written to get the ideas for the basic features of the app:

* Add players to a players database
* Allow users to create their own team
* Allow users to add players to their team
* Update and remove player and teams
* Update players and teams with a score

### App design

The app will use 3 tables, a Teams table, a Players table, and a intermediate Picks table.
A Pick constits of a player and a team, meaning a player can belong to many teams and teams can have many players.



### CI Pipline

The app is built using Python code, using Flask as a webframework. This lets us use Jinja to template the webpages and display them to the user.
A MySQL server is used to hold the database for the project, and it is connected to using SQLAlchemy so changes in the app are reflected in the database.
We are using GitHub as the version control system, so that changes to the source code can be monitored and accesed from a virtual machine for testing and deployment.
Jenkins is used to build and deploy the app, building on git pushes, and being hosted using Gunicorn.

* Code is writen in Python, either on a VM or on a local machine
* Code is pushed to the VCS GitHub
* Jenkins is setup to build the app when GitHub recives a push request
* Jenkins runs a test build of the app on the VM it is running on for testing
* Any changes can be made to the source code and pushed to Git
* Once the app is complete, the build can be completed, artifacts made and the app pushed to live.

### Risk Assesment

| Problem                                      | Risk                                                                                                                            | Probability | Risk level | Current mitigation                                                                             | Proposed mitigation                                                |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| sql db passwords lost(eg uploaded to github) | The database can be accesed by anyone, meaning data could be changed by unauthorised users                                      | Low         | Low        | Use environment variables to store database uri                                                |                                                                    |
| VM goes offline                              | The app will be unusable untill hosted on another Vm                                                                            | low         | Medium     |                                                                                                | Have a backup vm spin up and host the app if the main vm goes down |
| Database goes offline                        | The app won't be able to query the database, rendering the app useless. Updates to the database will be lost, causing data loss | low         | medium     |                                                                                                | Create a backup SQL server                                         |
| Database is attacked/data lost               | Data is lost or deleted using SQL injection, where tables/databases could be dropped using SQL                                  | low         | Low        | Since no sensitive data is being stored, it is not critical to defend against database attacks | Make sure data is regularly backed up to a backup SQL server       |



### Pytest

The Pytest package is used to test the functionality of the code using asserst to see if the code is behaving correctly. Using the --cov flag can show the number of lines
which are tested, and the percentage of the overall app. Using test to check the status codes thrown by visiting each page, we can check each page is behaiving correctly.
Using the current tests, the App is X% tested.

### Future Improvments

For future improvment, I would make it so that each team can only have 1 player per position as currently an unlimited number of players can be added to one team.
I would also have liked to introduced a 4th scores table, where players scores can be stored by week, as typicaly 10 weeks of games are played per split.







