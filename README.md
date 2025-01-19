# Run Using...

uvicorn app:app --host 0.0.0.0 --port 8000 --reload


# Test Using...

curl -X 'POST' \
  'http://0.0.0.0:8000/process_data' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"data": "example input"}'


curl -X 'POST' \
  'http://0.0.0.0:8000/process_data_concurrent' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"items": ["item1", "item2", "item3"]}'


Or Open http://0.0.0.0:8000/docs on your Browser