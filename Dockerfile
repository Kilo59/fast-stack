FROM python:3.12
WORKDIR /app/

# Disable in-memory buffering of application logs
#   https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1
ENV POETRY_CACHE_DIR=/tmp/pypoetry

RUN pip --no-cache-dir install poetry==1.8.4

COPY pyproject.toml poetry.lock ./

# Recommended approach for caching build layers with poetry
#   --no-root: skips project source, --no-directory: skips local dependencies
#   https://python-poetry.org/docs/faq
RUN poetry install --without dev --no-root --no-directory

COPY /fast_stack /app/fast_stack
COPY /tasks.py /app/tasks.py

EXPOSE 80

ENTRYPOINT ["poetry", "run", "fastapi", "run", "fast_stack/app.py", "--port", "80"]
