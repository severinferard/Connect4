# Connect4
Dual player Connect4 game oven LAN

## Description
The game features two game modes, local and multiplayer. In local mode, both player play on the same computer one after the other. In multiplayer mode, both player play on a different machine connected to the same network. In order to work, a server needs to be run on a machine connected to the network.
## Setup
Dowload or clone the repository. 
Run the following bash command to install all the packages needed. Those packages are listed in the requirements.txt file.

``` pip3 install -r requirements.txt ```
## Demo
#### Main menu
![Capture d’écran de 2019-07-12 14-07-43](https://user-images.githubusercontent.com/51379148/61144855-58209e00-a4d6-11e9-9be3-b3f1f8fbce4f.png)

#### Multiplayer game 
![Capture d’écran de 2019-07-12 14-06-47](https://user-images.githubusercontent.com/51379148/61144921-83a38880-a4d6-11e9-8de1-58e39df1df5c.png)

## Files architecture
```server.py``` contains the code needed to run the server. No multiplayer game can be played without a server running on the network
```network.py```contains a class called Network. A Network object is the created in the ```game.py``` to handle all the networking in multiplayer games.
```game.py``` contains a class called Game. It conatains all the methods used to run a local or multiplayer game.
```GUI.py``` contains two classes,  
```main.py``` finally initializes and runs the script. "graphic_client" and "MainMenu". The first one create an object responsible for handling all the graphics of a game. The second class create the main menu object.

## Packages used
### Graphics
* Pygame
* PygameMenu

### Modelisation
* Numpy

### Networking
* Socket
* thread
