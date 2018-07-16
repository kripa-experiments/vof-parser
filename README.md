# VoF Parser

Understand the Voice of the Fan at at <https://vof.metonymize.co> or <https://metonymize.co>.

# Developing

Make sure you have [pipenv](https://docs.pipenv.org/install/) installed. Clone the repository locally, and then run the following commands.

```
pipenv install --ignore-pipfile
make run
```

You also need to have the [Google Cloud SDK](https://cloud.google.com/sdk/install) to get the `gcloud` command.

## Deploying

First part of this has instructions about initializing with Google
Cloud. Other steps are about deploying to various targets.

### First time

If this is your first time with this project, then use the below
command to trigger the initialization flow. Login to your
@metolabs.com account and set your project to vof-parser. Call your
local configuration vof.

```
gcloud init
```

### Any time but first

If you've already setup a local configuration, then use the following
command to set it when you start working on this project.


```
gcloud config configurations vof
```

### Staging

When you want to deploy to a staging environment run the following
command. This is useful when you want to try some changes but do not
want the DNS entries to point to your new version. You can see the
staging environment by going
[here](https://staging-dot-vof-parser.appspot.com)

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

If you want to see the configuration for a deployed app then something like below gives it to you. This can be useful to confirm changes were made when deploying. It can also let you see how autoscaling is configured.

```
gcloud app versions list
# Pick out a version that is getting traffic
gcloud app versions describe -s default VERSION_FROM_ABOVE
```
