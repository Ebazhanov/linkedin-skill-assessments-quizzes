## Microsoft Azure Assessment

Q1. You need to create an application in Azure AD representing the Kinetico Web App so you can assign directory permissions to the app. To create the application identity, which command will you run?

- [ ] `bash az ad app permission grant -display-name $appName \ ...`
- [ ] `bash az ad app credential create -display-name $appName \ ...`
- [x] `bash az ad app create -display-name $appName \ ...`
- [ ] `bash az ad app permission ass -display-name $appName \ ...`

Q2. You need to deliver a mobile push notification for the Kinetico Retail app, hosted in Azure App service. The solution should minimize cost, complexity and development effort. Which option should you choose?

- [x] Notification Hub
- [ ] Event Hub
- [ ] Twilio
- [ ] Service Bus

Q3. Your application hosted in Azure App services needs to retrieve secrets from Azure Key vault. Which choice is NOT a way to authenticate to Key vault?

- [ ] service principle and certificate
- [ ] managed identity
- [ ] service principle and a secret
- [x] shared access key

Q4. You added a persistent volume claim to your apps YAML manifest. When you attempt to deploy to an existing AKS cluster there is no persistent volume available. What should you do?

- [ ] Do nothing. The API server will provision additional storage automatically
- [x] Add a data disk definition for the AKS cluste to your apps YAML manifest
- [ ] Add a data disk to each Kubernetes cluster node and reattempt app deployment
- [ ] Provision an Azure Files instance and reattempt app deployment

Q5. Your corporate web application is hosted in Azure regional data centres aroung the world. You need to route user requests to the closest service endpoint based on response latency. Which routing method should you use?

- [ ] Application gateway
- [ ] Front Door
- [ ] API Management
- [x] Traffic manager

Q6. You are developing a release strategy for several related software components. You need to reference variable groups and secure files across multiple build and release pipelines. What is the most efficient way to store and reference these assets from the pipeline?

- [ ] Add the assets to a git repository
- [x] Add the assets in Key Vault <<<<<SHOULD BE THIS ONE
- [ ] Add the assets to an encrypted volume
- [ ] Add the assets to a library <<<< COULD BE THIS ONE TOO

Q7. You need to grant full access for an app to a temporary Azure storage account. Configuring access should require minimum effort. Which option should you use?

- [x] Azure AD user account
- [ ] Shared access signature
- [ ] Shared key
- [ ] Certificate

Q8. The Kinetico web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

- [ ] Configure application insights cohort
- [x] Install the Log Analytics agent and configure Azure Monitor for Containers
- [ ] Install the App Insights on AKS nodes
- [ ] Add instrumentation to your app to send usage analytics with Application Insights.

Q9. Which choice is not a valid trigger for an Azure functions?

- [ ] based on a time (schedule)
- [ ] another Azure service (cosmos, service bus)
- [ ] threshold alert in Azure App insights
- [x] third party services

Q10. Which messaging service enables an even-driven programming model?

- [ ] Service Bus
- [ ] Event Hub
- [ ] Notification Hub
- [x] Event Grid

Q11. You need to populate a newly created SQL database from your release pipeline in Azure DevOps. The solution should minimise deployment time and efforts. Which approach should you use?

- [x] Populate from BACPAC file
- [ ] Restore from backup file
- [ ] populate from csv file
- [ ] Populate from SQL file

Q12. You need to host a community website for you neighbourhood association. The site contains static content, HTML CSS, and a few pages with client-side JS. Which option should you use?

- [x] Azure storage static website
- [ ] static website with Azure CDN
- [ ] App service on consumption plan
- [ ] App service on standard plan

Q13. Your organisation delivers a number of RESTful web services to customers around the world. You need to deploy cloud infrastructure to deliver these services to paying customers, including authentication, request throttling and routing of requests to the closest service endpoint. Which solution should you choose?

- [ ] Front door
- [ ] API Management
- [ ] Traffic manager
- [x] Application Gateway

