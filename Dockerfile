# BASE IMAGE TO START WITH
FROM python
# mkdir /app && cd /app
WORKDIR /app 
# SOURCE DEST
COPY req.txt  .   
# INSTALL REQUIREMENTS
RUN pip install -r req.txt
# COPY THE CODE FROM MY LOCAL FOLDER TO THE IMAGE
COPY . .
# RUN  THE DJANGO APP
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
