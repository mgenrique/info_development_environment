
Se puede hacer igualmente desarrollo sin usar Dev Containers trabajando directamente con Python
En este caso para configurar el entorno haremos:

````bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev python3-venv autoconf libssl-dev libxml2-dev libxslt1-dev libjpeg-dev libffi-dev libudev-dev zlib1g-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev ffmpeg libgammu-dev
````

Visit the Home Assistant Core repository at https://github.com/home-assistant/core

and click Fork. Once forked, setup your local copy of the source using the commands:

````bash
git clone https://github.com/YOUR_GIT_USERNAME/short_name_of_your_fork
cd core
git remote add upstream https://github.com/home-assistant/core.git
script/setup
source venv/bin/activate
hass -c config
````
