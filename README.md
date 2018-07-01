# VoF Parser

# Developing

Make sure you have [pipenv](https://docs.pipenv.org/install/) installed. Clone the repository locally, and then run the following commands.

```
pipenv install
make run
```

You also need to have the [Google Cloud SDK](https://cloud.google.com/sdk/install) to get the `gcloud` command.

## Deploying


```
glcoud auth login
gcloud config set project vof-parser
make deploy
```

## Helpful `gcloud` commands


You can stream logs from the command line by running:

```
gcloud app logs tail
```

To view your application in the web browser run:

```
gcloud app browse -s vof-parser
```
