# Acid Lab DevOps Challenge

# ML Model Exposed as REST API

## Project Structure

In this project you will find the following file structure:
  - [.github/workflows/](.github/workflows/): Github Actions Workflow pipelines
    - *[ main.yaml -> for the app implementation proccess ]*
    - *[ infrastructure_pipeline.yaml -> only for the infrastructure implementation, in this case Heroku ]*
  - [app/](app/): Directory with all the files neccesary to build the REST API app. Python app and ML model can be found here.
  - [datasets/](datasets/): Group of dataset to train and test the model in use.
  - [infrastructure/](infrastructure/): Terraform files to handle the Heroku app implementation.
  - [.gitignore](.gitignore): Git .gitignore to exclude not needed temporal files.
  - [Dockerfile](Dockerfile): Dockerfile needed to build the app image to deploy to Heroku app.
  - [model.ipynb](model.ipynb): Model Jupyter Notebook

## How to Test this Project

This project was develop to use GitHub Actions as CI/CD tool and Heroku as infrastructure cloud. You will need to create account for each of this platform in order to test the entire process.

### Before deploying the app lets create the infrastructure with Terraform !!!

We have to firt create the app in Heroku so we can get the name of the app and add a secret variable into GitHub secret so our GitHub Actions pipeline will deploy everything to this Heroku app instance. This app will be reach through the domain **https://<app-name>.herokuapp.com/**.

To create the app we will do it from out local machine since we are using local state files to handle the resources status in Terraform.
  
  1. Clone this repository to your local. Run `git clone https://github.com/jossteeven/acid-labs-devops-challenge.git`.
  2. Get inside the infrastructure folder. Run `cd acid-labs-devops-challenge/infrastructure`.
  3. Make sure you have Terraform installed in you local machine. If not, ue this reference to install it: [Install Terraform Here !](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
  4. Export the variable TF_VAR_HEROKU_API_KEY with you HEROKU api key. You can find it at your **Account Setting/Api Key** section. Run `export TF_VAR_HEROKU_API_KEY=<your-api-key>`.
  
  This variables is sentivite and that is why we use it as an environment variable an must not be fixed at the project code. You can add it too at the Setting/Secrets/Actions section of you projects to test the *insfrastrucutre_pipeline.yaml* file and still have it secure without exposing it.
  5. Execute `terraform init`
  6. You can run Execute `terraform plan` to see the resources that you are about to create before creating them.
  7. Execute Execute `terraform apply` to create the resources.
  8. Check you Heroku Dashboard, your app called **acid-lab-challenge** should be already created.

 We will need the app name stored in a secret so we will have to used this variable to let the pipeline know where to deploy our code. Save the name of you app, in the next steps you will know waht to do.
  
### Let´s go to the code !!!

1. Fork the project.
2. Add the following secrets into the Setting/Secrets/Actions section of your new project:
   - HEROKU_API_KEY: Add your Heroku API key. You can find it at **Account Setting/Api Key** on the right upper corner.
   - HEROKU_APP_NAME: Add the app anme of the heroku_app resource in the main.tf file. You can change it as you want. acid-lab-challenge is the default value. This i the app name of the Heroku app iinstance you already deployed in the passed section. Add here the name we told you to save.
   - HEROKU_EMAIL: Add you email associated with the Heroku app.
   - TF_VAR_HEROKU_API_KEY: Terraform variable.
   - DOCKER_PASSWORD: Your DockerHub password.
   - DOCKER_USERNAME: Your DockerHub username. You can find it at the profile section or at the top right corner.
3. You are ready to run the master pipeline. Follow this reference [Manually Run a Pipeline](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)
