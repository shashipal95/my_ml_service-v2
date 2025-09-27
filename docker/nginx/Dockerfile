# Use a modern Nginx Alpine image
FROM nginx:stable-alpine

# Copy your custom Nginx configuration (adjust path if needed)
COPY ./nginx.conf /etc/nginx/nginx.conf

# Copy static files to serve (adjust paths to match your project)
COPY ./backend/server/static /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
