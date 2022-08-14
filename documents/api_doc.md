# Reddit Emoji Frequencies

## Getting emoji counts

The endpoint located at "/emoji" provides the user with a dictionary where keys are emoji, and the associated values are the counts of those emoji for the given subreddit within the given time range. 

The service can be accessed without a UI using a POST request. The JSON body of the request must contain the following fields:

The required fields are the following:
- subreddit : string (The subreddit to search)
- after : string (The start date for the time range to search, formatted YYYY-MM-DD)
- before : string (The end date for the time range to search, formatted YYYY-MM-DD)

An optional field can be:
- limit : string/int (the number of requests to make using Pushshift / Reddit API)

Here is an example request body with all the possible fields:

```JSON
{
  "subreddit": "tokipona",
  "after": "2022-07-01",
  "before": "2022-07-29",
  "limit": "100"
}
```

Here is a complete CURL command for to acheive the same request:
```
curl -X 'POST' 'http://0.0.0.0:5000/emoji' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"subreddit":"tokipona", "after":"2022-07-01","before":"2022-07-29", "limit":100}'
```

The response will come back formatted as such:

```JSON
{
  "🇫🇷": 1,
  "😉": 1,
  "🤔": 1,
  "🥖": 1
}
```
