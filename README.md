# azure_flask_deployment
504 Week 2 Assignment, deploying basic flask application using Microsoft Azure App Services

## Flask Application

1. Create app.py file, importing flask and pandas. Place these packages in a requirements.txt file
2. Define your app and create a home route (in this assignment, calling the data within the route)
3. Format the route page using an html file placed in the templates folder. Create headers to describe the page and a table to store defined rows from the loaded dataset. 
4. Return this html template in your app route using render_template
5. Run the app locally in your terminal using 'python app.py'

## Azure Deployment

1. Install Azure CLI into your IDE 
2. Login into Azure using az login --use-device-code
3. Create a resource group inside of your Azure account which will be used to create the Web App
4. Create the web app using az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>, replacing bracketed terms with the corresponding resource group, app name, python version, and sku 

