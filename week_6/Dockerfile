# python version
FROM python:3.13

# working directory in the container
WORKDIR /app

#what i wanna copy in the img
COPY . /app

#requirements
RUN pip install --no-cache-dir -r requirements.txt

# port
EXPOSE 8000


# Run the app
CMD ["python", "/app/src/app.py"]

RUN pip install pytest