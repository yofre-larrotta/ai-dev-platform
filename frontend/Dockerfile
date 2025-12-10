FROM node:18-alpine

ENV PORT=8080

WORKDIR /app

COPY package.json ./
# Copy project-local npm configuration to handle SELF_SIGNED_CERT_IN_CHAIN errors in CI
# Note: This disables SSL verification temporarily. For production, add CA cert to trust store instead.
COPY .npmrc ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]
