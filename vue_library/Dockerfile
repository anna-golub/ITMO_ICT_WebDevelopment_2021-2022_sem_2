FROM node:lts-alpine

WORKDIR /code/vue_library
COPY package*.json ./
COPY . /code

EXPOSE 8080

RUN npm install -g npm
RUN npm install -g @vue/cli

RUN npm install
