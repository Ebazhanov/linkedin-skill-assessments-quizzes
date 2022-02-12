## Microsoft Azure

#### Q1. You need to create an application in Azure AD representing the Kineteco Web App so you can assign directory permissions to the app. To create the application identity, which command will you run?

- [ ] `bash az ad app permission grant -display-name $appName \ ...`
- [ ] `bash az ad app credential create -display-name $appName \ ...`
- [x] `bash az ad app create -display-name $appName \ ...`
- [ ] `bash az ad app permission ass -display-name $appName \ ...`

#### Q2. You need to deliver a mobile push notification feature for the Kineteco Retail app, hosted in Azure App Service. The solution should minimize cost, complexity, and development effort. Which option should you choose?

- [x] Notification Hub
- [ ] Event Grid
- [ ] Twilio
- [ ] Service Bus

**Explanation:** Twilio is an SMS notification app, also not from Microsoft. Event Grid can be techincally used for this purpose but it's a more generic event-broadcasting service. Service Bus is another generic publish-subscribe solution. Finally [Notification Hubs](https://docs.microsoft.com/en-us/azure/notification-hubs/notification-hubs-push-notification-overview) are specifically designed for push-notifications.

#### Q3. Your application hosted in Azure App Service needs to retrieve secrets from Azure Key Vault. Which choice is NOT a way to authenticate to Key Vault?

- [ ] service principal and a certificate
- [ ] managed identity
- [ ] service principal and a secret
- [x] shared access key

