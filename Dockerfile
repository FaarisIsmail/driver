FROM python
RUN pip install kubernetes
WORKDIR /app
COPY . /app
CMD ["python", "driver.py"]
