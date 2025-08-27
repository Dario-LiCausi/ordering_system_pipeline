# python version
FROM python:3.13

# working directory in the container
WORKDIR /app

COPY . /app

#requirements
RUN pip install --no-cache-dir -r requirements.txt

# port
EXPOSE 8000

# ENTRYPOINT 

# Run the app
CMD ["python", "/app/src/app.py"]
# CMD ["python", "app.py"]