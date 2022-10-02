FROM revolutiontech/zappa:1.1

COPY . .

RUN poetry install --no-dev

CMD ["poetry", "run", "zappa", "update"]