Q14. You have .NET app running CM scale set. You need to monitor application performance without modyfying the code. The solution should minimise the cost. What should you do?

- [ ] Enable network performance monitor on the VMs
- [ ] install the Log Analytics Agent and enable Azure Monitor for VMs
- [x] Install Application Insights Agent
- [ ] Enable SolarWinds Performance Monitor from the Azure Marketplace

Q15. When setting your CI/CD pipeline an approval from your product owner is required before a final release to production. What solution do you use to achieve this?

- [ ] Manual intervention task
- [x] pre-deployment condition
- [ ] branch filer
- [ ] pre-deployment gate

Q16. You want to configure the AKS instance running the Kineteco Inventory App to use Azure Active Directory (AD) for user authentication. To integrate with AKS with Azure AD which steps should you perform first?

- [ ] Create a service principal in Azure then assign the service principal AKS.
- [ ] Add users an Azure AD security group. Then assign the group permissions to AKS.
- [ ] Create a service principal in Azure AD. Then add user to the AKS security group. <<<<----Correct
- [ ] Create an App ID in Azure AD. Then create a service principal for the server app.

Q17. Which access protocol does Azure Files not support?

- [ ] Network File System (NFS)
- [ ] HTTP <<<<----Correct
- [ ] REST API
- [ ] Server Message Block(SMB)

Q18. You are writing an app for a sales team. You need to implement security in SQL Server to ensure that sales representatives see customer financial information only for customers whom they manage. Your app must make this transparent to the user. Which SQL data security option should you choose?

- [ ] Dynamic Data Masking <<<<----Correct
- [ ] Transparent Data Encryption
- [ ] Row-Level Security
- [ ] Always Encrypted

Q19. You configure access to secrets in Azure Key Vault with **\_**.

- [ ] service principals
- [ ] certificates
- [ ] access policies
- [ ] RBAC roles <<<<----Correct

Q20. Your Kineteco Web App experiences occasional spikes in usage that cause resource shortages that generate an alert. When this occurs, you want to configure scale out of the App Service plan resources. The solution should minimize cost and administrative effort. What should you do?

- [ ] Create a Logic App. Then configure an action group with the Logic App action type.
- [ ] Create an Azure Automation Runbook. Then configure an action group with the Automation Runbook action type.
- [ ] Configure an rule based on a metric. <<<<----Correct
- [ ] Create an Azure function. Then configure an action group with the Secure Webhook action type.

Q21. You have CI/CD pipeline for a modern web application in Azure DevOps. The CI/CD process includes both a build and a release pipeline. You need to ensure that user testing (UAT) is successful before triggering the release pipeline. The process should be automated as possible. What should you add to your build pipeline?

- [ ] Query Work Items gate
- [ ] Manual Intervention task
- [ ] Approval gate <<<<----Correct
- [ ] Invoke REST API gate

Q22. The Kineteco Web App is running on AKS to meet a spike in demand, the horizontal pod autoscaler recently provisioned additional pods, which are no longer needed. What should you do to scale down unnecessary pods?

- [ ] Trigger scale down in Azure Container Instances.
- [ ] Trigger scale down in the HPA from the Azure CLI.
- [ ] Manually deprovision unneeded pods.
- [ ] Do nothing. EPA will initiate scale down automatically. <<<<----Correct

Q23. Your ARM template, created in VS Code, is failing validation in the build pipeline in Azure DevOps. You need to correct syntax issues at authoring time with a minimum of cost and effort. What should you do?

- [ ] Install Azure extension in VS Code. <<<<----Correct
- [ ] Install Visual Studio 2019 Enterprise edition.
- [ ] Install Visual Studio 2019 Community edition.
- [ ] Install Visual Studio Code Intellicode extension in VS Code.

Q24. You need to migrate the backlog of a development project for a newly acquired subsidiary. The development team currently uses a Kanban board to track stories, tasks, and bugs. Which process framework should you select in Azure Boards?

- [ ] Agile <<<<----Correct
- [ ] Waterfall
- [ ] Basic
- [ ] CMMI

