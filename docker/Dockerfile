FROM python:3.9-slim


ENV POETRY_HOME="/home/poetry"
ENV VENV_PATH="/home/api/.venv"
ENV USER="api"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


RUN useradd $USER && \
  apt-get update && \
  apt-get install -y git build-essential locales ffmpeg curl postgresql-client iputils-ping net-tools dos2unix && \
  pip3 install --upgrade pip && \
  pip3 install poetry


WORKDIR /home/$USER


RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  locale


COPY --chown=$USER:$USER ./pyproject.toml ./
COPY --chown=$USER:$USER ./src/ ./src/
COPY --chown=$USER:$USER ./.env ./.env
COPY --chown=$USER:$USER ./run.py ./run.py
COPY --chown=$USER:$USER ./boot.sh ./boot.sh

RUN dos2unix boot.sh && \
    chmod +x boot.sh && \
    poetry config virtualenvs.create false && \
    poetry lock && \
    poetry install --no-root


USER $USER


ENTRYPOINT ["./boot.sh"]
