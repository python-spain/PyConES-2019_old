# build stage
FROM node:lts-alpine as build-frontend-stage
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build

# python setup
FROM python:3 as build-backend-stage
ENV PYTHONUNBUFFERED 1
COPY backend/Pipfile* ./
RUN pip install --user pipenv
RUN pipenv install
COPY backend .


# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
