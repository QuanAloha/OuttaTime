FROM node:current-alpine

WORKDIR /workspace/frontend

# Install git (and bash for better shell experience)
RUN apk add --no-cache git bash

# (Optional) Install GitHub CLI for advanced GitHub workflows
RUN apk add --no-cache curl && \
    curl -fsSL https://github.com/cli/cli/releases/download/v2.44.0/gh_2.44.0_linux_amd64.tar.gz | tar -xz && \
    mv gh_2.44.0_linux_amd64/bin/gh /usr/local/bin/gh && \
    rm -rf gh_2.44.0_linux_amd64

COPY package.json package-lock.json* ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "run", "dev"]
