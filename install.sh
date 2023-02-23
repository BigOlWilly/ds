sudo apt-get update -y
sudo apt install python3-pip -y

git clone https://github.com/MatrixTM/MHDDoS

cd MHDDoS

sudo pip3 install -r requirements.txt

cd ..

sudo python3 main.py
