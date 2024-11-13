# bootstrap the users environment with the necessary tools
set -e
# check if pipx is installed; install if not
if ! command -v pipx &> /dev/null
then
    echo "pipx not found; installing pipx"
    brew install pipx
    pipx ensurepath
else
    echo "pipx is already installed"
fi

# check if poetry is installed; install if not
if ! command -v poetry &> /dev/null
then
    echo "poetry not found; installing poetry"
    pipx install poetry
else
    echo "poetry is already installed"
fi

# install the poetry dependencies
poetry install  --with dev
# install the pre-commit hooks
poetry run pre-commit install
