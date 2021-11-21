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

Note: Free trial doesn't have the organizations.

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

- [ ] 1. Create a VPN from GCP to your corporate network. 2. Create a GCP network for the project. 3. Create the VM instances to support the application.
- [ ] 1. Create a GCP network for the project. 2. Create a VPN from your corporate network to GCP. 3. Create the VM instances to support the application.
- [x] 1. Create a GCP network for the project. 2. Create a VPN from GCP to your corporate network. 3. Create the VM instances to support the application.
- [ ] 1. Create a VPN from your corporate network to GCP. 2. Create a GCP network for the project. 3. Create the VM instances to support the application.

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

#### Q19. You want to quickly test a single Docker container image that will start a stateless HTTP service on GCP. Which service do you select to host your container image?

- [ ] Cloud Run
- [ ] Cloud Run on Google Kubernetes Engine
- [ ] Cloud Functions
- [x] Google Kubernetes Engine

#### Q20. You want to develop Firebase security rules following Google best practices. Which tool(s) do you use?

- [x] Firebase Emulator
- [ ] Firebase Emulator and GCP Rules Simulator
- [ ] GCP policy emulator and Firebase Rules Simulator
- [ ] Firebase Emulator and Firebase Rules Simulator

#### Q21. You want to build an application with conversation interpretation based on machine learning speech understanding. Which service is a best fit for this scenario?

- [x] Dialogflow
- [ ] Natural Language Translation
- [ ] Speech API
- [ ] AutoML Natural Language

#### Q22. Which service must you enable on your GKE cluster in order to use Cloud Run on Google Kubernetes Engine (GKE)?

- [x] Stackdriver
- [ ] Istio
- [ ] Knative
- [ ] Spinnaker

#### Q23. How can you enable clients inside a GKE cluster to be able to contact Pods?

- [ ] Configure the clients to connect via the default cluster IP.
- [ ] Configure an external name. Configure the clients to connect via the external name.
- [x] Configure a node port. COnfigure the clients to connect via the node port.
- [ ] Configure a load balancer. Configure the clients to connect via the load balancer.

#### Q24. You want to capture the message acknowledgment state of a subscription at a given time. What do you do?

- [ ] Create a Cloud Pub/Sub subscription backup.
- [ ] Create a Cloud Pub/Sub subscription topic.
- [x] Create a Cloud Pub/Sub subscription snapshot.
- [ ] Create a Cloud Pub/Sub subscription.

#### Q25. You need to set a bucket storage class for data that will be accessed once a month or less. Which type do you select?

- [ ] coldline
- [ ] multi-regional
- [ ] regional
- [x] nearline

#### Q26. Which command copies a file named test.txt to a Cloud Storage bucket named myBucket?

- [ ] `gcloud cp gs://myBucket test.txt`
- [ ] `gsutil cp gs://myBucket test.txt`
- [ ] `gcloud cp test.txt gs://myBucket`
- [x] `gsutil cp test.txt gs://myBucket`

#### Q27. Which command adds a column family named `cf1` to your Bigtable table named `my-table`?

- [ ] `cbt createfamily cf1 my-table`
- [x] `cbt createfamily my-table cf1`
- [ ] `gcloud createfamily cf1 my-table cf1`
- [ ] `gcloud createfamily my-table cf1`

#### Q28. Which command do you use to connect to a running Compute Engine instance with SSH?

- [ ] `gcloud ssh compute [instance_name] --zone=[zone]`
- [ ] `compute ssh connect [instance_name] --zone=[zone]`
- [x] `gcloud compute ssh [instance_name] --zone=[zone]`
- [ ] `compute connect ssh [instance_name] --zone=[zone]`

#### Q29. You need to set CORS for some objects in a bucket for a client-side application. What do you do?

- [ ] Segment the objects into two buckets. For the CORS objects, set the CORS policy at the bucket level.
- [x] Segment the objects into two buckets. For the CORS objects, set the CORS policy at the bucket level. Add client-side code to handle the requests.
- [ ] Leave the objects in one bucket. Set the CORS policy at the object level.
- [ ] Leave the objects in one bucket. Set the CORS policy at the object level. Add client-side code to handle the requests.

#### Q30. For your application, you are building a CI/CD pipeline that logs information when a message is sent to a queue. Which services should you select?

- [ ] Cloud Functions and Cloud Spanner
- [x] Cloud Functions and Cloud Pub/Sub
- [ ] Cloud Run and Cloud Pub/Sub
- [ ] Cloud Run and Cloud Spanner

#### Q31. You need to create instances with identical configurations that cannot be changed. Which Compute Engine feature do yo use?

- [x] instance templates
- [ ] instance groups
- [ ] snapshots
- [ ] instances

#### Q32. You want to automatically perform security scans on user-developed containers. Where should you advise your users to host their containers?

- [x] Google Container Registry
- [ ] GitLab
- [ ] Artifactory
- [ ] Docker Hub

#### Q33. You need to control incoming and outgoing traffic to a Compute Engine instance. What do yo do?

- [x] Configure firewall rules.
- [ ] Configure VPC Network Peering.
- [ ] Configure routes.
- [ ] Configure external IP addresses.

#### Q34. Which object is a container for GCP services instances?

- [ ] group
- [ ] folder
- [x] project
- [ ] organization

#### Q35. What is needed to access GCP APIs in your project?

- [ ] GCP VMs
- [ ] GCP buckets
- [ ] GCP credentials
- [x] GCP users

