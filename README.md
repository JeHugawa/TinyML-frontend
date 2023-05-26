# TinyML-frontend
frontend for the [TinyMLaaS](https://github.com/JeHugawa/TinyMLaaS-main).

## USB-detection

If running the frontend in a docker container, it is not possible to find newly added
usb devices inside the container. Because of this, be sure to connect required devices before starting
the frontend container

## Running

## Testing
For testing you need to have both the backend, frontend running and bridge.

Run Robot Framework tests with:
```
robot -d robot_output tests/
```

When Robot Framework tests are run, the environment variable _ROBOT_TESTS_ 
should be set to _true_. On bash, you can do that with
```
ROBOT_TESTS=true && export ROBOT_TESTS
```

This makes it that the robot tests don't access actual usb-devices, but rather
return set data.
