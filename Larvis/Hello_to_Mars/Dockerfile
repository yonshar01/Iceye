FROM python
WORKDIR /myproject
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_DEBUG=True
CMD python hello_mars_api.py
