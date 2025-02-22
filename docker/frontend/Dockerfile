FROM node:20-slim

WORKDIR /app

# Copy initialization script
COPY docker/frontend/init.sh ./init.sh
RUN chmod +x ./init.sh

EXPOSE 3000

CMD ["/app/init.sh"]
