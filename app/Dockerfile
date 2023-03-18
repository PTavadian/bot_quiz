FROM python:latest


WORKDIR /app

RUN pip install aiogram==2.25.1

RUN pip install python-dotenv==1.0.0

RUN pip install openpyxl==3.1.1

RUN pip install SQLAlchemy==2.0.5.post1

RUN pip install emoji==2.2.0


COPY . .

CMD [ "python", "bot_telegram.py" ]







