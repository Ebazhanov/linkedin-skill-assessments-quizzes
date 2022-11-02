## Google Cloud Platform (GCP)

#### Q1. You want to schedule a cron job to send a message to a Cloud Pub/Sub topic hourly. What do you do?

- [ ] Create a Cloud Function with a target of HTTP
- [ ] Create a Cloud Scheduler job with a target of HTTP
- [x] Create a Cloud Function with a target of Cloud Pub/Sub
- [ ] Create a Cloud Scheduler job with a target of Cloud Pub/Sub

#### Q2. You want to set up a managed Apache Spark cluster. Which service do you configure?

- [ ] Cloud Dataprep
- [ ] Cloud Composer
- [ ] Cloud Dataflow
- [x] Cloud Dataproc

#### Q3. GCP Organizations are not available in your GCP project. What type of account are you using?

- [ ] Temporary
- [x] Free Tier
- [ ] Local
- [ ] Organizational

**Note:** Free trial doesn't have the organizations.

#### Q4. What feature do you need to enable to support load balancing and autoscaling managed instance groups for Compute Engine?

- [ ] metadata
- [ ] security scans
- [ ] network endpoint groups
- [x] health checks

#### Q5. You are designing an application that will send messages with the MQTT protocol. What service should you use?

- [ ] BigQuery
- [x] Cloud Pub/Sub
- [ ] IoT Broker
- [ ] Bigtable

#### Q6. You want to configure services to host a mobile application that uses TensorFlow Lite models. Which services should you use?

- [ ] Cloud Functions and ML Kit
- [ ] Firebase and AI Platform jobs
- [x] Firebase and ML Kit
- [ ] Cloud Functions and AI Platform jobs