[reference link](https://cloud.google.com/endpoints/docs/openapi/enable-api)

#### Q36. Which object is used to hold payment information for a GCP project?

- [ ] organization
- [x] billing account
- [ ] folder
- [ ] payment account

[reference link](https://cloud.google.com/billing/docs/images/billing-project.png)

#### Q37. You need to cache your HTTP and HTTPS static content closer to users, so that you can get faster delivery and reduce serving costs. Which service do you set up?

- [ ] Cloud DNS
- [ ] Cloud NAT
- [x] Cloud CDN
- [ ] Cloud Load Balancing

[reference link](https://cloud.google.com/cdn/docs/caching)

#### Q38. You are designing security for an IoT device application. What best practices should you include in your design?

- [ ] Use a private key for each device. Keep the private key secret.
- [ ] Use a public key for each device. Keep the public key secret.
- [ ] Use a public private key pair for each device. Keep the public key secret.
- [x] Use a public private key pair for each device. Keep the private key secret.

[reference link](https://cloud.google.com/iot/docs/concepts/device-security)

#### Q39. You need to set a WordPress site with high availability on GCP using the fewest steps. What do you do?

- [ ] Configure and launch the WordPress HA deployment template from the GCP Marketplace.
- [ ] Configure and launch the WordPress HA deployment template from the WordPress Marketplace.
- [x] Create, configure, and launch a WordPress HA deployment template on Compute Engine.
- [ ] Create, configure, and launch a WordPress HA deployment template on Google Kubernetes Engine.

#### Q41. How do you configure Cloud Build to rebuild your image when a change is made to the source code?

- [x] Add a Cloud Build trigger, and set it to fire on commit to associate repository.
- [ ] Add a Cloud Build function, and set it to fire on commit to associate repository.
- [ ] Add a Cloud Build trigger, and set it to fire on commit to associate registry.
- [ ] Add a Cloud Build function, and set it to fire on commit to associate registry.

#### Q42. To be able to decrypt files that were encrypted with a customer-manager key, what conditions must be met?

- [x] Specify the decryption key with the same name as the encryption key. At least one version of a key with that name must be enabled.
- [ ] Specify a decryption key and version with the same name as the encryption key and version. The name key and that version must be enabled.
- [ ] Specify the decryption key with the same name as the encryption key. The named key and that version must be enabled.
- [ ] Specify a decryption key and version with the same name as the encryption key and version. At least one version of a key with that name must be enabled.

#### Q43. You want to encrypt a Compute Engine. What do you need to do?

- [x] Nothing. Images are encrypted by default with a Google-managed key.
- [ ] Nothing. Images are encrypted by default with a customer-managed key.
- [ ] Associate you image with a customer-managed key to encrypt it.
- [ ] Associate you image with a Google-managed key to encrypt it.

[Reference](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)

#### Q44. You want to quickly evaluate Cloud Filestore. What are the steps, in order, to set up a test environment?

- [ ]
  ```
  1. Create a Filestore instance.
  2. Mount the fileshare from that instance on a client VM instance.
  3. Create a Compute Instance VM to be the client.
  4. Create a file on the mounted fileshare.
  ```
- [ ]
  ```
  1. Create a Filestore instance.
  2. Mount the fileshare from that instance on a client VM instance.
  3. Create a file on the mounted file share.
  4. Create a Compute Instance VM to be the client.
  ```
- [x]
  ```
  1. Create a Compute Instance VM to be the client.
  2. Create a Filestore instance.
  3. Mount the file share from that instance on a client VM instance.
  4. Create a file on the mounted fileshare.
  ```
- [ ]
  ```
  1. Create a Compute Instance VM to be the client.
  2. Create a Cloud Filestore instance.
  3. Mount the fileshare from that instance on a client VM instance.
  4. Create a file on the mounted file share.
  ```

[Reference](https://cloud.google.com/filestore/docs/quickstart-console)

#### Q45. You need to optimize spending for always-on Compute Engine virtual machines of certain sizes and types-with minimum effort. What do you do?

- [ ] Analyze machine usage to verify that machines will be on for more that 25% of the time, and verify that contained use discounts have been automatically applied to your bill.
- [ ] Analyze machine usage to verify that machines will be on for more that 25% of the time, and verify that sustained use discounts have been automatically applied to your bill.
- [ ] Analyze machine usage to verify that machines will be on for more than 25% of the time and purchase contained use discounts.
- [ ] Analyze machine usage to verify that machines will be on for more than 25% of the time and purchase sustained use discounts.

#### Q46. You are designing a GCP replacement for your on-premises data warehouse. Which service do you select?

- [ ] Cloud SQL
- [ ] Bigtable
- [ ] Cloud Spanner
- [x] BigQuery

[Source: LinkedIn Assessment Practice mode](https://i.imgur.com/mOCQVug.png)

#### Q47. How can you quickly back up a persistent disk on Compute Engine?

- [x] Take a snapshot
- [ ] Create an instance group
- [ ] Create an instance template
- [ ] Create an image

[Source: LinkedIn Assessment Practice mode](https://i.imgur.com/9rNe5MV.png)

#### Q48. You are implementing IAM roles for your organization following GCP best practice. Which statement best reflects this?

- [ ] At minimum, you should have two levels of access: one for admins, one for users.
- [ ] At minimum, you should have three levels of access: one for networking, one for security, one for developers.
- [ ] At minimum, you should have three levels of access: one for admins, one for security, one for users.
- [ ] At minimum, you should have two levels of access: one for networking, one for developers.

#### Q49. You need to quickly build an application that logs all file uploads to a Cloud Storage bucket. Which service do you select?

- [ ] Cloud Functions
- [ ] Cloud Run
- [ ] Google Kubernetes Engine
- [ ] Google Compute Engine
