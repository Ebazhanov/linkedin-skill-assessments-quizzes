## Microsoft Azure AZ-900 Questions & Answers

#### Q1. This question requires that you evaluate the underlined text to determine if it is correct.
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



#### Q2.What are two characteristics of the public cloud? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

- [ ] dedicated hardware 
- [ ] limited storage 
- [X] metered pricing
- [X] self-service management
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



#### Q3. Your company hosts an accounting application named App1 that is used by all the customers of the
company. 
App1 has low usage during the first three weeks of each month and very high usage during the last week of
each month. 
Which benefit of Azure Cloud Services supports cost management for this type of usage pattern?

- [ ] high availabilit
- [ ]  high latency
- [X] elasticity
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



#### Q4. You plan to migrate a web application to Azure. The web application is accessed by external users. 
You need to recommend a cloud deployment solution to minimize the amount of administrative effort used to
manage the web application. 
What should you include in the recommendation?

- [ ]  Software as a Service (SaaS)
- [x]  Platform as a Service (PaaS)
- [ ] Infrastructure as a Service (IaaS)
- [ ]  Database as a Service (DaaS)

Explanation/Reference:
Explanation:
Azure App Service is a platform-as-a-service (PaaS) offering that lets you create web and mobile apps for
any platform or device and connect to data anywhere, in the cloud or on-premises. App Service includes the
web and mobile capabilities that were previously delivered separately as Azure Websites and Azure Mobile
Services.

[Ref](https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-app-services)


#### Q5. You have an on-premises network that contains 100 servers. 
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



#### Q6. You plan to migrate several servers from an on-premises network to Azure. 
What is an advantage of using a public cloud service for the servers over an on-premises network


- [ ] The public cloud is owned by the public, NOT a private corporation
- [ ] The public cloud is a crowd-sourcing solution that provides corporations with the ability to enhance the cloud
- [X] The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud
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



#### Q7. You have 1,000 virtual machines hosted on the Hyper-V hosts in a data center.
You plan to migrate all the virtual machines to an Azure pay-as-you-go subscription.
You need to identify which expenditure model to use for the planned Azure solution.
Which expenditure model should you identify?

- [X] operational
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


#### Q8. Your company has an on-premises network that contains multiple servers.
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

- [X] Replacing failed server hardware
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



#### Q9. A team of developers at your company plans to deploy, and then remove, 50 virtual machines each week. All the virtual machines are configured by using Azure Resource Manager templates.
You need to recommend which Azure service will minimize the administrative effort required to deploy and
remove the virtual machines. 
What should you recommend?

- [ ] Azure Reserved Virtual Machine (VM) Instances
- [X] Azure DevTest Labs
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

