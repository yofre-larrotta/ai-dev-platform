FROM node:18-alpine

ENV PORT=8080

WORKDIR /app

COPY package.json ./
# copy project-local npm configuration so npm uses it during install
COPY .npmrc ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]
