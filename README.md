# MonoClass
MonoClass is an information aggregator designed to pull course, grade, and assignment information from a variety of grading platforms used by CU Boulder, specifically Canvas and Moodle. 


# Setup

## Initial Setup
On Debian based systems, run
```
sudo apt-get install python3-pip
```
to get pip3.

Followed by
```
sudo pip3 install virtualenv
```

Installing node.js can be found [here](https://github.com/nodesource/distributions/blob/master/README.md).
On Debian, the commands are as follows
```
curl -sL https://deb.nodesource.com/setup_13.x | bash -
apt-get install -y nodejs
```

This will prepare your system for the run.sh and setup.sh scripts that follow.

## Frontend
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Setup Customized Scripts
```
./setup.sh
```
### Running
```
./run.sh
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Backend
### Setup
```
./setup.sh
```
### Running
```
./run.sh
```
