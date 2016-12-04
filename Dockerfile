FROM python:3
RUN mkdir /wpa/
ADD /wpa /wpa/
WORKDIR /wpa/
RUN pip install -r requirements.txt
CMD ["python","wpa.py"]
