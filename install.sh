sudo apt-get update
sudo apt install python-pip3

git clone https://github.com/MatrixTM/MHDDoS

cd MHDDoS

sudo pip3 install -r requirements.txt

cd ..

sudo python3 main.py
