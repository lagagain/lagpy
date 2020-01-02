#! /bin/bash

bash_path=$(dirname $0)
PYTONPATH=$bash_path


python3 -m lagpy.functools.Callable -v
python3 -m lagpy.functools.Environment v
python3 -m lagpy.function.common -v
python3 -m unittest -v tests
