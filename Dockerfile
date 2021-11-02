FROM python
RUN pip install kubernetes
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "driver.py"]
