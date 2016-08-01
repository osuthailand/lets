## LETS
## Latest Essential Tatoe Server
This server handles every non real time client feature, so:
- Ingame scoreboards
- Score submission
- PP calculation through `oppai` (std) and `wifipiano2` (mania)
- Screenshots
- Replays
- osu!direct
- Tillerino-like API

## Requirements
- Python 3.5
- MySQLdb (`mysqlclient` or `mysql-python`)
- Tornado (`tornado`)
- Bcrypt (`bcrypt`)
- Progressbar2 (`progressbar2`), only for `tomejerry.py`  
- oppai

## How to set up LETS
First of all, install all the dependencies
```
$ pip install mysqlclient tornado bcrypt progressbar2
```
then, run LETS once to create the default config file and edit it
```
$ python3 lets.py
$ nano config.ini
```
finally, configure oppai as described below.

## How to set up oppai with LETS
LETS uses lolisamurai's oppai as pp calculator for std. We use a slightly modified version of oppai, you can find it [here](https://github.com/osuripple/oppai).  
Go one directory above LETS (in the same directory where you have old-frontend, pep.py, lets and so on) and clone `oppai` inside the `oppai` folder, compile it with `make` and create the `maps` folder:
```
path/to/ripple$ git clone https://github.com/osuripple/oppai.git
path/to/ripple$ cd oppai
path/to/ripple/oppai$ make
path/to/ripple/oppai$ mkdir maps
```
*Note: `wifipiano` (mania pp calculator) is tailor-made for LETS and doesn't require any configuration.*

## tomejerry.py
`tomejerry.py` is a tool that allows you to calculate pp for specific scores. It's extremely useful to do mass PP recalculations if you fuck something up. It uses lets' config and packages, so make sure lets is installed and configured correctly before using it.  
`tomejerry` supports a lot of parameters, the main ones are:  
- `-r`, to recalculate PP for every score on every game mode (only std and mania are supported at the moment)    
- `-z` to calculate PP for scores with 0 pp  
- `-g x` to recalculate PP for scores for `x` gamemode (0: std, 3: mania)  
- `-i x` to recalculate PP for score with `x` id  
- `-n x` to recalculate PP for scores submitted by user with `x` username  
For a full list of all the arguments supported by `tomejerry`, run `python3 tomejerry.py --help`

## License
This project is licensed under the GNU AGPL 3 License.  
See the "LICENSE" file for more information.  
This project contains code taken by reference from [osu-performance](https://github.com/ppy/osu-performance) by Tom94.
