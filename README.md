Reddit Emoji Frequency Analyzer - Project for Ling 508

To run (have a working installation of docker and docker-compose CLI):

```
docker compose up
```


### Configuring .env

Configure a .env file in the root directory with your Reddit API information:

```
CLIENT_ID=[CLIENT ID STRING]
CLIENT_SECRET=[CLIENT SECRET STRING]
USER_AGENT=[USER_AGENT STRING]
```

This information can be obtained by [creating a new reddit app at this link.](https://reddit.com/prefs/apps)

Create a new app, give it a memorable name, and set your redirect uri to http://localhost:5000.

Your **CLIENT_ID** is the bolded alphanumeric string underneath the name of your app.
Your **CLIENT_SECRET** will be following the field *secret*.
Your **USER_AGENT** will be in the field *name*.