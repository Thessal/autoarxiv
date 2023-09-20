FROM python:3.8
WORKDIR /app
COPY . /app
RUN mkdir /app/input
RUN pip install -r requirements.txt
EXPOSE 3000
# Run app.py when the container launches
# CMD ["python", "app.py"]
CMD ["python","-u","app.py"]