[reference link](https://firebase.google.com/docs/ml-kit/android/use-custom-models)

#### Q7. You need to deploy Redis with unique persistent identities and stable hostnames on GKE. What type of deployment object do you use?

- [ ] GCP deployment
- [x] YAML configuration file
- [ ] Python nested template
- [ ] stateful set

#### Q8. You want to try out a machine-learning TensorFlow example notebook with the fewest configuration steps on GCP. What do you do?

- [ ] Upload the notebook to Google Colaboratory. Set the hardware accelerator to use GPU.
- [x] Create a notebook instance with TPU. Upload the notebook to the instance.
- [ ] Create a notebook instance with GPU. Upload the notebook to the instance.
- [ ] Upload the notebook to Google Colaboratory. Set the hardware accelerator to use TPU.

#### Q9. You need to configure a data retention policy for a Cloud Storage bucket to govern how long objects in the bucket must be retained. What feature do you enable?

- [ ] Requester Pays
- [x] Bucket Lock
- [ ] Bucket Policy Only
- [ ] Encryption Type

#### Q10. To be able to configure an existing Cloud Function, what information should you review and from which location?

- [ ] execution time in Cloud Storage logs
- [ ] execution time in Stackdriver logs
- [x] text payload in Stackdriver logs
- [ ] text payload in Cloud Storage logs

#### Q11. You need to execute a "lift and shift" move with as few steps as possible. Which items do you need to create to accomplish this task, listed in the correct order of creation?

- [ ] Create a VPN from GCP to your corporate network. 2. Create a GCP network for the project. 3. Create the VM instances to support the application.
- [x] Create a GCP network for the project. 2. Create a VPN from your corporate network to GCP. 3. Create the VM instances to support the application.
- [ ] Create a GCP network for the project. 2. Create a VPN from GCP to your corporate network. 3. Create the VM instances to support the application.
- [ ] Create a VPN from your corporate network to GCP. 2. Create a GCP network for the project. 3. Create the VM instances to support the application.

[refernce link](https://cloud.google.com/files/Lift-and-Shift-onto-Google-Cloud.pdf)

#### Q12. You are concerned about data egress charges for files in a Cloud Storage bucket. What configuration change should you make?

- [ ] Enable Requester Pays on the project.
- [ ] Enable Requester Pays on the bucket.
- [x] Change the default storage class from multi-regional to regional.
- [ ] Change the default storage class from regional to multi-regional.

#### Q13. You need to troubleshoot an Android app that uses Cloud Storage. Where do you look for logs?

- [ ] Firebase Crashlytics
- [x] Firebase Crashlytics and Stackdriver
- [ ] Firebase Testlab and Stackdriver
- [ ] Stackdriver

#### Q14. You want to configure services to be able to perform a regular interactive query of Google AdWords data. What should you do?

- [ ] Plan to use BigQuery. Create a BigQuery data set to hold the data.
- [ ] Plan to use Cloud SQL. Enable Cloud SQL Transfer Data API.
- [ ] Plan to use Cloud SQL. Create a Cloud SQL Database to hold the data.
- [x] Plan to user BigQuery. Enable BigQuery Transfer Data API.

#### Q15. You want to use GCP-preferred base container images. Where can your users find these images?

- [ ] Docker Hub
- [ ] Compute Engine base images
- [x] GCP Marketplace
- [ ] Google Kubernetes Engine base images

#### Q16. You want to set a notification for service spend in GCP. What do you do, and who will be notified?

- [x] Use the GCP Billing console Budgets section to set a billing alert. The billing admin will be notified if the alert threshold is exceeded.
- [ ] Use the GCP Billing console Budgets section to set a billing alert. The organizational admin will be notified if the alert threshold is exceeded.
- [ ] Use the GCP Organizational console Budgets section to set a billing alert. The project admin will be notified if the alert threshold is exceeded.
- [ ] Use the GCP Organizational console Budgets section to set a billing alert. The organizational admin will be notified if the alert threshold is exceeded.

#### Q17. Cloud SQL supports which two relational databases?

- [ ] Redis and Oracle
- [ ] MySQL and Oracle
- [ ] Redis and PostgreSQL
- [x] MySQL and PostgreSQL

#### Q18. You want to quickly test a single Docker container image that will start a stateless HTTP service on GCP. Which service do you select to host your container image?

- [ ] Cloud Run
- [ ] Cloud Run on Google Kubernetes Engine
- [ ] Cloud Functions
- [x] Google Kubernetes Engine

#### Q19. You want to develop Firebase security rules following Google best practices. Which tool(s) do you use?

- [x] Firebase Emulator
- [ ] Firebase Emulator and GCP Rules Simulator
- [ ] GCP policy emulator and Firebase Rules Simulator
- [ ] Firebase Emulator and Firebase Rules Simulator

#### Q20. You want to build an application with conversation interpretation based on machine learning speech understanding. Which service is a best fit for this scenario?

- [x] Dialogflow
- [ ] Natural Language Translation
- [ ] Speech API
- [ ] AutoML Natural Language

[reference link](https://cloud.google.com/dialogflow)

#### Q21. Which service must you enable on your GKE cluster in order to use Cloud Run on Google Kubernetes Engine (GKE)?

- [x] Stackdriver
- [ ] Istio
- [ ] Knative
- [ ] Spinnaker

#### Q22. How can you enable clients inside a GKE cluster to be able to contact Pods?

- [ ] Configure the clients to connect via the default cluster IP.
- [ ] Configure an external name. Configure the clients to connect via the external name.
- [x] Configure a node port. Configure the clients to connect via the node port.
- [ ] Configure a load balancer. Configure the clients to connect via the load balancer.

#### Q23. You want to capture the message acknowledgment state of a subscription at a given time. What do you do?

- [ ] Create a Cloud Pub/Sub subscription backup.
- [ ] Create a Cloud Pub/Sub subscription topic.
- [x] Create a Cloud Pub/Sub subscription snapshot.
- [ ] Create a Cloud Pub/Sub subscription.

#### Q24. You need to set a bucket storage class for data that will be accessed once a month or less. Which type do you select?

- [ ] coldline
- [ ] multi-regional
- [ ] regional
- [x] nearline

#### Q25. Which command copies a file named test.txt to a Cloud Storage bucket named myBucket?

- [ ] `gcloud cp gs://myBucket test.txt`
- [ ] `gsutil cp gs://myBucket test.txt`
- [ ] `gcloud cp test.txt gs://myBucket`
- [x] `gsutil cp test.txt gs://myBucket`

#### Q26. Which command adds a column family named `cf1` to your Bigtable table named `my-table`?

- [ ] `cbt createfamily cf1 my-table`
- [x] `cbt createfamily my-table cf1`
- [ ] `gcloud createfamily cf1 my-table cf1`
- [ ] `gcloud createfamily my-table cf1`

#### Q27. Which command do you use to connect to a running Compute Engine instance with SSH?

- [ ] `gcloud ssh compute [instance_name] --zone=[zone]`
- [ ] `compute ssh connect [instance_name] --zone=[zone]`
- [x] `gcloud compute ssh [instance_name] --zone=[zone]`
- [ ] `compute connect ssh [instance_name] --zone=[zone]`

#### Q28. You need to set CORS for some objects in a bucket for a client-side application. What do you do?

- [ ] Segment the objects into two buckets. For the CORS objects, set the CORS policy at the bucket level.
- [x] Segment the objects into two buckets. For the CORS objects, set the CORS policy at the bucket level. Add client-side code to handle the requests.
- [ ] Leave the objects in one bucket. Set the CORS policy at the object level.
- [ ] Leave the objects in one bucket. Set the CORS policy at the object level. Add client-side code to handle the requests.

[reference link](https://cloud.google.com/storage/docs/cross-origin)

#### Q29. For your application, you are building a CI/CD pipeline that logs information when a message is sent to a queue. Which services should you select?

- [ ] Cloud Functions and Cloud Spanner
- [x] Cloud Functions and Cloud Pub/Sub
- [ ] Cloud Run and Cloud Pub/Sub
- [ ] Cloud Run and Cloud Spanner

#### Q30. You need to create instances with identical configurations that cannot be changed. Which Compute Engine feature do yo use?

- [x] instance templates
- [ ] instance groups
- [ ] snapshots
- [ ] instances

#### Q31. You want to automatically perform security scans on user-developed containers. Where should you advise your users to host their containers?

- [x] Google Container Registry
- [ ] GitLab
- [ ] Artifactory
- [ ] Docker Hub

#### Q32. You need to control incoming and outgoing traffic to a Compute Engine instance. What do yo do?

- [x] Configure firewall rules.
- [ ] Configure VPC Network Peering.
- [ ] Configure routes.
- [ ] Configure external IP addresses.

[reference link](https://cloud.google.com/vpc/docs/firewalls)

#### Q33. Which object is a container for GCP services instances?

- [ ] group
- [ ] folder
- [x] project
- [ ] organization

#### Q34. What is needed to access GCP APIs in your project?

- [ ] GCP VMs
- [ ] GCP buckets
- [ ] GCP credentials
- [x] GCP users

[reference link](https://cloud.google.com/endpoints/docs/openapi/enable-api)

#### Q35. Which object is used to hold payment information for a GCP project?

- [ ] organization
- [x] billing account
- [ ] folder
- [ ] payment account

[reference link](https://cloud.google.com/billing/docs/images/billing-project.png?raw=png)

#### Q36. You need to cache your HTTP and HTTPS static content closer to users, so that you can get faster delivery and reduce serving costs. Which service do you set up?

- [ ] Cloud DNS
- [ ] Cloud NAT
- [x] Cloud CDN
- [ ] Cloud Load Balancing

[reference link](https://cloud.google.com/cdn/docs/caching)

#### Q37. You are designing security for an IoT device application. What best practices should you include in your design?

- [ ] Use a private key for each device. Keep the private key secret.
- [ ] Use a public key for each device. Keep the public key secret.
- [ ] Use a public private key pair for each device. Keep the public key secret.
- [x] Use a public private key pair for each device. Keep the private key secret.

[reference link](https://cloud.google.com/iot/docs/concepts/device-security)

#### Q38. You need to set a WordPress site with high availability on GCP using the fewest steps. What do you do?

- [ ] Configure and launch the WordPress HA deployment template from the GCP Marketplace.
- [ ] Configure and launch the WordPress HA deployment template from the WordPress Marketplace.
- [x] Create, configure, and launch a WordPress HA deployment template on Compute Engine.
- [ ] Create, configure, and launch a WordPress HA deployment template on Google Kubernetes Engine.

#### Q39. How do you configure Cloud Build to rebuild your image when a change is made to the source code?

- [x] Add a Cloud Build trigger, and set it to fire on commit to associate repository.
- [ ] Add a Cloud Build function, and set it to fire on commit to associate repository.
- [ ] Add a Cloud Build trigger, and set it to fire on commit to associate registry.
- [ ] Add a Cloud Build function, and set it to fire on commit to associate registry.

#### Q40. To be able to decrypt files that were encrypted with a customer-manager key, what conditions must be met?

- [x] Specify the decryption key with the same name as the encryption key. At least one version of a key with that name must be enabled.
- [ ] Specify a decryption key and version with the same name as the encryption key and version. The name key and that version must be enabled.
- [ ] Specify the decryption key with the same name as the encryption key. The named key and that version must be enabled.
- [ ] Specify a decryption key and version with the same name as the encryption key and version. At least one version of a key with that name must be enabled.

#### Q41. You want to encrypt a Compute Engine. What do you need to do?

- [x] Nothing. Images are encrypted by default with a Google-managed key.
- [ ] Nothing. Images are encrypted by default with a customer-managed key.
- [ ] Associate you image with a customer-managed key to encrypt it.
- [ ] Associate you image with a Google-managed key to encrypt it.

[Reference](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)

#### Q42. You want to quickly evaluate Cloud Filestore. What are the steps, in order, to set up a test environment?

- [ ] A
```
  1. Create a Filestore instance.
  2. Mount the fileshare from that instance on a client VM instance.
  3. Create a Compute Instance VM to be the client.
  4. Create a file on the mounted fileshare.
```
- [ ] B
```
  1. Create a Filestore instance.
  2. Mount the fileshare from that instance on a client VM instance.
  3. Create a file on the mounted file share.
  4. Create a Compute Instance VM to be the client.
```
- [x] C
```
  1. Create a Compute Instance VM to be the client.
  2. Create a Filestore instance.
  3. Mount the file share from that instance on a client VM instance.
  4. Create a file on the mounted fileshare.
```
- [ ] D
```
  1. Create a Compute Instance VM to be the client.
  2. Create a Cloud Filestore instance.
  3. Mount the fileshare from that instance on a client VM instance.
  4. Create a file on the mounted file share.
```

[Reference](https://cloud.google.com/filestore/docs/quickstart-console)

#### Q43. You need to optimize spending for always-on Compute Engine virtual machines of certain sizes and types-with minimum effort. What do you do?

- [ ] Analyze machine usage to verify that machines will be on for more that 25% of the time, and verify that contained use discounts have been automatically applied to your bill.
- [x] Analyze machine usage to verify that machines will be on for more that 25% of the time, and verify that sustained use discounts have been automatically applied to your bill.
- [ ] Analyze machine usage to verify that machines will be on for more than 25% of the time and purchase contained use discounts.
- [ ] Analyze machine usage to verify that machines will be on for more than 25% of the time and purchase sustained use discounts.

[Reference](https://cloud.google.com/compute/docs/sustained-use-discounts)

#### Q44. You are designing a GCP replacement for your on-premises data warehouse. Which service do you select?

- [ ] Cloud SQL
- [ ] Bigtable
- [ ] Cloud Spanner
- [x] BigQuery

#### Q45. How can you quickly back up a persistent disk on Compute Engine?

- [x] Take a snapshot
- [ ] Create an instance group
- [ ] Create an instance template
- [ ] Create an image

#### Q46. You are implementing IAM roles for your organization following GCP best practice. Which statement best reflects this?

- [ ] At minimum, you should have two levels of access: one for admins, one for users.
- [ ] At minimum, you should have three levels of access: one for networking, one for security, one for developers.
- [x] At minimum, you should have three levels of access: one for admins, one for security, one for users.
- [ ] At minimum, you should have two levels of access: one for networking, one for developers.

#### Q47. You need to quickly build an application that logs all file uploads to a Cloud Storage bucket. Which service do you select?

- [x] Cloud Functions
- [ ] Cloud Run
- [ ] Google Kubernetes Engine
- [ ] Google Compute Engine

[Reference](https://cloud.google.com/functions#all-features)

#### Q48. You need to answer the question "How long does it take my application to handle a given request?" What do you do?

- [ ] Configure Stackdriver Error Reporting.
- [ ] Configure Stackdriver Profiler.
- [x] Configure Stackdriver Trace.
- [ ] Configure Stackdriver Debug.

[Reference](https://stackoverflow.com/questions/69434714/how-to-use-stackdriver-on-gcp-to-get-how-long-does-it-take-to-process-a-request)

#### Q49. You want to select a fully managed, serverless platform for developing and hosting web applications at scale on GCP. Which service should you choose?

- [x] Google App Engine.
- [ ] Cloud Functions.
- [ ] Google Kubernetes Engine.
- [ ] Google Compute Engine.

[reference link](https://cloud.google.com/appengine/docs)

#### Q50. You have a set of exploratory queries that you want to run as inexpensively as possible in BigQuery. What should you do?

- [ ] Set the job priority for each query to Batch and expect to see query results immediately.
- [x] Set the job priority for each query to Interactive and expect to see query results immediately.
- [ ] Set the job priority for each query to Batch and expect to see query results within 24 hours.
- [ ] Set the job priority for each query to Batch and expect to see query results within 24 hours.

**Explanation**: _BigQuery offers a choice of two pricing models for runnig queries: on-demand (you are charged for the number of bytes processes by each query) and flat-rate (you purchase slots - dedicated processing capacity)._ If the exploratory queries are one-off, running in Interactive mode using on-demand pricing seems to be the optimal answer.

[Reference](https://cloud.google.com/bigquery/pricing)

#### Q51. How do you run a Docker container image on a Google Compute Engine virtual machine?

- [ ] Create a VM instance, and then SSH into the instance and install Kubernetes tools.
- [ ] Create a VM instance, and then SSH into the instance and install Docker tools.
- [ ] Create a VM instance and, in the web UI, select Allow HTTP traffic.
- [x] Create a VM instance and, in the web Ul, select Deploy a container image to this instance.

#### Q52. To configure a GCP Organization, which item should you create first?

- [x] Admin account
- [ ] Super Admin account
- [ ] multi-factor authentication
- [ ] recovery password

#### Q53. Which container(s) does Google Kubernetes Engine support?

- [ ] Docker or Singularity
- [ ] Docker, Singularity, or containerd
- [ ] Singularity only
- [x] Docker only

#### Q54. Cloud Genomics enables pipelines to run on top of which GCP service?

- [x] Cloud Dataflow
- [ ] Google Kubernetes Engine
- [ ] Cloud Dataproc
- [ ] Compute Engine

#### Q55. You want to encrypt a Compute Engine image. What do you need to do ?

- [ ] Nothing. Images are encrypted by default with a Google - managed key.
- [ ] Associate your image with the default Google-managed key to encrypt it.
- [ ] Nothing. Images are encrypted by default with a customer-managed key.
- [x] Associate your image with a customer-managed key to encrypt it.

**Explanation**: `Google does not store your keys on its servers and cannot access your protected data unless you provide the key. This also means that if you forget or lose your key, there is no way for Google to recover the key or to recover any data encrypted with the lost key.`

[Reference](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)

#### Q56. You want to build a data lake application on GCP. Which two services should you use?

- [ ] Cloud Storage and Cloud Spanner
- [x] Cloud Storage and Big Query
- [ ] Cloud Pub/Sub and Cloud Spanner
- [ ] Cloud Pub/Sub and Big Query

#### Q56. You want to work with GCP Organisation users in the console. Where do you navigate to?

- [ ] admin.google.com > Administration
- [x] console.cloud.google.com > Administration
- [ ] admin.google.com > Users
- [ ] console.cloud.google.com > Users

#### Q56. You want to select a fully managed platform for developing and hosting a web application written in Kotlin at scale on GCP. Which service should you choose?

- [x] Google App Engine Flexible
- [ ] Google App Engine Standard
- [ ] Google Kubernetes Engine Flexible
- [ ] Google Kubernetes Engine Standard

#### Q57. Which combination of Stackdriver services will alert you about errors generated by your applications and help you locate the root cause in the code?

- [x] Google Cloud Platform, Amazon Web Services
- [ ] Google Cloud Platform, Microsoft Azure, Amazon Web Services
- [ ] Google Cloud Platform, Microsoft Azure
- [ ] Google Cloud Platform

#### Q58. You are using Google Cloud Platform to host an Apache server and would like to enable an alert to notify you if the webserver becomes unresponsive. Which Google Cloud service and steps should you take to set up to set up this alert?

- [ ] The size of the Stackdriver log entries being exported exceeds the maximum capacity of the BigQuery dataset.
- [ ] The Cloud Data Transfer Service has not been enabled.
- [x] Stackdriver Logging does not have permission to write to the BigQuery dataset.
- [ ] There isn't a firewall rule allowing traffic between Stackdriver and BigQuery.

#### Q59. If you have configured Stackdriver Logging to export logs to BigQuery, but logs entries are not getting exported to BigQuery, what is the most likely cause?

- [ ] Monitoring, Trace, and Debugger
- [ ] Monitoring and Error Reporting
- [ ] Alerts and Debugger
- [x] Debugger and Error Reporting

#### Q60. You can use Stackdriver to monitor virtual machines on which cloud platforms?

- [x] Use Cloud Monitoring and create an uptime check.
- [ ] Use Cloud Monitoring and install the Monitoring Agent on the instance running the apache server.
- [ ] Use Cloud Monitoring and install the Ops Agent on the instance running the apache server.
- [ ] Use Cloud Profiler and create an alert.

#### Q61. In Google Kubernetes Engine, "**\_**" is a term Kubernetes uses to represent pods and controllers.

- [ ] masters
- [ ] pools
- [x] workloads
- [ ] nodes

#### Q62. In the command below, what is the purpose of the "--image" argument?

```
kubectl create deployment app --image=$ImageRepo:$Tag
```

- [ ] It tells Kubernetes what virtual machine image to use when launching new nodes.
- [ ] It is used to create a disk image of a running Docker container for backups or to be used in another deployment.
- [x] It tells the deployment controller which repository to check for a Docker image and what tag to use.
- [ ] It tells the deployment controller which Linux OS type to use when creating pods.

#### Q63. To effectively manage the limited number of IP addresses per node, how many IP addresses per pod does Google recommend?

- [ ] One IP address per pod
- [ ] Three IP addresses per pod
- [ ] Four IP addresses per pod
- [x] Two IP addresses per pod

#### Q64. In Google Kubernetes Engine, **\_** are the smallest unit of deployment within a Kubernetes cluster, and our primary Kubernetes building blocks.

- [x] pods
- [ ] instances
- [ ] sets
- [ ] containers

#### Q65. Which of the following statements is not a general security guideline for a Google Cloud Platform deployment pipeline?

- [ ] Regularly audit any changes to your IAM policies.
- [x] Integration steps should be able to deploy code.
- [ ] Log everything.
- [ ] Deployment steps should not be able to build code or access your code repository.

#### Q66. In order to allow signed images to be deployed with Google Cloud Platform's binary authorization enabled, you need to create a(n) **\_**.

- [ ] virtual machine
- [ ] alert
- [ ] log
- [x] attestor

#### Q67. Builders in Cloud Build are

- [ ] part of Google's proprietary infrastructure
- [ ] created from Managed Instance Templates
- [x] containers with pre-loaded tools and runtimes
- [ ] virtual machines with pre-loaded tools and runtimes

#### Q68. Which of the following statements about security in the Google Cloud Platform deployment pipeline is false?

- [x] It is pretty standard for developers and QA engineers to be allowed to create new clusters, but not allowed to deploy containers to certain existing clusters.
- [ ] Each employee's access to Google Cloud resources should be based upon what they require to do their job.
- [ ] The exact permissions will vary based upon the needs of the company, and depends upon the number of roles, steps, and environments that exist.
- [ ] Each employee's access to Google Cloud resources should be based on the principle of least privilege.

#### Q69. In order to create and store a key in Google Cloud Platform, you must first create a **\_** to hold the key.

- [ ] wallet
- [x] keyring
- [ ] policy
- [ ] keychain

#### Q70. David is the cloud admin for Blue Widget Corp. He has deployed a Linux VM called Linux01, and he needs to SSH to it from the console. Which command should David use to SSH to the VM?

- [ ] gcloud ssh --project blue-widget-project --zone us-central1-a Linux01
- [ ] gcloud compute ssh -project blue-widget-project -zone us-central1-a Linux01
- [ ] gcloud connect ssh --project blue-widget-project --zone us-central1-a Linux01
- [x] gcloud compute ssh --project blue-widget-project --zone us-central1-a Linux01

#### Q71. Which option will allow you to review latency data from App Engine Apps?

- [ ] App Engine Latency
- [x] Stackdriver Trace
- [ ] App Engine Data Viewer
- [ ] Stackdriver Latency

#### Q72. Regarding Stackdriver Debugger, which of the following locations are you not able to select your source code from?

- [ ] Bitbucket repository
- [x] Amazon S3
- [ ] Local files
- [ ] GitHub repository

#### Q73. Google Cloud services maintain **\_** that record all activity and access to your GCP resources.

- [ ] configuration files
- [ ] maintenance scripts
- [ ] analytics logs
- [x] audit logs

#### Q74. Which category of GCP audit log records every incident in which a user or service account is denied access to a resource?

- [ ] System Event
- [x] Policy Denied
- [ ] Admin Activity
- [ ] Data Access
