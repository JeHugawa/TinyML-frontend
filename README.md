# TinyML-frontend
frontend for the [TinyMLaaS](https://github.com/JeHugawa/TinyMLaaS-main).

## USB-detection

If running the frontend in a docker container, it is not possible to find newly added
usb devices inside the container. Because of this, be sure to connect required devices before starting
the frontend container

## Running

## Testing
For testing you need to have both the backend and frontend running. 

Run Robot Framework tests with:
```
robot -d robot_output tests/
```
