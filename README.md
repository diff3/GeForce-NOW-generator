# GeForce NOW generator

A simple Python script that generates a file with a list of owned games that can run on this glorious cloud platform.
It gets a JSON of games supported on GeForce NOW platform (via Nvidia's site) and a JSON of games on a provided user's Steam account to do its simple magic.

Blessed be the creator of **steamapi**, [smiley](https://github.com/smiley), for doing the backend work so I don't have to.

## Getting Started

Clone the project:

```
$ git clone https://github.com/Shushuda/GeForce-NOW-generator.git
```

Install requirements:

```
$ pip install -r requirements.txt
```

Create a valid **config.ini** file inside the repo dir (sample in Prerequisites) and run the script from the shell.

### Prerequisites

This project uses:

```
Python 3.7
```

as well as:

```
steamapi
```

Please update the **config.ini** file and add this information:

```
[STEAM]
ApiKey = <insert_your_key_here>
User = <inser_name>
```

The end user will also need to obtain a valid Steam API **key** to connect. It is simple and easy to do (domain name is a formality - just put '127.0.0.1' since there's no place like home).
Please refer to [official Steam API documentation](https://steamcommunity.com/dev) for more information.



## Authors

* **Weronika Sikora** - [Shushuda](https://github.com/Shushuda)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgements

* [smiley](https://github.com/smiley) for creating the steamapi library
* [PurpleBooth](https://gist.github.com/PurpleBooth) for creating this amazing README template
