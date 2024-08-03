#############################################################
# AEYE Web Nextjs Dockerfile
# Created By Yoonchul Chung
# Created At 2024.08.03
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################
FROM node:18-alpine AS builder

WORKDIR /app/

#############################################################
# Dependencies
COPY /AEYE_Front/package.json ./

RUN npm install

COPY /AEYE_Front/ /app/

# 빌드 과정에서 NODE_ENV를 production으로 설정
ENV NODE_ENV=production

RUN npm run build

#############################################################
# Run
FROM node:18-alpine 

WORKDIR /app/

COPY --from=builder /app/.next /app/.next
COPY --from=builder /app/package.json /app/package.json
COPY --from=builder /app/node_modules /app/node_modules

COPY --from=builder /app /app
ENV NODE_ENV=production

RUN npm install --production

EXPOSE 80
ENV PORT 80
CMD ["npm", "start"]
