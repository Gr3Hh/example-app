FROM python:3.9-alpine

# OS section
RUN apk --update upgrade && apk add --update --no-cache \
    curl libpq-dev python3-dev gcc bash musl-dev

# Poetry section
WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local' \
    PYTHONUNBUFFERED=1

ARG build_env=production

RUN curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version

COPY pyproject.toml poetry.lock .flake8 /app/

RUN poetry install $(if [[ $build_env = 'production' ]]; then echo '--only main'; fi) \
    --no-interaction --no-ansi --no-cache

COPY app .

# User section
ARG USERNAME=appuser
ARG USERGROUP=appgroup
ARG UID_GID=1000
RUN addgroup -g $UID_GID $USERGROUP \
    && adduser -D -u $UID_GID -G $USERGROUP $USERNAME

RUN chown -R $USERNAME:$USERGROUP /app

USER $USERNAME
