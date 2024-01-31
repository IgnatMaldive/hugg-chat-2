demo: https://flask-htmx-search.vercel.app/

# HTMX + Flask + Search

Sample search Panel using minimal HTMX/Flask stack, hosted in Vercel.
This example uses Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-vercel-serverless-functions.vercel.app/

## How it Works

This example uses the Tavily Search and Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
git clone this repo
cd api
python index.py
```

Your Flask application is now available at `http://localhost:5000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

