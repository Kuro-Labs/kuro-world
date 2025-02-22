FROM node:20-slim

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

EXPOSE 3000

# Add host to fix hot reload in docker
ENV NEXT_WEBPACK_USEPOLLING=1
ENV WATCHPACK_POLLING=true

CMD ["npm", "run", "dev"]
