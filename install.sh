# Install Dep.

sudo apt install -y python3-pip
sudo apt install -y build-essential
sudo apt install -y git
sudo apt install -y python3
sudo apt install -y python3-dev
sudo apt install -y ffmpeg
sudo apt install -y libsdl2-dev
sudo apt install -y libsdl2-image-dev
sudo apt install -y libsdl2-mixer-dev
sudo apt install -y libsdl2-ttf-dev
sudo apt install -y libportmidi-dev
sudo apt install -y libswscale-dev
sudo apt install -y libavformat-dev
sudo apt install -y libavcodec-dev
sudo apt install -y zlib1g-dev
sudo apt install -y autoconf
sudo apt install -y automake
sudo apt install -y libtool
sudo pip3 install --upgrade cython==0.21
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt install -y ccache
sudo apt install -y libncurses5:i386
sudo apt install -y libstdc++6:i386
sudo apt install -y libgtk2.0-0:i386 
sudo apt install -y libpangox-1.0-0:i386
sudo apt install -y libpangoxft-1.0-0:i386
sudo apt install -y libidn11:i386
sudo apt install -y openjdk-8-jdk
sudo apt install -y unzip
sudo apt install -y zlib1g-dev
sudo apt install -y zlib1g:i386

# Instalar gstreamer para audio, video (opcional)

sudo apt install -y libgstreamer1.0
sudo apt install -y gstreamer1.0-plugins-base
sudo apt install -y gstreamer1.0-plugins-good

# Atualizar ou Instalar buildozer

sudo pip3 install -U buildozer

# Instalando o kivy para o Python3 (Opcional)
# Isso é opcional porque você pode criar os apps na sua máquina real e criar os apks na VM

sudo add-apt-repository ppa:kivy-team/kivy
sudo apt update
sudo apt install -y python3-kivy
