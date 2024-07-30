FROM node:18-alpine AS aeye_web_front

WORKDIR /app
COPY ./AEYE_Front/* /app/


FROM aeye_web_front AS deps

COPY package*.json ./

RUN npm install


FROM deps AS build

RUN npm run build
COPY --from=builder /app ./
RUN npm install --production

FROM build AS runner

EXPOSE 3000

CMD ["npm", "start"]
