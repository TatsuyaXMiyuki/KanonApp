# KanonApp
> Companion server for the AnYme App


KanonApp is a server which adds extra functionality which is otherwise not possible with just MyAnimeList and AnYme.

The features are:

* Add notes to episodes you have watched
* Save unlimited waifus to your profile
* Save your favorite songs

Obviously more will come soon, however this is just a start

The data will be kept in sync on the KanonApp server which means it is available on all your devices.

# How do I use KanonApp?

visit https://kanonapp.com/login on your phone. You can check in the source code how the login process works.

## Installation

Linux:

```sh
git clone https://github.com/zunjae/KanonApp.git
cd source code
bash setup.sh
```

## Development setup

The source code is just the server. You still need some data. There are plenty of ways to get them yourself. I use https://github.com/manami-project/anime-offline-database (licensed under GNU Affero General Public License v3.0)

In order to run KanonApp you need to following dependencies:

* Python
    * sqlite3, flask, flask limiter, 
* Apache2 if you want to run it on a production server

## Roadmap

* Controllers/Repository/Decorators should be in separate classes

## Vision

* The server should never use an ORM mapper, because that adds unnecessary complexity to the project

* The Zdb class is responsible for saving or retrieving data
* The server should be hosted on a server running Apache 2 due to its lower complexity
* Rate limits should be strict

## Meta

ZUNJAE – [/u/zunjae](https://www.reddit.com/user/zunjae/) – zunjaeprivate@gmail.com

Distributed under the GNU license. See ``LICENSE`` for more information.

## Contributing

I don't accept pull requests considering Git(Hub) is unnecessary complex to understand. Instead, explain your changes line by line through Discord. Can be in public (for example, in the #tech channel) or by sending me a private message. Join [here](http://anymeapp.com/serverinvite)

## Motivation for making KanonApp open source

I don't fully understand Python nor hosting a server. By making KanonApp open source I am able to get feedback and fix issues early.
