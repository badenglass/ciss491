# ciss491 PDGA Statistics

## Message sent to Discord

Endpoint: `POST /predict`
Example URL when running locally: `http://localhost:8000/predict`

The requests expects: rating (float) and events_played (float or int)
Example request body:

```json
{
  "rating": 1000,
  "events_played": 20
}
```

Example curl request (replaced by PHP but nice for testing):

```sh
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"rating":1000,"events_played":20}'
```

You can also go the the following URL to test and make interactive requests: http://localhost:8000/docs

Here's an example response:

```json
{
  "rating": 1000,
  "events_played": 20,
  "predicted_points": 9110.57
}
```

## Start the API

`uvicorn model_api:app --reload --port 8000`
