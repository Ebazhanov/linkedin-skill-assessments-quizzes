## Microsoft Azure Assessment

Q1. You need to create an application in Azure AD representing the Kinetico Web App so you can assign directory permissions to the app. To create the application identity, which command will you run?

    az ad app permission grant -display-name $appName \ ...
    az ad app credential create -display-name $appName \ ...
    az ad app create -display-name $appName \ ...			<<<< CORRECT
    az ad app permission ass -display-name $appName \ ...

Q2. You need to deliver a mobile push notification for the Kinetico Retail app, hosted in Azure App service. The solution should minimize cost, complexity and development effort. Which option should you choose?

    Notification Hub 		<<<<< CORRECT
    Event Hub
    Twilio
    Service Bus

Q3. Your application hosted in Azure App services needs to retrieve secrets from Azure Key vault. Which choice is NOT a way to authenticate to Key vault?

    service principle and certificate
    managed identity
    service principle and a secret
    shared access key		<<<<< CORRECT

Q4. You added a persistent volume claim to your apps YAML manifest. When you attempt to deploy to an existing AKS cluster there is no persistent volume available. What should you do?

    Do nothing. The API server will provision additional storage automatically
    Add a data disk definition for the AKS cluste to your apps YAML manifest		<<<< MAYBE THIS ONE
    Add a data disk to each Kubernetes cluster node and reattempt app deployment
    Provision an Azure Files instance and reattempt app deployment

Q5. Your corporate web application is hosted in Azure regional data centres aroung the world. You need to route user requests to the closest service endpoint based on response latency. Which routing method should you use?

    Application gateway
    Front Door
    API Management
    Traffic manager		<<<< CORRECT

Q6. You are developing a release strategy for several related software components. You need to reference variable groups and secure files across multiple build and release pipelines. What is the most efficient way to store and reference these assets from the pipeline?

    Add the assets to a git repository
    Add the assets in Key Vault		<<<<<SHOULD BE THIS ONE
    Add the assets to an encrypted volume
    Add the assets to a library 		<<<< COULD BE THIS ONE TOO

Q7. You need to grant full access for an app to a temporary Azure storage account. Configuring access should require minimum effort. Which option should you use?

    Azure AD user account		<<<< CORRECT
    Shared access signature
    Shared key
    Certificate

Q8. The Kinetico web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

    Configure application insights cohort
    Install the Log Analytics agent and configure Azure Monitor for Containers	<<<<< CORRECT
    Install the App Insights on AKS nodes
    Add instrumentation to your app to send usage analytics with Application Insights.

Q9. Which choice is not a valid trigger for an Azure functions?

    based on a time (schedule)
    another Azure service (cosmos, service bus)
    threshold alert in Azure App insights
    third party services		<<<<<< CORRECT

Q10. Which messaging service enables an even-driven programming model?

    Service Bus
    Event Hub
    Notification Hub
    Event Grid		<<<<<< CORRECT

Q11. You need to populate a newly created SQL database from your release pipeline in Azure DevOps. The solution should minimise deployment time and efforts. Which approach should you use?

    Populate from BACPAC file		<<<< CORRECT
    Restore from backup file
    populate from csv file
    Populate from SQL file

Q12. You need to host a community website for you neighbourhood association. The site contains static content, HTML CSS, and a few pages with client-side JS. Which option should you use?

    Azure storage static website		<<<< CORRECT
    static website with Azure CDN
    App service on consumption plan
    App service on standard plan


Q13. Your organisation delivers a number of RESTful web services to customers around the world. You need to deploy cloud infrastructure to deliver these services to paying customers, including authentication, request throttling and routing of requests to the closest service endpoint. Which solution should you choose?

    Front door
    API Management
    Traffic manager
    Application Gateway <<<< CORRECT

Q14. You have .NET app running CM scale set. You need to monitor application performance without modyfying the code. The solution should minimise the cost. What should you do?

    Enable network performance monitor on the VMs
    install the Log Analytics Agent and enable Azure Monitor for VMs
    Install Application Insights Agent		<<< CORRECT
    Enable SolarWinds Performance Monitor from the Azure Marketplace

Q15. When setting your CI/CD pipeline an approval from your product owner is required before a final release to production. What solution do you use to achieve this?

    Manual intervention task
    pre-deployment condition	<<< SHOULD BE THIS
    branch filer
    pre-deployment gate		<<< MAYBE THIS?
