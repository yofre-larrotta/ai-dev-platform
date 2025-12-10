FROM node:18-alpine

ENV PORT=8080
ENV NODE_ENV=development

WORKDIR /app

# Copy package files
COPY package.json package*.json ./

# Install dependencies
RUN npm install

# Copy application files
COPY . .

# Expose the port
EXPOSE 8080

# Start the application
CMD ["npm", "start"]
