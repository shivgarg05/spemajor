# pull official base image
FROM node:18-buster-slim as builder

# set work directory
WORKDIR /ui

# install dependencies and avoid `node-gyp rebuild` errors
RUN apt-get update && apt-get install -y \
        python \
        make \
        g++ \
    && rm -rf /var/lib/apt/lists/*

# copy package.json and package-lock.json files
COPY ./package*.json ./

# install dependencies
RUN npm install --legacy-peer-deps

# copy our react project
COPY ./ .

# perform npm build
# ARG API_SERVER
# ENV REACT_APP_API_SERVER=${API_SERVER}
RUN npm run build

#########
# FINAL #
#########

# pull official base image
FROM node:18-buster-slim

# set work directory
WORKDIR /ui

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve

# copy our build files from our builder stage
COPY --from=builder /ui/build  ./build
