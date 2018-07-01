# VoF Parser

# Developing

Make sure you have [pipenv](https://docs.pipenv.org/install/) installed. Clone the repository locally, and then run the following commands.

```
pipenv install
make run
```

You also need to have the [Google Cloud SDK](https://cloud.google.com/sdk/install) to get the `gcloud` command.

## Deploying

Make sure you've done the below commands to login to your Google Account and set your project.

```
glcoud auth login
gcloud config set project vof-parser
```

### Staging

When you want to deploy to a staging environment run the following command. This is useful when you want to try some changes but do not want the DNS entries to point to your new version. You can see the staging environment by going [here](https://staging-dot-vof-parser.appspot.com)

```
make deploy-staging
```

When you're done testing staging then run `make stop-staging` to turn it off.

### Production

When you're ready to deploy to production then run the following command.

```
make deploy-prod
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