Q25. You have set of SQL databases used with various PaaS applications with predictable usage patterns. You are planning to move these databases to Azure SQL and need to choose the right deployment option. Your priorities are minimizing costs, and having the ability to assign CPU and resources to individual databases. Which option should you choose?

- [ ] Azure SQL elastic pool <<<<----Correct
- [ ] SQL on Azure VMs
- [ ] Azure SQL Database
- [ ] SQL Managed Instance

Q26. Your photo app hosted in Azure records user operations in a log for historical reference. Records must not be overwritten. Which storage type should you select to host log data?

- [ ] append blob <<<<----Correct
- [ ] table storage
- [ ] page blob
- [ ] block blob

Q27. The Kineteco Retail App uses keys for signing and encryption of some data transfers. How should you write your app to invoke keys?

- [ ] Azure CLI
- [ ] Azure Portal <<<<----Correct
- [ ] Azure PowerShell
- [ ] REST API

Q28. You need to create tech support chatbot for Microsoft teams that interacts with users based on natural language processing (NLP). The bot should be capable of processing differing sentence structures. Which Microsoft framework component will deliver this functionality?

- [ ] LUIS <<<<----Correct
- [ ] Text to Speech
- [ ] QnA Maker
- [ ] Recognizer

Q29. You are implementing an application to manage automated warehouse operations for a global retailer. You need to design an enrollment process for IoT devices for production use. Solution requirements are as follows: Register IoT devices in bulk; encrypt all communication between devices and the Azure IoT cloud service; and implement Microsoft recommendations for device security. Which option should you choose?

- [ ] managed identity (shared)
- [ ] X.509 certificate <<<<----Correct
- [ ] managed service identity (per device)
- [ ] SAS key

