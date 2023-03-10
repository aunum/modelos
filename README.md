# ![logo](./static/L_blue.svg)
An operating system for machine learning

## Installation
```
pip install modelos
```
### Configuring

ModelOS requires and OCI compliant image registry. This can be set using any of:

* `$MDL_IMAGE_REPO` env var
* `tool.modelos.image_repo` in `pyproject.toml`
* `image_repo` in `mdl.yaml` file at project root
* `image_repo` function parameters

ModelOS requires a Kubernetes cluster >= 1.22.0 and will use your current kubeconfig context.

## Usage

> **_NOTE:_**  ModelOS is pre-alpha and under heavy development, expect breakage

### Objects

Objects are distributed persistent Python objects.

A sample object
```python
from modelos import Object

class Ham(Object):

    temp: int
    weight: int
    brand: str

    def __init__(self, weight: int, brand: str) -> None:
        self.weight = weight
        self.brand = brand

    def bake(self, temp: int) -> None:
        self.temp = temp

    def cut(self, weight: int) -> int:
        self.weight = self.weight - weight
        return self.weight

```

ModelOS objects work just like Python objects with some extra capabilities.

### Developing Objects
Develop on the object remotely
```python
# Create a client which can be used to generate remote instances
HamClient = Ham.client(hot=True)

# Creates a remote instance within the context then deletes it
with HamClient(weight=12, brand="black forest") as ham:
    ham.bake(temp=340)

    # Store the object
    uri = ham.store()
```
Example develop URI: `acme.org/ml-project:obj.ham.f2oij-2oijr-f8g2n`


### Releasing Objects
Release the object to be used by others. This creates a semver for the object and client/server packages
```python
HamClient = Ham.client()

# Creates a remote instance within the context then deletes it
with HamClient(weight=14, brand="honey baked") as ham:
    ham.bake(temp=340)

    uri = ham.release()
```
Example release URI: `acme.org/ml-project:obj.ham.v1.2.3`   

#### Versioning scheme

__v1__: interface version   
__v1.2__: class version   
__v1.2.3__: instance version   


### Using Objects
Install a client from a release and use it to generate a remote instance
```python
from modelos import install

install("acme.org/ml-project:obj.ham.v1")

from ml_project.ham.v1 import HamClient

# Use the latest release
with HamClient(weight=10) as ham:
    ham.bake(temp=320)

# Specify a class release version
HamClient.version = "v1.2"

with HamClient(weight=10) as ham:
    ham.bake(temp=320)

# Specify an instance version
with HamClient.instance("v1.2.3") as ham:
    ham.bake(temp=320)
```

Install a class and use locally or remotely
```python
from modelos import install

install("acme.org/ml-project:obj.ham.v1.2")

from ml_project.ham.v1_2 import Ham

# locally
ham = Ham(weight=12)
ham.bake(temp=300)

# remotely
with Ham.client()(weight=10) as ham:
    ham.bake(temp=320)
```

Install an instance and use it locally
```python
from modelos import install

install("acme.org/ml-project:obj.ham.v1.2.3")

from ml_project.ham.v1_2_3 import Ham

# load the object instance state
ham = Ham.from_env()

ham.bake(temp=400)
```

An example working project can be found at https://github.com/pbarker/kvd

## Packages
Packages are versioned filesystems

```python
from modelos.pkg import Pkg, clean

# Create a new package from the ./data dir
pkg = Pkg("foo", "./data", "A foo package", remote="acme.org/ml-project")

# See package contents
pkg.show()

# Push the package to its remote
pkg.push()

# List files in the package
files = pkg.ls()

# Open a file in the package
with pkg.open("./foo.yaml") as f:
    b = f.read()

# Release the package
pkg.release("v0.0.1", labels={"type": "foo"}, tags=["baz"])

# Check the latest package is our release
assert pkg.latest() == "v0.0.1"

# Delete the package
pkg.delete()

# Describe a remote package
info = Pkg.describe("acme.org/ml-project:pkg.fs.bar.v1.2.3")

# Use a remote package
bar_pkg = Pkg("bar", version="v1.2.3", remote="acme.org/ml-project")

# Clean packages
clean("acme.org/ml-project", "foo")
```

See the [tests](./tests/pkg/pkg_test.py) for more examples

## Roadmap

- [ ] Releasing
- [ ] Properties
- [ ] Packages
- [ ] Environments
- [ ] Runtimes
- [ ] Extension objects
- [ ] Finding / indexing
- [ ] Docs / landing
- [ ] UI / CLI
- [ ] Schema
- [ ] Bi-directional streaming
- [ ] Smarter versioning
