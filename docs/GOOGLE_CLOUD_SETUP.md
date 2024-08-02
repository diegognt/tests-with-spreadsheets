# Google Cloud set up

This guide walks you through setting up Google Cloud for interacting with Google Sheets. 

## A Google Cloud Project
In case that you do not have a Google Cloud Project available, follow the next steps. In case you already have one, please skip this section.

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the "Create Project" button.
3. Give your project a unique name and select a location.
4. Click "Create".

## Enable the Google Sheet API.

1. In the Google Cloud Console, navigate to the API & Services section.
2. Select "Library".
3. Search for "Google Sheets API" and enable it.

## Create a Service Account

1. In the Google Cloud Console, navigate to the "IAM & Admin" section.
2. Select "Service accounts".
3. Click "Create Service Account".
4. Give your service account a name and description.
5. Under "Role", select "Project > Editor" (or a more restrictive role if needed).
6. Click "Create".

## Setup the Google Cloud SDK & CLI in a local machine:

Visit the [official documentation](https://cloud.google.com/sdk/docs/install) for detailed instructions then, download the appropriate installer for your system.

> **Note:** If you have not initialize the gcloud CLI, open a terminal or command prompt, then run the command `gcloud init`

#### To set a GCP Project as default,
1. Check the available project, `gcloud projects list`, The command will display a list of projects you have access to. Identify the project you want to set as default.
2. Set a project as default, `gcloud config set project YOUR_PROJECT_ID`
3. Verify, run `gcloud config list`, this will show the current configuration, including the default project.

## Obtaining a Service Account Key

Once you have a service account, you can use the gcloud CLI to create a key for it,

```sh
gcloud iam service-accounts keys create ./secret.json --iam-account <service_account_email>
``` 
