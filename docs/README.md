# Earthshot documentation

This file gives a quick overview on compiling Earthshot documentation.

## Environment

Make sure that your current environment has all the requirements for the earthshot package itself. Additionally, you need to install Sphinx along with plugins:


```
pip install -r requirements.txt
```

## Compile

Documentation can be compiled with the following command:

```
make html
```

The output will be generated inside the `_build/html` directory.
