FROM python:3.8

RUN python -m venv env
RUN echo "source /env/bin/activate " > ~/.bashrc
# RUN conda activate wordpineenv
# RUN echo "source activate wordpineenv" > ~/.bashrc
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
# COPY . .

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
