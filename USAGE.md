Nerd stuff below, don't read if you are not interested in hosting Kanon yourself.

## Installation

Linux:

```sh
git clone https://github.com/zunjae/KanonApp.git
cd source code
bash setup.sh
python3.5 __init__.py
```

## Development setup

The source code is just the server. You still need some data. There are plenty of ways to get them yourself. I use https://github.com/manami-project/anime-offline-database (licensed under GNU Affero General Public License v3.0)

In order to run KanonApp you need to following dependencies:

* Python
    * sqlite3, flask, flask limiter, 
* Apache2 if you want to run it on a production server

## Roadmap

* Controllers/Repository/Decorators should be in separate classes
* Rate limits should be based on the user_token instead of remote address

## Vision

* The server should never use an ORM mapper because it adds unnecessary complexity to the project
* The Zdb class is responsible for saving or retrieving data from the SQLite database
* The server should be hosted on a server running Apache 2
* Rate limits should be strict

## Meta

ZUNJAE – [/u/zunjae](https://www.reddit.com/user/zunjae/) – zunjaeprivate@gmail.com

Distributed under the GNU license. See ``LICENSE`` for more information.

## Contributing

I don't accept pull requests considering Git(Hub) is unnecessary complex to understand. Instead, explain your changes line by line through Discord. Can be in public (for example, in the #tech channel) or by sending me a private message. Join [here](http://anymeapp.com/serverinvite)

## Motivation for making KanonApp open source

I plan on allowing users to host Kanon themselves. In the future, AnYme will have the option to setup your own backend so syncing should happen on _your_ server.
