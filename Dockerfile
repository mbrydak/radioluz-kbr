FROM python:alpine

RUN python -m pip install beautifulsoup4 requests
WORKDIR /app
RUN mkdir -p /app/data/{data_raw,data_clean}

COPY *.py /app/

CMD ["python", "get_data.py"] 
