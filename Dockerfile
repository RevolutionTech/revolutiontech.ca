FROM revolutiontech/zappa:1.1

COPY . .

RUN poetry install --only main

CMD ["poetry", "run", "zappa", "update"]