[Azure Key Vault Developer's Guide](https://docs.microsoft.com/en-us/azure/key-vault/general/developers-guide#authenticate-to-key-vault-in-code) lists 3 available methods. The _shared access key_ does not exist in Azure at all, the closest term is _shared access signature (SAS)_ but it's used to access Azure Storage only.

#### Q4. You added a persistent volume claim to your apps YAML manifest. When you attempt to deploy to an existing AKS cluster there is no persistent volume available. What should you do?

- [ ] Do nothing. The API server will provision additional storage automatically
- [x] Add a data disk definition for the AKS cluster to your apps YAML manifest
- [ ] Add a data disk to each Kubernetes cluster node and reattempt app deployment
- [ ] Provision an Azure Files instance and reattempt app deployment

#### Q5. Your corporate web application is hosted in Azure regional data centres around the world. You need to route user requests to the closest service endpoint based on response latency. Which routing method should you use?

- [ ] Application gateway
- [ ] Front Door
- [ ] API Management
- [x] Traffic manager

#### Q6. You are developing a release strategy for several related software components. You need to reference variable groups and secure files across multiple build and release pipelines. What is the most efficient way to store and reference these assets from the pipeline?

- [ ] Add the assets to a git repository
- [x] Add the assets in Key Vault
- [ ] Add the assets to an encrypted volume
- [ ] Add the assets to a library

#### Q7. You need to grant full access for an app to a temporary Azure storage account. Configuring access should require minimum effort. Which option should you use?

- [ ] Azure AD user account
- [x] Shared access signature
- [ ] Shared key
- [ ] Certificate

[Shared access signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) exists exactly for the purpose of giving a temporary access. Azure AD user account is not temporary so it needs to be managed. Creating/revoking Certificates for temporary access is just too much hassle.

#### Q8. The Kineteco web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

- [ ] Configure application insights cohort
- [ ] Install the Log Analytics agent and configure Azure Monitor for Containers
- [ ] Install the App Insights on AKS nodes
- [ ] Add instrumentation to your app to send usage analytics with Application Insights.

[Container Monitoring doc](https://docs.microsoft.com/en-us/azure/azure-monitor/containers/containers) explicitly mentions that it's not for AKS. 3 and 4 look right

#### Q9. Which choice is not a valid trigger for an Azure functions?

- [ ] based on a time (schedule)
- [ ] another Azure service (cosmos, service bus)
- [ ] threshold alert in Azure App insights
- [x] third party services (GitHub)

#### Q10. Which messaging service enables an event-driven programming model?

- [ ] Service Bus
- [ ] Event Hub
- [ ] Notification Hub
- [x] Event Grid

#### Q11. You need to populate a newly created SQL database from your release pipeline in Azure DevOps. The solution should minimize deployment time and efforts. Which approach should you use?

- [x] Populate from a BACPAC file.
- [ ] Restore from a backup file.
- [ ] Populate from a CSV file.
- [ ] Populate from a SQL file.

#### Q12. You need to host a community website for your neighborhood association. The site contains static content, including HTML, CSS, and a few pages with client-side JavaScript. The site contains no sensitive information, and CORS support is unnecessary. The association has limited funds to pay for hosting, so the solution should be as inexpensive as possible. Which option should you use?

- [x] Azure Storage static website
- [ ] static website with Azure CDN
- [ ] App Service on Consumption plan
- [ ] App Service on Standard plan

#### Q13. Your organization delivers a number of RESTful web services to customers around the world. You need to deploy cloud infrastructure to deliver these services to paying customers, including authentication, request throttling and routing of requests to the closest service endpoint. Which solution should you choose?

- [ ] Front door
- [x] API Management
- [ ] Traffic manager
- [ ] Application Gateway

**Hint:** If you see the words REST and throttling - the answer is almost always API Management. It's the most expensive solution but is specifically designed to proxy the REST API.

#### Q14. You have a .NET app running on a VM Scale set. You need to monitor application performance without modifying the code. The solution should minimize the cost. What should you do?

- [ ] Enable Network Performance Monitor on the VMs.
- [ ] Install the Log Analytics Agent and enable Azure Monitor for VMs.
- [x] Install the Application Insights Agent.
- [ ] Enable SolarWinds Performance Monitor from the Azure Marketplace.

#### Q15. When setting your CI/CD pipeline an approval from your product owner is required before a final release to production. What solution do you use to achieve this?

- [ ] a Manual Intervention task
- [x] a pre-deployment condition
- [ ] a branch filter
- [ ] a pre-deployment gate

#### Q16. You want to configure the AKS instance running the Kineteco Inventory App to use Azure Active Directory (AD) for user authentication. To integrate with AKS with Azure AD which steps should you perform first?

- [ ] Create a service principal in Azure then assign the service principal AKS.
- [ ] Add users an Azure AD security group. Then assign the group permissions to AKS.
- [x] Create a service principal in Azure AD. Then add user to the AKS security group.
- [ ] Create an App ID in Azure AD. Then create a service principal for the server app.

#### Q17. Which access protocol does Azure Files not support?

- [ ] Network File System (NFS)
- [x] HTTPS
- [ ] REST API
- [ ] Server Message Block(SMB)

[What is Azure Files?](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-introduction) page mentions the supported protocols.

#### Q18. You are writing an app for a sales team. You need to implement security in SQL Server to ensure that sales representatives see customer financial information only for customers whom they manage. Your app must make this transparent to the user. Which SQL data security option should you choose?

- [x] Dynamic Data Masking
- [ ] Transparent Data Encryption
- [ ] Row-Level Security
- [ ] Always Encrypted

#### Q19. You configure access to secrets in Azure Key Vault with `__`.

- [ ] service principals
- [ ] certificates
- [ ] access policies
- [x] RBAC roles

#### Q20. Your Kineteco Web App experiences occasional spikes in usage that cause resource shortages that generate an alert. When this occurs, you want to configure scale out of the App Service plan resources. The solution should minimize cost and administrative effort. What should you do?

- [ ] Create a Logic App. Then configure an action group with the Logic App action type.
- [ ] Create an Azure Automation Runbook. Then configure an action group with the Automation Runbook action type.
- [x] Configure an autoscale rule based on a metric.
- [ ] Create an Azure function. Then configure an action group with the Secure Webhook action type.

#### Q21. You have CI/CD pipeline for a modern web application in Azure DevOps. The CI/CD process includes both a build and a release pipeline. You need to ensure that user testing (UAT) is successful before triggering the release pipeline. The process should be automated as possible. What should you add to your build pipeline?

- [ ] Query Work Items gate
- [ ] Manual Intervention task
- [x] Approval gate
- [ ] Invoke REST API gate

#### Q22. The Kineteco Web App is running on AKS. To meet a spike in demand, the horizontal pod autoscaler recently provisioned additional pods, which are no longer needed. What should you do to scale down unnecessary pods?

- [ ] Trigger scale down in Azure Container Instances.
- [ ] Trigger scale down in the HPA from the Azure CLI.
- [ ] Manually deprovision unneeded pods.
- [x] Do nothing. HPA will initiate scale down automatically.

#### Q23. Your ARM template, created in VS Code, is failing validation in the build pipeline in Azure DevOps. You need to correct syntax issues at authoring time with a minimum of cost and effort. What should you do?

- [x] Install Azure Resource Manager Tools extension in VS Code.
- [ ] Install Visual Studio 2019 Enterprise edition.
- [ ] Install Visual Studio 2019 Community edition.
- [ ] Install Visual Studio Code IntelliCode extension in VS Code.

#### Q24. You need to migrate the backlog of a development project for a newly acquired subsidiary. The development team currently uses a Kanban board to track stories, tasks, and bugs. Which process framework should you select in Azure Boards?

- [x] Agile
- [ ] Waterfall
- [ ] Basic
- [ ] CMMI

#### Q25. You have set of SQL databases used with various PaaS applications with predictable usage patterns. You are planning to move these databases to Azure SQL and need to choose the right deployment option. Your priorities are minimizing costs, and having the ability to assign CPU and resources to individual databases. Which option should you choose?

- [x] Azure SQL elastic pool
- [ ] SQL on Azure VMs
- [ ] Azure SQL Database
- [ ] SQL Managed Instance

#### Q26. Your photo app hosted in Azure records user operations in a log for historical reference. Records must not be overwritten. Which storage type should you select to host log data?

- [x] append blob
- [ ] table storage
- [ ] page blob
- [ ] block blob

#### Q27. The Kineteco Retail App uses keys for signing and encryption of some data transfers. How should you write your app to invoke keys?

- [ ] Azure CLI
- [x] Azure Portal
- [ ] Azure PowerShell
- [ ] REST API

#### Q28. You need to create a tech support chatbot for Microsoft Teams that interacts with users based on natural language processing (NLP). The bot should be capable of processing differing sentence structures. Which Microsoft Bot Framework component will deliver this functionality?

- [x] LUIS
- [ ] Text to Speech
- [ ] QnA Maker
- [ ] Form Recognizer

#### Q29. You are implementing an application to manage automated warehouse operations for a global retailer. You need to design an enrollment process for IoT devices for production use. Solution requirements are as follows: Register IoT devices in bulk; encrypt all communication between devices and the Azure IoT cloud service; and implement Microsoft recommendations for device security. Which option should you choose?

- [ ] managed identity (shared)
- [x] X.509 certificate
- [ ] managed service identity (per device)
- [ ] SAS key

#### Q30. You are deploying three Azure VMS with an Azure Resource Manager (ARM) template. Which ARM function implements the iteration loop to provision the right number of VMs?

```json
{
    "type": "Microsoft.Compute/virtualMachines",
    "name": "[concat('myvm', `______`)]",
    "apiVersion": "2016-04-30-preview",
    "location": "[parameters('location')]",
    "copy": " ",
    "name": "virtualMachineLoop",
    "count": "[parameters('numberOfInstances')]"
},
```

- [ ] max()
- [x] copyIndex()
- [ ] createArray()
- [ ] indexOf()

#### Q31. The Kineteco web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

- [ ] Install the Analytics agent and configure Azure Monitor for Containers.
- [ ] Install the App Insights Agent on AKS nodes.
- [x] Configure Application Insights cohorts.
- [ ] Add instrumentation to your app to send usage analysis with Application Insights.

#### Q32. Your web app hosted on Azure VMS generates a large number of random (non-sequential) writes. Which storage type should you select for your application?

- [x] page blob
- [ ] block blob
- [ ] table storage
- [ ] queue storage

#### Q33. You are configuring a release pipeline in Azure DevOps. You need to reference several application variables across multiple pipelines at deployment time. How should you store application variables?

- [ ] Store secrets in Azure Key Vault.
- [ ] Store secrets in a configuration file.
- [ ] Configure release variables.
- [x] Configure a variable group.

#### Q34. You have configured the Kineteco Web App to run on Azure Kubernetes Service (AKS). Application resources need to scale to meet spikes in traffic. What should you do? The solution should minimize manual effort and cost.

- [ ] Configure the horizontal pod autoscaler (HPA).
- [ ] Manually scale pod when necessary.
- [ ] Configure burst to Azure Container Instances.
- [x] Do nothing. Pods running on AKS scale up automatically.

#### Q35. You are configuring a release pipeline in Azure DevOps. You need to read secrets from Azure Key Vault during pipeline execution. How should you retrieve application variables?

- [ ] with a community-developed Key Vault task
- [ ] with an ARM template
- [x] all of these answers
- [ ] with an Azure CLI script in a Bash task

#### Q36. You need to update the data within an existing database in Azure SQL with your changes. You want to test this process from your development workstation before incorporating the update into your CI/CD process. Which command will you run to update the schema on the target database?

- [x] SqlPackage.exe /TargetFile:" myapp.bacpac " /Action:**Export**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
- [ ] SqlPackage.exe /TargetFile:" myapp.bacpac " /Action:**Import**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
- [ ] SqlPackage.exe /TargetFile:"./myapp.bacpac" /Action:**Publish**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"
- [ ] SqlPackage.exe /TargetFile:"./myapp.bacpac" /Action:**Extract**
      /SourceServerName:"kinetecosql.database.windows.net"
      /SourceDatabaseName:"kinetecoweb" /SourceUser:"admin" /SourcePassword:"MyPassword"

#### Q37. You have a web app hosted in Azure App Service that reads from and writes data to an Azure SQL Database back-end. You need to send email alert when your web app returns any failure HTTP status code (anything except HTTP 200) for a user request. Which solution should you use?

- [x] service map in Azure Monitor
- [ ] application maps in Azure Application Insights
- [ ] availability tests in Azure Application Insights
- [ ] Profiler in Azure Application Insights

#### Q38. Your new release pipeline in Azure DevOps includes a Bash task that runs an Azure CLI script. The Bash task running script fails. The agent setting of the agent job in the release pipeline is pictured below. The solution must minimize cost. What should you change in agent pool settings?

- [ ] Change to a self-hosted agent pool running Ubuntu 16.04 LTS or later.
- [ ] Changed to a hosted pool running Windows 2019.
- [x] Change to a hosted agent pool running Ubuntu 16.04 LTS or later.
- [ ] Change to a self-hosted agent pool running Windows 2019.

#### Q39. You are selecting a cloud messaging solution for your retail mobile app. Requirements for the solution are: Process messages in the order they are received: preserve messages in case of a processing delay; end guarantee message delivery. Which solution should you use?

- [ ] Event Grid
- [x] Service Bus
- [ ] Event Hub
- [ ] Queue Storage

#### Q40. You need to provision a port mapping on the underlying node that allows the application to be accessed directly with the IP address and on the cluster node. Which service type should you provision?

- [ ] LoadBalancer
- [x] NodePort
- [ ] Cluster IP
- [ ] ExternalName

#### Q41. What is the difference between a user-assigned managed identity and a system-assigned managed identity?

- [x] The lifecycle of a user-managed identity is managed separately from the resource.
- [ ] with a user-assigned managed identity, Azure manages the password for you.
- [ ] The lifecycle of a system-managed identity is managed separately from the resource.
- [ ] with a system-assigned managed identity, Azure manages the password for you.

#### Q42. You need to configure user access to Azure DevOps agent pools to meet the following requirements: Use an agent pool when authoring build or release pipelines for the project; view the agent pool and agents of the organization; and use the principle of least privilege. Which role memberships are required for the Azure DevOps organization and the project?

- [ ] Organization: Administrator; Project: Service Account
- [x] Organization: Reader; Project: Service Account
- [ ] Organization: Reader; Project: Administrator
- [ ] Organization: Service Account; Project: Reader

#### Q43. You have created an Azure CLI script for a release pipeline in Azure DevOps. You need to reference the working directory for the running job. Which variable should you reference?

- [x] Agent.WorkFolder
- [ ] Agent.HomeDirectory
- [ ] Agent.BuildDirectory
- [ ] Agent.ToolsDirectory

#### Q44. You are selecting Azure technologies for a new a pp that will process print jobs in a facility with thousands of printers. A pool of worker processes will send jobs to printer and report results when jobs are complete. Requirements for the solution are: Worker processes will retrieve and process messages as capacity permits; if a worker process or printer fails, a worker process should be able to retrieve message and resume processing; and the solution should maintain a central (server-side) log of messages processed. Which solution should you use?

- [ ] Event Hub
- [ ] Event Grid
- [ ] Service Bus
- [x] Queue Storage

#### Q45. In Azure Key Vault, you can manage access to your application secrets by setting permissions at any level except **\_**.

- [ ] on the secret itself
- [ ] by secret type
- [ ] on the Key Vault instance
- [x] at the Azure Subscription level

#### Q46. Your company hosts a web application that uses Azure SQL Database to store data. You need to implement measures that allow only members of the managers group to see sensitive information. Which two actions should you perform?

- [ ] Implement dynamic data masking and include the managers group.
- [ ] Implement transparent data encryption and include the managers group.
- [x] Implement dynamic data masking and exclude the managers group.
- [ ] Implement transparent data encryption and exclude the managers group.

`Dynamic data masking helps prevent unauthorized access to sensitive data by enabling customers to designate how much of the sensitive data to reveal with minimal impact on the application layer.`
[Reference](https://docs.microsoft.com/en-us/powershell/module/azurerm.sql/new-azurermsqldatabasedatamaskingrule?view=azurermps-6.13.0)

#### Q47. The Kineteco Inventory App uses an Azure SQL Database instance to store application and store inventory data. Store employees report occasional periods where queries in the web interface never return data. You suspect a database issue and need to identify the performance issue as soon as possible. The resource health dashboard reports "No health related issues found." What should you do?

- [ ] Run the troubleshooting wizards under Resource and solve problems.
- [x] Enable Intelligent Insights.
- [ ] Configure App Insights to alert admins when web interface experiences latency.
- [ ] Configure an alert rule to email DBAs when DTU usage hits 100%.

#### Q48. Your web application needs to access files on an Azure Files share. Which option will deliver the highest throughput?

- [x] SMB
- [ ] REST API
- [ ] Storage Explorer
- [ ] NFS

#### Q49. You have source code for a project in a repository on GitHub. You need to migrate source code to a repository in Azure Repos. The solution should minimize effort. Which solution should you recommend?

- [ ] Download the GitHub repository to a Zip file, and then unzip the repository in Azure DevOps.
- [x] From the **Import a Git repository** menu, select **Import**.
- [ ] Create a service connection to the GitHub repository.
- [ ] Create a webhook in GitHub and then trigger it from Azure DevOps.

#### Q50. You need to facilitate user acceptance testing (UAT) on your web application hosted in App Service. Testers must approve changes before they are deployed to production. You should implement support for these requirements with a minimum of cost and complexity. What should you do?

- [ ] Configure an additional App Service instance. In Azure DevOps, enable an approval gate for deployment.
- [ ] Configure an Azure load balancer to redirect traffic to the approved App Service instance.
- [x] Configure an additional deployment slot in the existing App Service instance.
- [ ] Configure an App Service Environment (ASE).

#### Q51. Your microservices application includes a logging component that performs a large number of sequentinal writes. Which type of Azure Storage should you use?

- [ ] Table storage
- [x] append blob
- [ ] page blob
- [ ] block blob

#### Q52. Group policy objects are not being applied to domain controllers because the Default Domain Controllers and Default Domain group policies are corrupt. What can you run in a command prompt to recover them?

- [ ] `dcpromo.exe`
- [x] `dcgpofix.exe`
- [ ] `dcdiagfix.exe`
- [ ] `ntdsutil.exe`

#### Q53. Your JavaScript app hosted in Azure App Service needs to be able to make calls to a remote domain in another Azure region. Which App Service feature do you need to configure?

- [x] `CORS`
- [ ] `deployment slots`
- [ ] `WebJobs`
- [ ] `custom domains`

As described in [Microsoft Docs: Hosting a Restful-API with CORS in AAS](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api): The Answer should be CORS (Cross Origin Ressource Sharing)

#### Q54. Bindings in Azure Function triggers have a direction property that is always \_.

- [ ] parallel
- [ ] out
- [ ] asynchronous
- [x] in

#### Q55. You are selecting a cloud messaging solution for your multimedia news app. The app routes news items to the appropriate services for processing and delivery to subscribers. Requirements for the solution are as follows: Events should be routed to the appropriate service to process event; events must be routed to multiple services when necessary; and only relevant events should be routed to a service for processing. Which solution should you use?

- [ ] Event Grid
- [ ] Service Bus
- [ ] Event Hub
- [ ] Queue Storage
