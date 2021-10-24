# syntax=docker/dockerfile:1
FROM node:12-alpine
RUN apk add --no-cache python g++ make
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["node", "src/index.js"]