FROM python:3.11.0
WORKDIR /app
COPY . /app
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "keep_alive_website.py"]
