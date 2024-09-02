FROM python:3.9.6
ENV TOKEN='type_your_telegram_bot_token_here'
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]
EXPOSE 80