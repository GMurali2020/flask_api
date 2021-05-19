FROM python
COPY . /pandas/flaskapi
EXPOSE 5000
WORKDIR /pandas/flaskapi
RUN pip install -r requirements.txt
CMD python app.py