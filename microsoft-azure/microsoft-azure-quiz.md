## Microsoft Azure

#### Q1. You need to create an application in Azure AD representing the Kineteco Web App so you can assign directory permissions to the app. To create the application identity, which command will you run?

- [ ] `bash az ad app permission grant -display-name $appName \ ...`
- [ ] `bash az ad app credential create -display-name $appName \ ...`
- [x] `bash az ad app create -display-name $appName \ ...`
- [ ] `bash az ad app permission ass -display-name $appName \ ...`

[Ref](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest)

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
- [ ] Add the assets in Key Vault
- [ ] Add the assets to an encrypted volume
- [x] Add the assets to a library

[Ref](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/?view=azure-devops)

#### Q7. You need to grant full access for an app to a temporary Azure storage account. Configuring access should require minimum effort. Which option should you use?

- [ ] Azure AD user account
- [x] Shared access signature
- [ ] Shared key
- [ ] Certificate

[Shared access signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) exists exactly for the purpose of giving a temporary access. Azure AD user account is not temporary so it needs to be managed. Creating/revoking Certificates for temporary access is just too much hassle.

#### Q8. Which choice is not a valid trigger for an Azure functions?

- [ ] based on a time (schedule)
- [ ] another Azure service (cosmos, service bus)
- [x] threshold alert in Azure App insights
- [ ] third party services (GitHub)

[Ref](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=csharp)

#### Q9. Which messaging service enables an event-driven programming model?

- [ ] Service Bus
- [ ] Event Hub
- [ ] Notification Hub
- [x] Event Grid

