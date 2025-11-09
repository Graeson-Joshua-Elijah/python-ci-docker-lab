# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# default command shows example run (overridden by docker run or CI)
CMD ["python", "app.py", "--a", "2", "--b", "3"]
