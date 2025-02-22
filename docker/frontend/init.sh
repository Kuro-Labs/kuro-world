#!/bin/sh

# Check if package.json exists
if [ ! -f package.json ]; then
    # Initialize Next.js project
    npx create-next-app@latest . \
        --typescript \
        --tailwind \
        --eslint \
        --no-git \
        --app \
        --src-dir \
        --import-alias "@/*" \
        --no-experimental-app \
        --yes
fi

# Start the development server
npm run dev