[Ref](https://docs.microsoft.com/en-us/azure/event-grid/compare-messaging-services)

#### Q10. You need to populate a newly created SQL database from your release pipeline in Azure DevOps. The solution should minimize deployment time and efforts. Which approach should you use?

- [x] Populate from a BACPAC file.
- [ ] Restore from a backup file.
- [ ] Populate from a CSV file.
- [ ] Populate from a SQL file.

#### Q11. You need to host a community website for your neighborhood association. The site contains static content, including HTML, CSS, and a few pages with client-side JavaScript. The site contains no sensitive information, and CORS support is unnecessary. The association has limited funds to pay for hosting, so the solution should be as inexpensive as possible. Which option should you use?

- [x] Azure Storage static website
- [ ] static website with Azure CDN
- [ ] App Service on Consumption plan
- [ ] App Service on Standard plan

#### Q12. Your organization delivers a number of RESTful web services to customers around the world. You need to deploy cloud infrastructure to deliver these services to paying customers, including authentication, request throttling and routing of requests to the closest service endpoint. Which solution should you choose?

- [ ] Front door
- [x] API Management
- [ ] Traffic manager
- [ ] Application Gateway

**Hint:** If you see the words REST and throttling - the answer is almost always API Management. It's the most expensive solution but is specifically designed to proxy the REST API.

#### Q13. You have a .NET app running on a VM Scale set. You need to monitor application performance without modifying the code. The solution should minimize the cost. What should you do?

- [ ] Enable Network Performance Monitor on the VMs.
- [ ] Install the Log Analytics Agent and enable Azure Monitor for VMs.
- [x] Install the Application Insights Agent.
- [ ] Enable SolarWinds Performance Monitor from the Azure Marketplace.

#### Q14. When setting your CI/CD pipeline an approval from your product owner is required before a final release to production. What solution do you use to achieve this?

- [ ] a Manual Intervention task
- [x] a pre-deployment condition
- [ ] a branch filter
- [ ] a pre-deployment gate

#### Q15. You want to configure the AKS instance running the Kineteco Inventory App to use Azure Active Directory (AD) for user authentication. To integrate with AKS with Azure AD which steps should you perform first?

- [ ] Create a service principal in Azure then assign the service principal AKS.
- [ ] Add users an Azure AD security group. Then assign the group permissions to AKS.
- [x] Create a service principal in Azure AD. Then add user to the AKS security group.
- [ ] Create an App ID in Azure AD. Then create a service principal for the server app.

#### Q16. Which access protocol does Azure Files not support?

- [ ] Network File System (NFS)
- [x] HTTPS
- [ ] REST API
- [ ] Server Message Block(SMB)

[What is Azure Files?](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-introduction) page mentions the supported protocols.

#### Q17. You are writing an app for a sales team. You need to implement security in SQL Server to ensure that sales representatives see customer financial information only for customers whom they manage. Your app must make this transparent to the user. Which SQL data security option should you choose?

- [x] Dynamic Data Masking
- [ ] Transparent Data Encryption
- [ ] Row-Level Security
- [ ] Always Encrypted

#### Q18. You configure access to secrets in Azure Key Vault with `__`.

- [ ] service principals
- [ ] certificates
- [ ] access policies
- [x] RBAC roles

[Controlling access to Key Vault data](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features#controlling-access-to-key-vault-data)

#### Q19. Your Kineteco Web App experiences occasional spikes in usage that cause resource shortages that generate an alert. When this occurs, you want to configure scale out of the App Service plan resources. The solution should minimize cost and administrative effort. What should you do?

- [ ] Create a Logic App. Then configure an action group with the Logic App action type.
- [ ] Create an Azure Automation Runbook. Then configure an action group with the Automation Runbook action type.
- [x] Configure an autoscale rule based on a metric.
- [ ] Create an Azure function. Then configure an action group with the Secure Webhook action type.

#### Q20. You have CI/CD pipeline for a modern web application in Azure DevOps. The CI/CD process includes both a build and a release pipeline. You need to ensure that user testing (UAT) is successful before triggering the release pipeline. The process should be automated as possible. What should you add to your build pipeline?

- [ ] Query Work Items gate
- [ ] Manual Intervention task
- [x] Approval gate
- [ ] Invoke REST API gate

#### Q21. The Kineteco Web App is running on AKS. To meet a spike in demand, the horizontal pod autoscaler recently provisioned additional pods, which are no longer needed. What should you do to scale down unnecessary pods?

- [ ] Trigger scale down in Azure Container Instances.
- [ ] Trigger scale down in the HPA from the Azure CLI.
- [ ] Manually deprovision unneeded pods.
- [x] Do nothing. HPA will initiate scale down automatically.

#### Q22. Your ARM template, created in VS Code, is failing validation in the build pipeline in Azure DevOps. You need to correct syntax issues at authoring time with a minimum of cost and effort. What should you do?

- [x] Install Azure Resource Manager Tools extension in VS Code.
- [ ] Install Visual Studio 2019 Enterprise edition.
- [ ] Install Visual Studio 2019 Community edition.
- [ ] Install Visual Studio Code IntelliCode extension in VS Code.

#### Q23. You need to migrate the backlog of a development project for a newly acquired subsidiary. The development team currently uses a Kanban board to track stories, tasks, and bugs. Which process framework should you select in Azure Boards?

- [x] Agile
- [ ] Waterfall
- [ ] Basic
- [ ] CMMI

#### Q24. You have set of SQL databases used with various PaaS applications with predictable usage patterns. You are planning to move these databases to Azure SQL and need to choose the right deployment option. Your priorities are minimizing costs, and having the ability to assign CPU and resources to individual databases. Which option should you choose?

- [x] Azure SQL elastic pool
- [ ] SQL on Azure VMs
- [ ] Azure SQL Database
- [ ] SQL Managed Instance

**Explanation:** For many businesses and applications, creating individual databases and scaling performance up or down as needed is sufficient, especially when usage patterns are relatively predictable. Unpredictable usage patterns can make it difficult to manage costs and your business model. Elastic pools aim to solve this problem. Performance resources are allocated to a pool, not to a single database. You pay for the collective performance resources of the pool, not for the performance of a single database.

1. [Reference](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=csharp)
2. [Reference](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview?view=azuresql)

#### Q25. Your photo app hosted in Azure records user operations in a log for historical reference. Records must not be overwritten. Which storage type should you select to host log data?

- [x] append blob
- [ ] table storage
- [ ] page blob
- [ ] block blob

#### Q26. The Kineteco Retail App uses keys for signing and encryption of some data transfers. How should you write your app to invoke keys?

- [ ] Azure CLI
- [x] Azure Portal
- [ ] Azure PowerShell
- [ ] REST API

#### Q27. You need to create a tech support chatbot for Microsoft Teams that interacts with users based on natural language processing (NLP). The bot should be capable of processing differing sentence structures. Which Microsoft Bot Framework component will deliver this functionality?

- [x] LUIS
- [ ] Text to Speech
- [ ] QnA Maker
- [ ] Form Recognizer

#### Q28. You are implementing an application to manage automated warehouse operations for a global retailer. You need to design an enrollment process for IoT devices for production use. Solution requirements are as follows: Register IoT devices in bulk; encrypt all communication between devices and the Azure IoT cloud service; and implement Microsoft recommendations for device security. Which option should you choose?

- [ ] managed identity (shared)
- [x] X.509 certificate
- [ ] managed service identity (per device)
- [ ] SAS key

#### Q29. You are deploying three Azure VMS with an Azure Resource Manager (ARM) template. Which ARM function implements the iteration loop to provision the right number of VMs?

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

#### Q30. The Kineteco web app runs in an Azure Kubernetes Service. You need to monitor feature use and user navigation paths to identify where improvements are needed. What should you do?

- [ ] Install the Analytics agent and configure Azure Monitor for Containers.
- [ ] Install the App Insights Agent on AKS nodes.
- [x] Configure Application Insights cohorts.
- [ ] Add instrumentation to your app to send usage analysis with Application Insights.

#### Q31. Your web app hosted on Azure VMS generates a large number of random (non-sequential) writes. Which storage type should you select for your application?

- [x] page blob
- [ ] block blob
- [ ] table storage
- [ ] queue storage

#### Q32. You are configuring a release pipeline in Azure DevOps. You need to reference several application variables across multiple pipelines at deployment time. How should you store application variables?

- [ ] Store secrets in Azure Key Vault.
- [ ] Store secrets in a configuration file.
- [ ] Configure release variables.
- [x] Configure a variable group.

#### Q33. You have configured the Kineteco Web App to run on Azure Kubernetes Service (AKS). Application resources need to scale to meet spikes in traffic. What should you do? The solution should minimize manual effort and cost.

- [ ] Configure the horizontal pod autoscaler (HPA).
- [ ] Manually scale pod when necessary.
- [ ] Configure burst to Azure Container Instances.
- [x] Do nothing. Pods running on AKS scale up automatically.

#### Q34. You are configuring a release pipeline in Azure DevOps. You need to read secrets from Azure Key Vault during pipeline execution. How should you retrieve application variables?

- [ ] with a community-developed Key Vault task
- [ ] with an ARM template
- [x] all of these answers
- [ ] with an Azure CLI script in a Bash task

#### Q35. You need to update the data within an existing database in Azure SQL with your changes. You want to test this process from your development workstation before incorporating the update into your CI/CD process. Which command will you run to update the schema on the target database?

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

#### Q36. You have a web app hosted in Azure App Service that reads from and writes data to an Azure SQL Database back-end. You need to send email alert when your web app returns any failure HTTP status code (anything except HTTP 200) for a user request. Which solution should you use?

- [x] service map in Azure Monitor
- [ ] application maps in Azure Application Insights
- [ ] availability tests in Azure Application Insights
- [ ] Profiler in Azure Application Insights

#### Q37. Your new release pipeline in Azure DevOps includes a Bash task that runs an Azure CLI script. The Bash task running script fails. The agent setting of the agent job in the release pipeline is pictured below. The solution must minimize cost. What should you change in agent pool settings?

- [ ] Change to a self-hosted agent pool running Ubuntu 16.04 LTS or later.
- [ ] Changed to a hosted pool running Windows 2019.
- [x] Change to a hosted agent pool running Ubuntu 16.04 LTS or later.
- [ ] Change to a self-hosted agent pool running Windows 2019.

#### Q38. You are selecting a cloud messaging solution for your retail mobile app. Requirements for the solution are: Process messages in the order they are received: preserve messages in case of a processing delay; end guarantee message delivery. Which solution should you use?

- [ ] Event Grid
- [x] Service Bus
- [ ] Event Hub
- [ ] Queue Storage

#### Q39. You need to provision a port mapping on the underlying node that allows the application to be accessed directly with the IP address and on the cluster node. Which service type should you provision?

- [ ] LoadBalancer
- [x] NodePort
- [ ] Cluster IP
- [ ] ExternalName

#### Q40. What is the difference between a user-assigned managed identity and a system-assigned managed identity?

- [x] The lifecycle of a user-managed identity is managed separately from the resource.
- [ ] with a user-assigned managed identity, Azure manages the password for you.
- [ ] The lifecycle of a system-managed identity is managed separately from the resource.
- [ ] with a system-assigned managed identity, Azure manages the password for you.

#### Q41. You need to configure user access to Azure DevOps agent pools to meet the following requirements: Use an agent pool when authoring build or release pipelines for the project; view the agent pool and agents of the organization; and use the principle of least privilege. Which role memberships are required for the Azure DevOps organization and the project?

- [ ] Organization: Administrator; Project: Service Account
- [x] Organization: Reader; Project: Service Account
- [ ] Organization: Reader; Project: Administrator
- [ ] Organization: Service Account; Project: Reader

#### Q42. You have created an Azure CLI script for a release pipeline in Azure DevOps. You need to reference the working directory for the running job. Which variable should you reference?

- [x] Agent.WorkFolder
- [ ] Agent.HomeDirectory
- [ ] Agent.BuildDirectory
- [ ] Agent.ToolsDirectory

#### Q43. You are selecting Azure technologies for a new app that will process print jobs in a facility with thousands of printers. A pool of worker processes will send jobs to printer and report results when jobs are complete. Requirements for the solution are: Worker processes will retrieve and process messages as capacity permits; if a worker process or printer fails, a worker process should be able to retrieve message and resume processing; and the solution should maintain a central (server-side) log of messages processed. Which solution should you use?

- [ ] Event Hub
- [ ] Event Grid
- [ ] Service Bus
- [x] Queue Storage

#### Q44. In Azure Key Vault, you can manage access to your application secrets by setting permissions at any level except **\_**.

- [ ] on the secret itself
- [ ] by secret type
- [ ] on the Key Vault instance
- [x] at the Azure Subscription level

#### Q45. Your company hosts a web application that uses Azure SQL Database to store data. You need to implement measures that allow only members of the managers group to see sensitive information. Which two actions should you perform?

- [ ] Implement dynamic data masking and include the managers group.
- [ ] Implement transparent data encryption and include the managers group.
- [x] Implement dynamic data masking and exclude the managers group.
- [ ] Implement transparent data encryption and exclude the managers group.

`Dynamic data masking helps prevent unauthorized access to sensitive data by enabling customers to designate how much of the sensitive data to reveal with minimal impact on the application layer.`
[Reference](https://docs.microsoft.com/en-us/powershell/module/azurerm.sql/new-azurermsqldatabasedatamaskingrule?view=azurermps-6.13.0)

#### Q46. The Kineteco Inventory App uses an Azure SQL Database instance to store application and store inventory data. Store employees report occasional periods where queries in the web interface never return data. You suspect a database issue and need to identify the performance issue as soon as possible. The resource health dashboard reports "No health related issues found." What should you do?

- [ ] Run the troubleshooting wizards under Resource and solve problems.
- [x] Enable Intelligent Insights.
- [ ] Configure App Insights to alert admins when web interface experiences latency.
- [ ] Configure an alert rule to email DBAs when DTU usage hits 100%.

#### Q47. Your web application needs to access files on an Azure Files share. Which option will deliver the highest throughput?

- [x] SMB
- [ ] REST API
- [ ] Storage Explorer
- [ ] NFS

#### Q48. You have source code for a project in a repository on GitHub. You need to migrate source code to a repository in Azure Repos. The solution should minimize effort. Which solution should you recommend?

- [ ] Download the GitHub repository to a Zip file, and then unzip the repository in Azure DevOps.
- [x] From the **Import a Git repository** menu, select **Import**.
- [ ] Create a service connection to the GitHub repository.
- [ ] Create a webhook in GitHub and then trigger it from Azure DevOps.

#### Q49. You need to facilitate user acceptance testing (UAT) on your web application hosted in App Service. Testers must approve changes before they are deployed to production. You should implement support for these requirements with a minimum of cost and complexity. What should you do?

- [ ] Configure an additional App Service instance. In Azure DevOps, enable an approval gate for deployment.
- [ ] Configure an Azure load balancer to redirect traffic to the approved App Service instance.
- [x] Configure an additional deployment slot in the existing App Service instance.
- [ ] Configure an App Service Environment (ASE).

#### Q50. Your microservices application includes a logging component that performs a large number of sequentinal writes. Which type of Azure Storage should you use?

- [ ] Table storage
- [x] append blob
- [ ] page blob
- [ ] block blob

#### Q51. Group policy objects are not being applied to domain controllers because the Default Domain Controllers and Default Domain group policies are corrupt. What can you run in a command prompt to recover them?

- [ ] `dcpromo.exe`
- [x] `dcgpofix.exe`
- [ ] `dcdiagfix.exe`
- [ ] `ntdsutil.exe`

#### Q52. Your JavaScript app hosted in Azure App Service needs to be able to make calls to a remote domain in another Azure region. Which App Service feature do you need to configure?

- [x] `CORS`
- [ ] `deployment slots`
- [ ] `WebJobs`
- [ ] `custom domains`

As described in [Microsoft Docs: Hosting a Restful-API with CORS in AAS](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api): The Answer should be CORS (Cross Origin Ressource Sharing)

#### Q53. Bindings in Azure Function triggers have a direction property that is always \_.

- [ ] parallel
- [ ] out
- [ ] asynchronous
- [x] in

#### Q54. You are selecting a cloud messaging solution for your multimedia news app. The app routes news items to the appropriate services for processing and delivery to subscribers. Requirements for the solution are as follows: Events should be routed to the appropriate service to process event; events must be routed to multiple services when necessary; and only relevant events should be routed to a service for processing. Which solution should you use?

- [x] Event Grid
- [ ] Service Bus
- [ ] Event Hub
- [ ] Queue Storage

**Explanation:** Event Grid is a highly scalable serverless event broker that lets you integrate applications using events. Events are delivered from Event Grid to subscriber destinations such as applications, Azure services, or any endpoint that Event Grid has network access to. The source of these events can be other applications, SaaS services, and Azure services.

[Ref](https://learn.microsoft.com/en-us/azure/event-grid/overview)

#### Q55. You need to create an application in Azure Active Direcotry representing the Kineteco Web App so you can assign directory permission to the app. To create the application identity, which command will you run?

- [ ] `bash az ad app permission grant ...
- [ ] `bash az ad app credential create ...
- [x] `bash az ad app create ...
- [ ] `bash az ad app permission ass ...

[Ref](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest)

#### Q56. Which type of Azure snapshot works by snapshotting the differences between the virtual machine and the current state?

- [ ] full
- [ ] delta
- [ ] non-redundant
- [x] incremental

#### Q57. Which PowerShell commandlet connects and authenticates to the Azure portal?

- [ ] Login-AzTenant
- [ ] Login-AzPortal
- [ ] Auth-Az
- [x] Connect-AzAccount

#### Q58. Which hybrid connection option to Azure Virtual Desktop offers the highest bandwidth and best performance?

- [x] Azure ExpressRoute
- [ ] RDP Shortpath
- [ ] Site-to-Site VPN
- [ ] Point-to-Site VPN

#### Q59. In Azure Virtual Desktop, you can **\_** the storage accounts associated with FSLogix to enable you to control access using Active Directory Domain Services.

- [x] domain join
- [ ] profile
- [ ] VPN connect
- [ ] join integrate

#### Q60. Which storage solution for FSLogix in Azure Virtual Desktop is the highest-performing storage solution in the cloud today?

- [ ] Windows Storage Spaces Direct File Server Cluster
- [ ] Azure Files
- [x] Azure NetApp Files
- [ ] Avere vFXT for Azure

#### Q61. In an Azure Pipeline, what type of wildcard is used to stand in for a single character?

- [ ] `*`
- [ ] `#`
- [x] `?`
- [ ] `&`

#### Q62. To execute your pipeline in Azure DevOps, you will need to use **\*\***\_**\*\***.

- [ ] gates
- [x] agents
- [ ] packages
- [ ] variables

#### Q63. Which of the following is true if parallelism is desired in Azure Pipelines?

- [ ] No more than one build agent can be used.
- [x] More than one build agent is required.
- [ ] Complexity is reduced with parallelism.
- [ ] A maximum number of build agents constrains it.

#### Q64. In an Azure Pipeline, a build agent is a piece of software that runs a series of tasks, called a \***\*\_\_\_\*\***, on a machine.

- [ ] String
- [ ] Circuit
- [x] Job
- [ ] Commit

#### Q65. In Azure Pipelines, if a build has four jobs that can be run concurrently, but only three agents are available, what will happen?

- [x] Only three jobs will run in parallel at one given time.
- [ ] The build will override one of the jobs so that it can run.
- [ ] The build will forfeit and not run at all.
- [ ] The build will wait until another agent becomes available.

#### Q66. Which type of Azure Web Application Firewall log tracks requests coming through the firewall policy while in detection or prevention mode?

- [ ] Activity Log
- [ ] Performance Resource Log
- [ ] Access Resource Log
- [x] Firewall Resource Log

#### Q67. Which of the following options is not a possible rule action for Azure Web Application Firewall policies for Application Gateway?

- [x] deny
- [ ] log
- [ ] allow
- [ ] block

#### Q68. Which of the following statements about Azure Web Application Firewall policies for Application Gateway is true?

- [ ] Each policy can be applied to only one target.
- [x] Policies can be applied globally to the Application Gateway at the site hosted by the gateway.
- [ ] Managed rules have a priority over custom rules.
- [ ] You can create a maximum of 100 policies.

#### Q69. Which of the following services is not a service supported by Azure Web Application Firewall?

- [ ] Azure Application Gateway
- [ ] Azure Content Delivery Network
- [ ] Azure Front Door
- [x] Azure API Management

#### Q70. Azure **\_** is a globally scalable entry point for web applications hosted in Azure.

- [ ] Content Delivery Network
- [x] Front Door
- [ ] Application Gateway
- [ ] API Management

#### Q71. You need to create an application in Azure Active Directory representing the Kineteco Web App so you can assign directory permissions to the app. To create the application identity, which command will you run?

- [ ] appName="KinetecoWebApp"

      az ad app permission grant -display-name $appName \
          --homepage "http://localhost/$appName" \

  --identifier-uris [http://localhost/$appName](http://localhost/$appName)

- [x] appName="KinetecoWebApp"

      az ad app create -display-name $appName \
          --homepage "http://localhost/$appName" \
          --identifier-uris [http://localhost/$appName](http://localhost/$appName)

- [ ] appName="KinetecoWebApp"

      az ad app credential create -display-name $appName \
          --homepage "http://localhost/$appName" \
          --identifier-uris [http://localhost/$appName](http://localhost/$appName)

- [ ] appName="KinetecoWebApp"

      az ad app permission add -display-name $appName \
          --homepage "http://localhost/$appName" \
          --identifier-uris [http://localhost/$appName](http://localhost/$appName)

#### Q72. In the Azure Service Bus, what is the purpose of the dead letter queue?

- [ ] It is used to ensure that the Azure Bus Service queue can deliver messages in a First-In-First-Out manner.
- [ ] It can be used for load balancing queues.
- [ ] It is a duplicate queue used as a backup queue.
- [x] It is used to store messages which could not be delivered.

[Ref](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues)

#### Q73. You have a WCF application on-premises behind a firewall, and you need to expose it to an Azure web role. Which of the following services would be the best solution?

- [ ] Azure Data Management Gateway
- [ ] Service Bus Topics
- [ ] Azure On-Premises Data Gateway
- [x] WCF Relay

[Ref](https://docs.microsoft.com/en-us/azure/service-bus-relay/relay-hybrid-connections-dotnet-get-started)

#### Q74. When using Azure Service Bus, a single message sent to a topic can be received by multiple subscriptions. Is this true?

- [x] Yes
- [ ] Yes, if the message metadata allows it
- [ ] No
- [ ] No, the first subscription to process it gets it

[Ref](https://azure.microsoft.com/en-us/documentation/articles/service-bus-fundamentals-hybrid-solutions/#topics)

#### Q75. You're designing a solution that needs to be low cost and to expose a WCF application that lives on-premises to a Web API that lives in Azure. Which of the following will be added to your design?

- [ ] A point-to-site VPN
- [ ] A site-to-site VPN
- [x] WCF Relay
- [ ] Self-Hosted Integration Runtime

[Ref](https://docs.microsoft.com/en-us/azure/azure-relay/service-bus-dotnet-hybrid-app-using-service-bus-relay)

#### Q76. What are the core messaging entities in Azure Service Bus?

- [ ] Queues, transactions, and messages
- [x] Queues, topics, and subscriptions
- [ ] Topics, subscriptions, and message sessions
- [ ] Queues, message locks, and transactions

[Ref](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)

#### Q77. This question requires that you evaluate the underlined text to determine if it is correct.

An organization that hosts its infrastructure in a private cloud can close its data center.
Instructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If
the statement is incorrect, select the answer choice that makes the statement correct.

- [ ] No change is needed.
- [ ] in a hybrid cloud
- [x] in the public cloud
- [ ] on a Hyper-V host

Explanation/Reference:
Explanation:
A private cloud is hosted in your datacenter. Therefore, you cannot close your datacenter if you are using a
private cloud.
A public cloud is hosted externally, for example, in Microsoft Azure. An organization that hosts its
infrastructure in a public cloud can close its data center.
Public cloud is the most common deployment model. In this case, you have no local hardware to manage or
keep up-to-date – everything runs on your cloud provider's hardware.
Microsoft Azure is an example of a public cloud provider.
In a private cloud, you create a cloud environment in your own datacenter and provide self-service access to
compute resources to users in your organization. This offers a simulation of a public cloud to your users, but
you remain completely responsible for the purchase and maintenance of the hardware and software services
you provide.

[Ref](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest)

#### Q78.What are two characteristics of the public cloud? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- [ ] dedicated hardware
- [ ] limited storage
- [x] metered pricing
- [x] self-service management
- [ ] unsecured connections

Explanation/Reference:
Explanation:
With the public cloud, you get pay-as-you-go pricing – you pay only for what you use, no CapEx costs.
With the public cloud, you have self-service management. You are responsible for the deployment and
configuration of the cloud resources such as virtual machines or web sites. The underlying hardware that
hosts the cloud resources is managed by the cloud provider.
Incorrect Answers:
A: You don’t have dedicated hardware. The underlying hardware is shared so you could have multiple
customers using cloud resources hosted on the same physical hardware.
B: Connections to the public cloud are secure.
C: Storage is not limited. You can have as much storage as you like.

[Ref](https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models)

#### Q79. Your company hosts an accounting application named App1 that is used by all the customers of the

company.
App1 has low usage during the first three weeks of each month and very high usage during the last week of
each month.
Which benefit of Azure Cloud Services supports cost management for this type of usage pattern?

- [ ] high availabilit
- [ ] high latency
- [x] elasticity
- [ ] load balancing

Explanation/Reference:
Explanation:
Elasticity in this case is the ability to provide additional compute resource when needed and reduce the
compute resource when not needed to reduce costs. Autoscaling is an example of elasticity.
Elastic computing is the ability to quickly expand or decrease computer processing, memory and storage
resources to meet changing demands without worrying about capacity planning and engineering for peak
usage. Typically controlled by system monitoring tools, elastic computing matches the amount of resources
allocated to the amount of resources actually needed without disrupting operations. With cloud elasticity, a
company avoids paying for unused capacity or idle resources and doesn’t have to worry about investing in
the purchase or maintenance of additional resources and equipment.

[Ref](https://azure.microsoft.com/en-gb/overview/what-is-elastic-computing/)

#### Q80. You plan to migrate a web application to Azure. The web application is accessed by external users.

You need to recommend a cloud deployment solution to minimize the amount of administrative effort used to
manage the web application.
What should you include in the recommendation?

- [ ] Software as a Service (SaaS)
- [x] Platform as a Service (PaaS)
- [ ] Infrastructure as a Service (IaaS)
- [ ] Database as a Service (DaaS)

Explanation/Reference:
Explanation:
Azure App Service is a platform-as-a-service (PaaS) offering that lets you create web and mobile apps for
any platform or device and connect to data anywhere, in the cloud or on-premises. App Service includes the
web and mobile capabilities that were previously delivered separately as Azure Websites and Azure Mobile
Services.

[Ref](https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-app-services)

#### Q81. You have an on-premises network that contains 100 servers.

You need to recommend a solution that provides additional resources to your users. The solution must
minimize capital and operational expenditure costs.
What should you include in the recommendation?

- [ ] a complete migration to the public cloud
- [ ] an additional data center
- [ ] a private cloud
- [x] a hybrid cloud

Explanation/Reference:
Explanation:
A hybrid cloud is a combination of a private cloud and a public cloud.
Capital expenditure is the spending of money up-front for infrastructure such as new servers.
With a hybrid cloud, you can continue to use the on-premises servers while adding new servers in the public
cloud (Azure for example). Adding new servers in Azure minimizes the capital expenditure costs as you are
not paying for new servers as you would if you deployed new server on-premises.
Incorrect Answers:
A: A complete migration of 100 servers to the public cloud would involve a lot of operational expenditure (the
cost of migrating all the servers).
B: An additional data center would involve a lot of capital expenditure (the cost of the new infrastructure).
C: A private cloud is hosted on on-premises servers to this would involve a lot of capital expenditure (the cost
of the new infrastructure to host the private cloud

[Ref](https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models)

#### Q82. You plan to migrate several servers from an on-premises network to Azure.

What is an advantage of using a public cloud service for the servers over an on-premises network

- [ ] The public cloud is owned by the public, NOT a private corporation
- [ ] The public cloud is a crowd-sourcing solution that provides corporations with the ability to enhance the cloud
- [x] The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud
- [ ] All public cloud resources can be freely accessed by every member of the public

Explanation/Reference:
Explanation:
The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the
cloud. The hardware resources (servers, infrastructure etc.) are managed by the cloud provider. Multiple
companies create resources such as virtual machines and virtual networks on the hardware resources.
Incorrect Answers:
A: The public cloud is not owned by the public. In the case of Microsoft Azure, the cloud is owned by
Microsoft.
B: The public cloud is a not crowd-sourcing solution. In the case of Microsoft Azure, the cloud is owned by Microsoft.
C: It is not true that public cloud resources can be freely accessed by every member of the public. You pay for a cloud subscription and create accounts for your users to access your cloud resources. No one can
access your cloud resources until you create user accounts and provide the appropriate access permissions.

#### Q83. You have 1,000 virtual machines hosted on the Hyper-V hosts in a data center.

You plan to migrate all the virtual machines to an Azure pay-as-you-go subscription.
You need to identify which expenditure model to use for the planned Azure solution.
Which expenditure model should you identify?

- [x] operational
- [ ] elastic
- [ ] capital
- [ ] scalable

Explanation/Reference:
Explanation:
One of the major changes that you will face when you move from on-premises cloud to the public cloud is the
switch from capital expenditure (buying hardware) to operating expenditure (paying for service as you use it).
This switch also requires more careful management of your costs. The benefit of the cloud is that you can
fundamentally and positively affect the cost of a service you use by merely shutting down or resizing it when it's not needed.

[Ref](https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold)

#### Q84. Your company has an on-premises network that contains multiple servers.

The company plans to reduce the following administrative responsibilities of network administrators:
Backing up application data
Replacing failed server hardware
Managing physical server security
Updating server operating systems
Managing permissions to shared documents
The company plans to migrate several servers to Azure virtual machines.
You need to identify which administrative responsibilities will be eliminated after the planned migration.
Which two responsibilities should you identify? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

- [x] Replacing failed server hardware
- [ ] Backing up application data
- [x] Updating server operating systems
- [ ] Managing permissions to shared documents

Explanation/Reference:
Explanation:
Azure virtual machines run on Hyper-V physical servers. The physical servers are owned and managed by
Microsoft. As an Azure customer, you have no access to the physical servers. Microsoft manage the
replacement of failed server hardware and the security of the physical servers so you don’t need to.
Incorrect Answers:
B: Microsoft have no control over the applications you run on the virtual machines. Therefore, it is your
responsibility to ensure that application data is backed up.
D: Microsoft do not manage the operating systems you run on the virtual machines. Therefore, it is your
responsibility to ensure that the operating systems are updated.
E: Microsoft have no control over the shared folders you host on the virtual machines. Therefore, it is your responsibility to ensure that folder permissions are configured appropriately.

#### Q85. A team of developers at your company plans to deploy, and then remove, 50 virtual machines each week. All the virtual machines are configured by using Azure Resource Manager templates.

You need to recommend which Azure service will minimize the administrative effort required to deploy and
remove the virtual machines.
What should you recommend?

- [ ] Azure Reserved Virtual Machine (VM) Instances
- [x] Azure DevTest Labs
- [ ] Azure virtual machine scale sets
- [ ] Microsoft Managed Desktop

Explanation/Reference:
Explanation:
DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates.
By using DevTest Labs, you can test the latest versions of your applications by doing the following tasks:
Quickly provision Windows and Linux environments by using reusable templates and artifacts.
Easily integrate your deployment pipeline with DevTest Labs to provision on-demand environments.
Scale up your load testing by provisioning multiple test agents and create pre-provisioned environments for training and demos.

[Ref](https://docs.microsoft.com/en-us/azure/lab-services/devtest-lab-overview)

#### Q86. You use Azure Table storage to store customer information for an application. The data contains customer details and is partitioned by last name. You need to

create a query that returns all customers with the last name Smith. Which code segment should you use?

- [ ] TableQuery.GenerateFilterCondition("PartitionKey", Equals, "Smith")
- [ ] TableQuery.GenerateFilterCondition("LastName", Equals, "Smith")
- [x] TableQuery.GenerateFilterCondition("PartitionKey", QueryComparisons.Equal, "Smith")
- [ ] TableQuery.GenerateFilterCondition("LastName", QueryComparisons.Equal, "Smith")

Explanation:
Retrieve all entities in a partition. The following code example specifies a filter for entities where 'Smith' is the partition key. This example prints the fields of each
entity in the query results to the console.
Construct the query operation for all customer entities where PartitionKey="Smith". TableQuery<CustomerEntity> query = new
TableQuery<CustomerEntity>().Where(TableQuery.GenerateFilterCondition("PartitionKey",
QueryComparisons.Equal, "Smith"));

[Ref](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-dotnet)

#### Q87.You develop an app that allows users to upload photos and videos to Azure storage. The app uses a storage REST API call to upload the media to a blob storage

account named Account1. You have blob storage containers named Container1 and Container2. Uploading of videos occurs on an irregular basis.
You need to copy specific blobs from Container1 to Container2 in real time when specific requirements are met, excluding backup blob copies.
What should you do?

- [ ] Download the blob to a virtual machine and then upload the blob to Container2.
- [x] Run the Azure PowerShell command Start-AzureStorageBlobCopy
- [ ] Copy blobs to Container2 by using the Put Blob operation of the Blob Service REST API.
- [ ] Use AzCopy with the Snapshot switch blobs to Container2.

Explanation:
The Start-AzureStorageBlobCopy cmdlet starts to copy a blob. Example 1: Copy a named blob
C:\PS>Start-AzureStorageBlobCopy -SrcBlob "ContosoPlanning2015" -DestContainer "ContosoArchives"
-SrcContainer "ContosoUploads"
This command starts the copy operation of the blob named ContosoPlanning2015 from the container named ContosoUploads to the container named
ContosoArchives.

[Ref](https://docs.microsoft.com/en-us/powershell/module/azure.storage/start-azurestorageblobcopy?view=azurermps)

#### Q88. You are a developer for a SaaS company that offers many web services. All web services for the company must meet the following requirements:

Use API Management to access the services Use OpenID Connect for authentication Prevent anonymous usage A recent security audit found that several web services can be called without any authentication.
Which API Management policy should you implement?

- [ ] jsonp
- [ ] authentication-certificate
- [ ] check-header
- [x] validate-jwt

[Ref](https://docs.microsoft.com/en-us/azure/api-management/api-management-howto-protect-backend-with-aad)

#### Q89.You are developing an Azure Cosmos DB solution by using the Azure Cosmos DB SQL API. The data includes millions of documents. Each document may

contain hundreds of properties. The properties of the documents do not contain distinct values for partitioning. Azure Cosmos DB must scale individual containers in the database to meet the
performance needs of the application by spreading the workload evenly across all partitions over time.
You need to select a partition key.
Which two partition keys can you use? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

- [x] a concatenation of multiple property values with a random suffix appended
- [ ] a single property value that does not appear frequently in the documents
- [x] a hash suffix appended to a property value
- [ ] a value containing the collection name
- [ ] a single property value that appears frequently in the documents

Explanation:
You can form a partition key by concatenating multiple property values into a single artificial partitionKey property. These keys are referred to as synthetic keys.
Another possible strategy to distribute the workload more evenly is to append a random number at the end of the partition key value. When you distribute items in
this way, you can perform parallel write operations across partitions.
Note: It's the best practice to have a partition key with many distinct values, such as hundreds or thousands. The goal is to distribute your data and workload
evenly across the items associated with these partition key values. If such a property doesn’t exist in your data, you can construct a synthetic partition key.

[Ref](https://docs.microsoft.com/en-us/azure/cosmos-db/synthetic-partition-keys)

#### Q90.You are developing an ASP.NET Core Web API web service. The web service uses Azure Application Insights for all telemetry and dependency tracking. The web

service reads and writes data to a database other than Microsoft SQL Server.
You need to ensure that dependency tracking works for calls to the third-party database.
Which two Dependency Telemetry properties should you store in the database? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

- [x] Telemetry.Context.Operation.Id
- [ ] Tetemetry.Context.Cloud.Rolelnstance
- [x] Telemetry.Id
- [ ] Telemetry.ContextSession.Id

[Ref](https://docs.microsoft.com/en-us/azure/azure-monitor/app/custom-operations-tracking)

#### Q91. You are preparing to deploy an ASP.NET Core website to an Azure Web App from a GitHub repository. The website includes static content generated by a script.

You plan to use the Azure Web App continuous deployment feature.
You need to run the static generation script before the website starts serving traffic.
What are two possible ways to achieve this goal? Each correct answer presents a complete solution. NOTE: Each correct selection is worth one point

- [ ] Create a file named .deployment in the root of the repository that calls a script which generates the static content and deploys the website
- [ ] Add a PreBuild target in the websites csproj project file that runs the static content generation script
- [ ] Create a file named run.cmd in the folder /run that calls a script which generates the static content and deploys the website.
- [ ] Add the path to the static content generation tool to WEBSITE_RUN_FROM_PACKAGE setting in the host.json file.

Explanation:
A: To customize your deployment, include a .deployment file in the repository root.
You just need to add a file to the root of your repository with the name .deployment and the content: [config]
command = YOUR COMMAND TO RUN FOR DEPLOYMENT
this command can be just running a script (batch file) that has all that is required for your deployment, like copying files from the repository to the web root directory
for example.
D: In Azure, you can run your functions directly from a deployment package file in your function app. The other option is to deploy your files in the
d:\home\site\wwwroot directory of your function app (see A above).
To enable your function app to run from a package, you just add a WEBSITE_RUN_FROM_PACKAGE setting to your function app settings.
Note: The host.json metadata file contains global configuration options that affect all functions for a function app.

[Ref](https://github.com/projectkudu/kudu/wiki/Custom-Deployment-Script)
[Ref](https://docs.microsoft.com/bs-latn-ba/azure/azure-functions/run-functions-from-deployment-package)

#### Q92. You provide an Azure API Management managed web service lo clients. The back end web service implements HTTP Strict Transport Security (HSTS).

Every request to the backend service must include a valid HTTP authorization header. You need to configure the Azure API Management instance with an
authentication policy. Which two policies can you uses? Each correct answer presents a complete solution NOTE: Each correct selection is worth one point.

- [x] Certificate Authentication
- [ ] Basic Authentication
- [x] OAuth Client Credential Grant
- [ ] Digest Authentication

#### Q93.A company is implementing a publish-subscribe (Pub/Sub) messaging component by using Azure Service Bus. You are developing the first subscription

application.
In the Azure portal you see that messages are being sent to the subscription for each topic. You create and initialize a subscription client object by supplying the
correct details, but the subscription application is still not consuming the messages.
You need to complete the source code of the subscription client What should you do

- [ ] await subscriptionClient.CloseAsync();
- [ ] await subscriptionClient.AddRuleAsync(new RuleDescription(RuleDescription.DefaultRuleName, new TrueFilter()));
- [x] subscriptionClient.RegisterMessageHandler(ProcessMessagesAsync, messageHandlerOptions);
- [ ] subscriptionClient = new SubscriptionClient(ServiceBusConnectionString, TopicName, SubscriptionName);

Explanation:
Using topic client, call RegisterMessageHandler which is used to receive messages continuously from the entity. It registers a message handler and begins a new
thread to receive messages. This handler is waited on every time a new message is received by the receiver.
subscriptionClient.RegisterMessageHandler(ReceiveMessagesAsync, messageHandlerOptions);

[Ref](https://www.c-sharpcorner.com/article/azure-service-bus-topic-and-subscription-pub-sub/)

#### Q94. You develop a gateway solution for a public facing news API. The news API back end is implemented as a RESTful service and uses an OpenAPI specification.

You need to ensure that you can access the news API by using an Azure API Management service instance. Which Azure PowerShell command should you run?

- [ ] Import-AzureRmApiManagementApi –Context $ApiMgmtContext –SpecificationFormat "Swagger" -SpecificationPath $SwaggerPath –Path $Path
- [ ] New-AzureRmApiManagementBackend -Context $ApiMgmtContext -Url $Url -Protocol http
- [ ] New-AzureRmApiManagement –ResourceGroupName $ResourceGroup –Name $Name – Location $Location –Organization $Org –AdminEmail $AdminEmail
- [x] New-AzureRmApiManagementBackendProxy –Url $ApiUrl

Explanation:
New-AzureRmApiManagementBackendProxy creates a new Backend Proxy Object which can be piped when creating a new Backend entity.
Example: Create a Backend Proxy In-Memory Object
PS C:\>$secpassword = ConvertTo-SecureString "PlainTextPassword" -AsPlainText -Force
PS C:\>$proxyCreds = New-Object System.Management.Automation.PSCredential ("foo", $secpassword) PS C:\>$credential = NewAzureRmApiManagementBackendProxy
-ProxyCredential $proxyCred
PS C:\>$apimContext = New-AzureRmApiManagementContext -ResourceGroupName "Api-Default-WestUS" -ServiceName "contoso"
PS C:\>$backend = New-AzureRmApiManagementBackend -Context $apimContext -BackendId 123 Protocol http -Title
"first backend" -SkipCertificateChainValidation $true
-Proxy $credential -Description "backend with proxy server"
Creates a Backend Proxy Object and sets up Backend

#### Q95. You are developing a mobile instant messaging app for a company. The mobile app must meet the following requirements:

• Support offline data sync.
• Update the latest messages during normal sync cycles. You need to implement Offline Data Sync.
Which two actions should you perform? Each conn I answer presents part of the solution. NOTE: Each correct selection is worth one point.

- [ ] Retrieve records from Offline Data Sync on every call to the PullAsync method.
- [x] Retrieve records from Offline Data Sync using an Incremental Sync.
- [ ] Push records to Offline Data Sync using an Incremental Sync.
- [ ] . Return the updatedAt column from the Mobile Service Backend and implement sorting by using the column.
- [x] Return the updatedAt column from the Mobile Service Backend and implement sorting by the message id.

[Ref](https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-offline-data-sync)

#### Q96.You develop a website. You plan to host the website in Azure. You expect the website to experience high traffic volumes after it is published. You must ensure tha the website remains available and responsive while minimizing cost. You need to deploy the website. What should you do?

- [ ] Deploy the website to an App Service that uses the Shared service tie
- [ ] Configure the App Service plan to automatically scale when the CPU load is high.
- [x] Deploy the website to a virtual machin
- [ ] . Configure the virtual machine to automatically scale when the CPU load is high.

Explanation:
Windows Azure Web Sites (WAWS) offers 3 modes: Standard, Free, and Shared.
Standard mode carries an enterprise-grade SLA (Service Level Agreement) of 99.9% monthly, even for sites with just one instance.
Standard mode runs on dedicated instances, making it different from the other ways to buy Windows Azure Web Sites.

#### Q97. You develop a serverless application using several Azure Functions. These functions connect to data from within the code.

You want to configure tracing for an Azure Function App project. You need to change configuration settings in the hostjson file. Which tool should you use?

- [x] Azure porta
- [ ] Azure PowerShell
- [ ] Azure Functions Core Tools (Azure CLI)
- [ ] Visual Studio

Explanation:
The function editor built into the Azure portal lets you update the function.json file and the code file for a function. The host.json file, which contains some runtimespecific configurations, is in the root folder of the function app

[Ref](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference#fileupdate)

#### Q98. You are developing an internal website for employees to view sensitive data. The website uses Azure Active Directory (AAD) for authentication. You need to

implement multifactor authentication for the website.
What should you do? Each correct answer presents part of the solution. NOTE; Each correct selection is worth one point

- [x] In Azure AD, create a new conditional access policy.
- [ ] In Azure AD, enable application proxy.
- [ ] Configure the website to use Azure AD B2C.
- [ ] In Azure AD conditional access, enable the baseline policy.
- [x] Upgrade to Azure AD Premium.

[Ref](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-getstarted)

#### Q99. You must implement Application Insights instrumentation capabilities utilizing the Azure Mobile Apps SDK to provide meaningful analysis of user interactions with a

mobile app. You need to capture the data required to implement the Usage Analytics feature of Application Insights. Which three data values should you capture? Each correct
answer presents part of the solution
NOTE: Each correct selection is worth one point.

- [x] Trace
- [ ] Session Id
- [ ] Exception
- [x] User Id
- [x] Events

Explanation:
Application Insights is a service for monitoring the performance and usage of your apps. This module allows you to send telemetry of various kinds (events, traces,
etc.) to the Application Insights service where your data can be visualized in the Azure Portal. Application Insights manages the ID of a session for you.

[Ref](https://github.com/microsoft/ApplicationInsights-Android)

#### Q100. You develop Azure solutions.

You must connect to a No-SQL globally-distributed database by using the .NET API. You need to create an object to configure and execute requests in the
database. Which code segment should you use?

- [ ] new Container(EndpointUri, PrimaryKey)
- [ ] new Database(Endpoint, PrimaryKey);
- [x] new CosmosClient(EndpointUri, PrimaryKey);

Explanation:
Example:
// Create a new instance of the Cosmos Client
this.cosmosClient = new CosmosClient(EndpointUri, PrimaryKey)
//ADD THIS PART TO YOUR CODE
await this.CreateDatabaseAsync();

[Ref](https://docs.microsoft.com/en-us/azure/cosmos-db/sql-api-get-started)

#### Q101. Your company plans to migrate all its data and resources to Azure. The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure. You need to deploy an Azure environment that meets the company's migration plan. What should you create?

- [ ] Azure virtual machines, Azure SQL databases, and Azure Storage accounts.
- [ ] Azure storage accounts and web server in Azure virtual machines.
- [ ] an Azure App Service and Azure virtual machines that have Microsoft SQL Server installed.
- [x] an Azure App Service and Azure SQL databases.
      [Ref](https://azurecharts.com/overview/?f=paas)

### Q102. What is the first stage in the Microsoft Cloud Adoption Framework for Azure?

- [ ] Adopt the cloud.
- [ ] Make a plan.
- [x] Define your strategy.
- [ ] Ready your organization.
      [Ref](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/overview)

### Q103. You need to identify the type of failure for which an Azure Availability Zone can be used to protect access to Azure services. What should you identify?

- [ ] a physical server failure
- [x] an Azure data center failure
- [ ] an Azure region failure
- [ ] a storage failure
      [Ref](https://docs.microsoft.com/en-us/azure/virtual-machines/availability)
