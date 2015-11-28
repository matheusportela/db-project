# db-project
This project is a course requirement for the Databases class of 2015, at the University of Brasília.

# Dependencies
* PostgreSQL 9.4.5
* Psycopg 2.6.1

## Installing PostgreSQL
On Mac OS X, install PostgreSQL via [Homebrew](http://brew.sh/).

```sh
$ brew install postgresql
```

In order to launch PostgreSQL, run the commands bellow. It will start PostgreSQL at login.

```sh
# ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
# launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
```

Should you want to run PostgreSQL without launching it at login, run the following command.

```sh
$ postgres -D /usr/local/var/postgres
```

PostgreSQL standard installation also provides a command-line interface for database interaction.

```sh
$ psql <database>
```

## Installing Python dependencies
The command bellow installs all necessary Python dependencies.

```sh
$ pip install psycopg2
```

# Configuration

First, it is necessary to create a database to operate with the project. Let's create a `healthdb` in PostgreSQL with the command bellow.

```sh
$ createdb healthdb
```

Should you need to delete the created database, just drop it with the following command.

```sh
$ dropdb healthdb
```

# Specification
In this project, we develop a system able to store and query data for public health management.

# Entity-Relationship Model
![](docs/entity_relationship_model.png)