Q30. You are deploying three Azure VMS with an Azure Resource Manager (ARM) template. Which ARM function implements the iteration loop to provision the right number of VMs?
´´´´{
"type": "Microsoft.Compute/virtualMachines",
"name": "[concat('myvm', `______`)]",
"apiVersion": "2016-04-30-preview",
"location": "[parameters('location')]",
"copy": {
"name": "virtualMachineLoop",
"count": "[parameters('numberOfInstances')]"
},´´´´

- [ ] max()
- [ ] copyIndex() <<<<----Correct
- [ ] createArray()
- [ ] indexOf()

Q31. The Kineteco web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

- [ ] Install the Analytics agent and configure Azure Monitor for Containers.
- [ ] Install the App Insights Agent on AKS nodes.
- [ ] Configure Application Insights cohorts. <<<<----Correct
- [ ] Add instrumentation to your app to send usage analysis with Application Insights.

Q32. Your web app hosted on Azure VMS generates a large number of random (non-sequential) writes. Which storage type should you select for your application?

- [ ] page blob <<<<----Correct
- [ ] block blob
- [ ] table storage
- [ ] queue storage

Q33. You are configuring a release pipeline in Azure DevOps. You need to reference several application variables across multiple pipelines at deployment time. How should you store application variables?

- [ ] Store secrets in Azure Key Vault.
- [ ] Store secrets in a configuration file.
- [ ] Configure release variables.
- [ ] Configure a variable group. <<<<----Correct

Q34. You have configured the Kineteco Web App to run on Azure Kubernetes Service (AKS). Application resources need to scale to meet spikes in traffic. What should you do? The solution should minimize manual effort and cost

- [ ] Configure the horizontal pod autoscaler (HPA).
- [ ] Manually scale pod when necessary.
- [ ] Configure burst to Azure Container Instances.
- [ ] Do nothing. Pods running on AKS scale up automatically. <<<<----Correct

Q35. You are configuring a release pipeline in Azure DevOps. You need to read secrets from Azure Key Vault during pipeline execution. How should you retrieve application variables?

- [ ] with a community-developed Key Vault task
- [ ] with an ARM template
- [ ] all of these answers <<<<----Correct
- [ ] with an Azure CLI script in a Bash task

Q36. You need to update the data within an existing database in Azure SQL with your changes. You want to test this process from your development workstation before incorporating the update into your CI/CD process. Which command will you run to update the schema on the target database?

- [ ] SqlPackage.exe /TargetFile:" myapp.bacpac " /Action:**Export** <<<<----Correct
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
- [ ] SqlPackage.exe /TargetFile:" myapp.bacpac " /Action:**Import**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
      SqiPackage.exe /TargetFile :" myapp.bacpac Action:Import
- [ ] SqlPackage.exe /TargetFile:"./myapp.bacpac" /Action:**Publish**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
- [ ] SqlPackage.exe /TargetFile:"./myapp.bacpac" /Action:**Extract**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"

Q37. You have web app hosted in Azure App Service that reads from and writes data to an Azure SQL Database back-end. You need to send email alert when your web app returns any failure HTTP status cede (anything except HTTP 200) for a user request. Which solution should you use?

- [ ] service map in Azure Monitor <<<<----Correct
- [ ] application maps in Azure Application Insights
- [ ] availability tests in Azure Application Insights
- [ ] Profiler in Azure Application Insights

Q38. Your new release pipeline in Azure DevOps includes a Bash task that runs an Azure CLI script. The Bash task running script fails. The agent setting of the agent job in the release pipeline is pictured below. The solution must minimize cost. What should you change in agent pool settings?

- [ ] Change to a self-hosted agent pool running Ubuntu 16.04 LTS or later.
- [ ] Changed to a hosted pool running Windows 2019.
- [ ] Change to a hosted agent pool running Ubuntu 16.04 LTS or later. <<<<----Correct
- [ ] Change to a self-hosted agent pool running Windows 2019.

Q39. You are selecting a cloud messaging solution for your retail mobile app. Requirements for the solution are: Process messages in the order they are received: preserve messages in case of a processing delay; end guarantee message delivery. Which solution should you use?

- [ ] Event Grid
- [ ] Service Bus <<<<----Correct
- [ ] Event Hub
- [ ] Queue Storage

Q40. You need to provision a port mapping on the underlying node that allows the application to be accessed directly with the IP address and on the cluster node. Which service type should you provision?

- [ ] LoadBalancer
- [ ] NodePort <<<<----Correct
- [ ] Cluster IP
- [ ] ExternalName

Q41. What is the difference between a user-assigned managed identity and a system-assigned managed identity?

- [ ] The lifecycle of a user-managed identity is managed separately from the resource. <<<<----Correct
- [ ] with a user-assigned managed identity, Azure manages the password for you.
- [ ] The lifecycle of a system-managed identity is managed separately from the resource.
- [ ] with a system-assigned managed identity, Azure manages the password for you.

Q42. You need to configure user access to Azure DevOps agent pools to meet the following requirements: Use an agent pool when authoring build or release pipelines for the project; view the agent pool and agents of the organization; and use the principle of least privilege. Which role memberships are required for the Azure DevOps organization and the project?

- [ ] Organization: Administrator; Project: Service Account
- [ ] Organization: Reader; Project: Service Account <<<<---Correct
- [ ] Organization: Reader; Project: Administrator
- [ ] Organization: Service Account; Project: Reader

Q43. You have created an Azure CLI script for a release pipeline in Azure DevOps. You need to reference the working directory for the running job. Which variable should you reference?

- [ ] Agent.WorkFolder <<<<---Correct
- [ ] Agent.HomeDirectory
- [ ] Agent.BuildDirectory
- [ ] Agent.ToolsDirectory

Q44. You are selecting Azure technologies for a new a pp that will process print jobs in a facility with thousands of printers. A pool of worker processes willsend jobs to printer and report results when jobs are complete. Requirements for the solution are: Worker processes will retrieve and process messages as capacity permits; if a worker process or printer fails, a worker process should be able to retrieve message and resurne processing; and the solution should maintain a central (server-side) log of messages processed. Which solution should you use?

- [ ] Event Hub
- [ ] Event Grid
- [ ] Service Bus
- [ ] Queue Storage
