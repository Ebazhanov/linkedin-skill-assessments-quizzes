## Google Cloud Platform (GCP) Assessment

#### Q1. You want to schedule a cron job to send a message to a Cloud Pub/Sub topic hourly. What do you do?

- [ ] Create a Cloud Function with a targer of HTTP
- [ ] Create a Cloud Scheduler job with a targer of HTTP
- [x] Create a Cloud Function with a targer of Cloud Pub/Sub
- [ ] Create a Cloud Scheduler job with a targer of Cloud Pub/Sub

#### Q2. You want to set up a managed Apache Spark cluster. Which service do you configure?

- [ ] Cloud Dataprep
- [ ] Cloud Composer
- [ ] Cloud Dataflow
- [x] Cloud Dataproc

#### Q3. GCP Organizations are not available in your GCP project. What type of account are you using?

- [ ] Temporary
- [*] Free Tier- free trail doesnt have the organization
- [ ] Local
- [ ] Organizational

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
- [?] Create a notebook instance with TPU. Upload the notebook to the instance.
- [ ] Create a notebook instance with GPU. Upload the notebook to the instance.
- [ ] Upload the notebook to Google Colaboratory. Set the hardware accelerator yo use TPU.

#### Q9. You need to configure a data retention policy for a Cloud Storage bucket to govern how long objects in the bucket must be retained. What feature do you enable?

- [ ] Requester Pays
- [x] Bucket Lock
- [ ] Bucket Policy Only
- [ ] Encryption Type

#### Q10. To be able to configure an existing Cloud Function, what information should you review and from which location?

- [ ] execution time in Cloud Storage logs
- [ ] execution time in Stackdriver logs
- [?] text payload in Stackdriver logs
- [ ] text payload in Cloud Storage logs

#### Q11. You need to execute a "lift and shift" move with as few steps as possible. Which items do you need to create to accomplish this task, listed in the correct order of creation?

- [ ] 1. Create a VPN from GCP to your corporate network.
  2. Create a GCP network for the project.
  3. Create the VM instances to support the application.
- [ ] 1. Create a GCP network for the project.
  2. Create a VPN from your corporate network to GCP.
  3. Create the VM instances to support the application.
- [?] 1. Create a GCP network for the project. 2. Create a VPN from GCP to your corporate network. 3. Create the VM instances to support the application.
- [ ] 1. Create a VPN from your corporate network to GCP.
  2. Create a GCP network for the project.
  3. Create the VM instances to support the application.

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

- [ ] Radis and Oracle
- [ ] MySQL and Oracle
- [ ] Radis and PostgreSQL
- [x] MySQL and PostgreSQL

#### Q18. You want to try out a machine-learning TensorFlow example notebook with the fewest configuration steps on GCP. What do you do?

- [ ] Create a notebook instance with TPU. Upload the notebook to the instance.
- [x] Create a notebook instance with GPU. Upload the notebook to the instance.
- [ ] Upload the notebook to Google Colaboratory. Set the hardware accelerator to use GPU.
- [ ] Upload the notebook to Google Colaboratory. Set the hardware accelerator to use TPU.

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
