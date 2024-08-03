send()
{
  curl -X POST http://127.0.0.1:6000/api/data/front/ \
     -F "name=YourName" \
     -F "date=2024-08-01" \
     -F "image=@./image.png"
}

send
