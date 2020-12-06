FROM python:3.8
WORKDIR /app
COPY . /app
CMD ["python", "-m", "unittest", "tests.test_loginvalidate", "&&", "python", "compare.py"]