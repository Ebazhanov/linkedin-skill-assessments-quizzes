## Amazon Web Services (AWS)

#### Q1. You have an application using a 100 GB MySQL database that you are migrating into AWS. What should you consider when deciding between whether to host the database on RDS for MySQL or Aurora?

- [ ] cost
- [ ] ease of maintenance vs. granularity of control
- [x] all of these answers
- [ ] the current storage engine used by the application, such as InnoDB or MyISAM

#### Q2. Which database is a NoSQL database type that can quickly store and retrieve key-value pairs?

- [ ] Aurora
- [ ] Neptune
- [ ] RDS for MySQL
- [x] DynamoDB

#### Q3. Your database is an RDS instance running SQL Server with Multi-AZ replication and you have several older .NET console utilities that perform database operations every 15 seconds. When the cluster has to switch the primary database server to the secondary AZ, the .NET utilities start to report connection failures to the database although other applications are able to access the database. How do you correct this problem?

- [ ] Use the RDS console to force a reboot of the database instance so that the primary server becomes the master server again.
- [ ] The server running the .NET utilities is caching the DNS lookup on the database cluster address. Flush the DNS cache of the server and force the C# utilities to open new connections to the database.
- [ ] A.NET application will retain the IP address of a connection string until the host machine is rebooted.
- [x] The NET utilities need to change the SQL Server endpoint in the connection strings to read from the secondary database server using a try/catch.

#### Q4. What AWS services can help you automate your development pipeline for continuous integration and continuous deployment?

- [ ] CodePipeline
- [ ] CodeDeploy
- [x] all of these answers
- [ ] CodeBuild

#### Q5. Which AWS service complies with the standards outlined in Payment Card Industry Data Security Standard (PCI DSS) Level 1 for the handling and transmission of credit card data?

- [ ] API Gateway
- [x] all of these answers
- [ ] Simple Queue Service (SQS)
- [ ] Kinesis Data Streams

#### Q6. You have a large amount of files on your network-attached storage array that must be archived and maintained for a period of 10 years due to industry regulations. This data will be infrequently accessed but must be kept What is the best AWS service for storing this data?

- [ ] EFS
- [ ] Snowball
- [ ] OEBS
- [x] S3 Glacier

#### Q7. For your AWS root account, you have generated a random password of the maximum allowed length and included special characters. Which additional steps should you take to secure your AWS root account?

- [ ] Create an AM role for the account administrator with the highest privileges. Do not store the root password, but when the root account is needed reset the password on the root account via email confirmation and repeat this procedure.
- [ ] Store your randomly generated password in your organizational secrets database using a service such as 1Password or LastPass, and only grant access to this secret to the DevOps team.
- [ ] Create IAM accounts for your administrators and attach the AdministratorAccess policy to their accounts. Disable the root account in the user settings.
- [x] Create an IAM role for the account administrator with the highest privileges and do not use the root account in day-today operations. Enable two-factor authentication on the root account

#### Q8. Which Elastic Load Balancing option supports Lambda as a target?

- [ ] Network Load Balancer
- [ ] Lambda can not be called directly by incoming web requests. You must use API Gateway.
- [ ] Classic Load Balancer
- [x] Application Load Balancer

#### Q9. How do you architect a solution for an SQL Server database to be replicated across AWS regions in an active-active architecture?

- [ ] Use RDS for SQL Server and create the same instance in two different regions. Use Database Migration Service to keep each database in sync.
- [ ] Use a VPN or VPC peering to establish a connection between the VPCs in each region. Install SQL Server Enterprise Edition on EC2 instances in each region and configure an Always On availability group.
- [x] Use RDS for SQL Server 2016 or 2017 Enterprise Edition. Enable Multi-AZ support and select the Mirroring/Always On option. Select another region for the mirroring option.
- [ ] You can not set up an active-active architecture for SQL Server that spans geographic regions.

[Reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html?opt_id=oeu1612780272452r0.9199525073583283)

#### Q10. What does it cost to launch an EC2 instance from the AWS Marketplace?

- [ ] All images in the AWS Marketplace incur additional hourly fees in addition to the charges from the instance size you select.
- [ ] You can only launch images that were created by other users on your AWS account, so you pay only for the instance size you select and the S3 storage costs for the base image.
- [x] Each image has its own pricing that could either be free, or include charges for software licensing costs. You will also pay for the instance the image runs on
- [ ] All images in the AWS Marketplace contain only open-source software with no additional fees and are created by other AWS users. You will pay only for the instance size you select.

#### Q11. When using an ECS cluster with EC2 instances, what maintenance tasks should you perform on the EC2s?

- [ ] The instances created by ECS do not have patches that need to be applied; however, you should make sure your containers contain any important security updates.
- [x] Refresh the cluster with instances built from the latest ECS AMI.
- [ ] ECS clusters do not use EC2 instances.
- [ ] You should not directly manipulate the EC2 instances created by ECS. AWS will automatically update these instances.

#### Q12. What in-memory caching server is not supported by ElastiCache?

- [ ] Redis 5
- [ ] Memcached
- [x] Elasticsearch
- [ ] Redis 3

#### Q13. Which AWS service can be used to help generate the documentation required by various compliance standards, such as Payment Card Industry Data Security Standard (PCI DSS) Level 1 for the handling of credit card data?

- [x] Artifact
- [ ] DocumentDB
- [ ] Print out the AWS Compliance summary and keep it with your required documentation for an audit.
- [ ] Secrets Manager

#### Q14. When using AWS for research and development ahead of a planned migration, how do you prevent unexpected increases or spikes in the billing?

- [ ] Use the billing dashboard to create a cost budget. Input the max amount you want to be charged each month. Any charges that occur over this amount will cause AWS to automatically suspend those resources
- [ ] Using the root AWS account, activate IAM access to the billing information for the account. Make sure your IAM users have the Billing FullAccessGroup policy. Then from the billing dashboard, check the accrued charges once a day.
- [ ] If you are using the AWS free tier, you will have to confirm the usage of any service that goes over the AWS free tier limits.
- [x] Using the root AWS account enable Billing Alerts in the user preferences. Then use CloudWatch to create a billing alarm and set a threshold to a specific dollar amount for your estimated monthly charges.

#### Q15. You are creating a DynamoDB table to store all movies that have been released since 1938. Your application will allow users to search by movie title and see the details of that film. Given the sample below showing the movie data that you will be importing, what is the best set of keys to apply to this table?

```json
{
  "title": "The Avengers",
  "year": 2012,
  "cast": ["Mark Ruffalo", "Robert Downey, Jr."],
  "genres": ["Action"]
}
```

- [ ] The primary key should be a partition key of the title field.
- [ ] The primary key should be the title field and the partition key should be the genres field.
- [ ] The primary key should be a composite key comprised of a partition key on the title field and a sort key on the year field.
- [x] The primary key should be created as a completely unique value, such a sequential numerical list of movie IDs. The partition key should be title field for fast lookup.

#### Q16. What data store provides a simple and quick way of storing basic user attributes in an object-based format?

- [ ] ORDS for Oracle
- [ ] Redshift
- [ ] Neptune
- [x] DynamoDB

#### Q17. You need a schemaless database. Which Amazon database service provides that solution?

- [ ] ORDS
- [ ] Aurora
- [ ] Redshift
- [x] DynamoDB

#### Q18. Which communication channel does SNS not support natively?

- [ ] OSMS text message
- [ ] push notification
- [ ] email
- [x] automated phone call

#### Q19. When designing a serverless web application using Lambda, what key concept must you factor into your design?

- [ ] Serverless web applications run within the web browser of the user, so you will need to store any data the user changes directly in a database.
- [ ] Lambda only allows you to write functions in JavaScript.
- [ ] Lambda does not use servers, so it can only return the same request to every user.
- [x] Lambda is stateless, so it won't remember who a user is in between requests.

#### Q20. A principle of DevOps is to view infrastructure as code. Which AWS service allows you to script your AWS infrastructure?

- [ ] CloudTrail
- [x] CloudFormation
- [ ] AWS Config
- [ ] AWS Service Catalog

#### Q21. You created a Windows EC2 instance with a public IP address and installed SQL Server. When attempting to connect to SQL Server from SQL Server Enterprise Manager on your local computer, the Windows EC2 instance is unable to establish a connection to the server. What is the first thing you should check?

- [ ] Check the routing tables for the VPC.
- [x] Verify that the assigned security groups allow TCP port 1433 traffic from your current IP address.
- [ ] Check the policies within Windows Firewall.
- [ ] Verify that you are connecting to the instance using a user that is not sa.

#### Q22. You are hosting an application configured to stream media to its clients on TCP ports 3380-3384, 3386-3388, and 3390. The Inbound tab below shows three incoming security group policies attached to this instance. Which policy should you use?

![image](images/001.png?raw=png)

- [x] The rule that exposes TCP ports 3380-3390 would also publicly expose port 3389 (RDP) to the entire internet. Write separate rules to only expose the needed ports.
- [ ] The first security group rule allows all traffic into this instance. Exposing your entire instance to the whole internet leaves the server open to various attacks of the other services running on different port numbers.
- [ ] Verify that the AWS account owners actually control the entire CIDR C block for 12.228.11.0-255 and these are secured IPs for RDP access into this instance.
- [ ] There are no recommendations to make.

#### Q23. You have four front-end web servers behind a load balancer, which use NFS to access another EC2 instance that resizes and stores images for the front-end application. What security group policies should be assigned to these servers?

- [ ] Assign Elastic IPs to all of the instances and create a group that allows all traffic to pass between each of the five
      Elastic IP addresses and allow all inbound HTTPS traffic.
- [x] Front-end web servers should allow HTTPS. Assign another group to all of the instances that allows all traffic to pass between instances using that group.
- [ ] Create a security group that allows inbound NFS, HTTP, and HTTPS traffic from all IP addresses. Apply this group to all of the servers.
- [ ] Create a security group that allows inbound HTTP and HTTPS traffic from all IP addresses and apply this to the web servers. Create a second security group for the NFS filestore that allows outbound NFS traffic to the private IP range of the front-end web servers.

#### Q24. You have a Linux EC2 web server that suddenly is timing out on all HTTP requests and your SSH connection attempts are timing out. You notice that it is failing the system status check in the EC2 console. What action should you take?

- [x] Restore the instance from the last AMI image. System status checks indicate that the filesystem on the instance is corrupted.
- [ ] Stop and start the instance. This will move the instance to another host.
- [ ] Contact AWS support. Failing a system status check indicates a failure in the underlying hardware and must be addressed by an AWS representative.
- [ ] Reboot the instance. This will stop and start the instance and move it to another host.

#### Q25. You have several on-premise servers and would like to store your offsite backups on AWS. What fully managed backup service can you use to ship your backups to AWS?

- [ ] Windows Server 2016 supports S3 as a target when using storage replicas.
- [x] Use Storage Gateway.
- [ ] Sync files directly to S3 with the AWS CLI.
- [ ] Use the RDS console to force a reboot of the database instance so that the primary server becomes the master server again.

#### Q26. What is the best practice for creating a highly available PostgreSQL database in RDS that can sustain the loss of a single AWS region?

- [ ] PostgreSQL cannot be replicated across regions. Restore the database backups from an S3 bucket and repoint your database connections to the new instance.
- [ ] Create Read Replicas in other AWS regions. You can designate a new master database from any of the read replicas until the regional failure is resolved.
- [ ] Verify that your instance is configured for Multi-AZ support. Database changes will be automatically synced to another region in the event of a failure and RDS will automatically select a new master until the regional failure is resolved.
- [x] Create Read Replicas in other AWS regions. Ensure read operations against the database occur on an available Read Replica, and send write operations to another region if you need to promote a Read Replica to a standalone database if the master is down.

#### Q27. You created a new Linux EC2 instance and installed PostgreSQL but you are not able to establish a connection to the server from your local computer. What steps do you take to resolve this issue?

- [ ] Create a security group rule that allows all traffic from 0.0.0.0/0. This will verify whether or not another rule is denying the traffic.
- [x] Verify that the assigned security groups allow traffic from your IP address to port 5432. Verify that PostgreSQL is configured to listen to external traffic and is bound to the public interface.
- [ ] Make sure that you are using an Elastic IP and that it is included within the `postgresql.conf` configuration file.
- [ ] Stop and start the instance. New security group rules will only take effect after a restart.

#### Q28. What does the statement body of this S3 bucket policy do?

```json
{
  "Sid": "bucketpolicy1",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::userreports/*",
  "Condition": {
    "IpAddress": { "aws:SourceIp": "68.249.108.0/24" },
    "NotIpAddress": { "aws:SourceIp": "68.249.108.128/32" }
  }
}
```

- [ ] bucketpolicy1 allows any user to perform any action on the objects in the userreports bucket, but limits the objects to read-only permissions for anyone coming from 68.249.108.0 to 68.249.108.255 - except 68.249.108.128.
- [ ] bucketpolicy1 allows any user coming from the IP range of 68.249.108.0 to access objects in the userreports bucket and denies access to 68.249.108.128.
- [ ] bucketpolicy1 allows any user to perform any action on the objects in the userreports bucket - except anyone coming from the IP of 68.249.108.128.
- [x] bucketpolicy1 allows any user coming from the IP range of 68.249.108.0 to 68.249.108.255 to access objects in the userreports bucket-except anyone coming from the IP of 68.249.108.128.

#### Q29. A new developer has been added to the team and you have been asked to provide access to the organization's AWS account. What is the best practice for granting access?

- [ ] Give the new developer the IAM login that is assigned to the development team. This IAM user should already include all of the policies that a developer would need.
- [ ] Create a IAM user for the new developer. Manually assign policies to the new IAM user account.
- [ ] Do not give the new developer access to the AWS console. Using the IAM user that is assigned to the development group, generate a new set of access keys and label these with the name of the developer.
- [x] Create a IAM user for the new developer. Assign the new developer the a developer group you already created for the other developers.

#### Q30. When launching an EC2 instance with an instance type that supports instance storage, what use case is best for instance storage?

- [x] Use the instance storage to serve temporary files that require low I/O latency.
- [ ] Use the instance storage to handle files uploaded by your users. Since it is more secure than an EBS volume, you can isolate any malicious files from infecting your server.
- [ ] Instance storage is faster than EBS volumes, so install the root of the operating system on this volume to speed up server performance.
- [ ] Instance storage is a deprecated option for storage and should not be used.

#### Q31. What's the best practice for horizontally scaling a legacy ASP.NET web application that relies on Active Directory and is currently deployed to a single Windows EC2 instance?

- [x] Use Sysprep to shut down the instance during a maintenance window. Create an AMI image and place both servers behind Application Load Balancer with sticky sessions.
- [ ] Launch a new EC2 with the latest version of Windows Server and install the application again. Use Application Load Balancer and sticky sessions to balance between both servers.
- [ ] Create a clone of the server using an AMI image and user Application Load Balancer to balance the traffic between both instances using sticky sessions.
- [ ] Horizontal scaling is not the best practice in this situation. Increase the size of the existing EC2 instance and vertically scale the application.

#### Q32. What does this small section of a CloudFormation template do?

```yaml
FlowLog:
  Type: AWS::EC2::FlowLog
  Properties:
    DeliverLogsPermissionArn: !GetAtt IamRole.Arn
    LogGroupName: FlowLogsGroup
    ResourceId: !Ref LogVpcId
    ResourceType: VPC
    TrafficType: ALL
```

- [x] It writes the VPC network flow logs to the CloudWatch FlowLogsGroup log group. You could use this to inspect the network connections of your VPC.
- [ ] It logs all of the network traffic within a VPC except Instance IDs defined by LogVpcID and logs it to the CloudWatch FlowLogsGroup log group.
- [ ] It logs all the network traffic going to and from a single EC2 instance into the CloudWatch FlowLogsGroup log group. You could use this to inspect suspicious network traffic coming into an EC2 instance.
- [ ] It logs all of the DNS requests made by resources within a VPC and logs them to the CloudWatch FlowLogsGroup. Use this to diagnose DNS lookup errors within your environment.

#### Q33. You are running Docker containers on ECS. What is the most important metric to monitor?

- [ ] The running container count for each service from within CloudWatch.
- [ ] The instance health of each EC2 instance in your cluster from within CloudWatch.
- [ ] Monitor the EC2 service dashboard. Watch for posted outages to the ECS service.
- [x] The memory consumption of each EC2 instance in your cluster from within CloudWatch.

#### Q34. Application Load Balancer can route traffic to several different target groups based upon several conditions. Which of these use cases is not supported by Application Load Balancer?

- [ ] A request with a HTTP header of X-Requested-With: staging can be routed to a target group for an ECS service in your staging environment.
- [ ] Source IPs matching 192.0.2.0/24 on a listener port of 1433 can be routed to a target group for an RDS for SQL Server cluster.
- [ ] A path of /signup\* can be routed to a target group for a Lambda function that processes new user registrations.
- [x] An Http POST query string of ? action=createuser can be routed to a target group for an ECS service.

#### Q35. What does a VPC do?

- [x] creates a cloud-based network to interconnect a set of virtual servers and appliances
- [ ] creates a secure tunnel between two networks
- [ ] creates a shared storage plane for application data to be shared across multiple instances.
- [ ] creates a private network that is completely isolated from the public internet.

#### Q36. Can you lose the public IP address associated with your EC2 instance?

- [ ] Yes, you can lose it if you reboot the instance.
- [x] Yes, you can lose it if you stop and start the instance.
- [ ] No, you will never lose the public IP address for your instance.
- [ ] Yes, you can lose it when you edit the instance properties and release the IP address.

#### Q37. Where is the best place to store database backups on an EC2 instance that is configured as a database server?

- [x] an S3 bucket, synced with the database backups via a script that calls the AWS CLI
- [ ] EBS volume attached to the instance
- [ ] instance attached to the instance
- [ ] instance storage, with a script that replicates the database backups to another instance in a different availability zone.

#### Q38. Which of these is a valid restriction on the properties of a VPC?

- [ ] You can have only 10 internet gateways per region on a new AWS account.
- [ ] You can have only 10 VPCs per region on a new AWS account
- [x] You cannot create a CIDR block with a netmask larger than /16
- [ ] You can have only 10 subnets within a VPC

#### Q39. You have a Linux EC2 instance that is not responding to requests and you can not connect to it via SSH. Using the EC2 console, you issued a command to stop the instance, but for the past 10 minutes the instance has been in the "stopping" state. What is the next step you should take?

- [x] Issue another stop action via the EC2 console, and choose the option to forcefully stop the instance.
- [ ] Create an AMI image of the instance, and choose the option to take the image without restarting the instance.
- [ ] Edit the instance properties and increase the instance size.
- [ ] Contact AWS support. Any further actions could corrupt the file system.

#### Q40. You have 14 on-premise web servers, 4 database servers, 6 servers using GIS software, 3 file servers, and 4 development servers. What considerations should you take into account when migrating these servers into AWS?

- [ ] AWS does not have a way to separate billing for compute costs, so you will need to design a way to split the budget between departments.
- [ ] Software licensing costs are always included in services such as RDS, so factor the loss of use of your on-premise licenses in your budget.
- [x] New AWS accounts are limited to 20 on-demand EC2 instances. Submit a request to increase your rate limits before starting a migration.
- [ ] The only way to transfer large amounts of database data up to AWS is via S3, which can have a slow upload speed. Plan for this delay and cost in your migration plan.

#### Q41. As your web application grows and your application monitoring needs become more complex, which additional log monitoring service should you NOT consider?

- [ ] ELK stack: Elasticsearch, Loggly, and Kibana
- [x] PRTG
- [ ] New Relic
- [ ] Datadog

#### Q42. You have a T2 EC2 instance that is critical to your infrastructure. How would you monitor the most important metric for this instance?

- [x] Turn on CloudWatch Auto Recovery and put monitors on the System Status and Instance Status checks for the instance to notify you when either is in alarm.
- [ ] Use CloudWatch to put monitors on the remaining CPU credits. If you run out of CPU credit the instance will be stopped.

#### Q43. Which feature can be used to respond to a sudden increase in web traffic?

- [ ] EC2 Auto Scaling groups
- [ ] AWS Shield Advanced
- [ ] RDS Read Replicas
- [x] all of these answers

#### Q44. If a set of servers are located within a private subnet of your VPC, how can you connect those servers to on-premise servers?

- [ ] Establish a connection with AWS Direct Connect.
- [ ] Use the AWS Client VPN.
- [ ] Install a OpenVPN server on an instance that is located within the subnet with an elastic IP.
- [x] All of these options can establish a connection to a private subnet.

#### Q45. You have a UDP load balancer that is created by an instance that is running an NGINX proxy. Your application performance management (APM) solution can detect failures in your load balancer instance and transfer the Elastic IP to a passive standby instance. Using the AWS CLI, which script do you program into your APM to move the Elastic IP?

- [x] A

```
aws ec2 disassociate-address --association-id eipassoc-2bebb712
aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
```

- [ ] B

```
aws ec2 release-address --association-id eipassoc-2bebb712
aws ec2 assign-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
```

- [ ] C

```
aws ec2 stop-instances --instance-ids i-8b953
wait 30
aws ec2 disassociate-address --association-id eipassoc-2bebb712
aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
aws ec2 start-instances --instance-ids i-8b953
```

- [ ] D

```
aws ec2 release-address --association-id eipassoc-2bebb712
aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
```

#### Q46. What service can host your Docker containers?

- [ ] Lightsail
- [ ] Elastic Container Service (ECS)
- [ ] Elastic Compute Cloud (EC2)
- [x] All of these services can host a Docker container.

#### Q47. In the S3 console, underneath the Access column, what does the public badge next to the bucket name indicate?

![image](images/002.png?raw=png)

- [x] All objects within this bucket are assigned public access and could be readable or writable by anyone on the internet. Ensure no sensitive data is being publicly shared within this bucket.
- [ ] All objects within this bucket are writable, which means that the public internet has the ability to upload any file directly to your S3 bucket. Your S3 bucket could be used to serve malware.
- [ ] Some objects within this bucket are assigned public access. Verify that any publicly shared objects within this bucket contain no sensitive data.
- [ ] Objects within this bucket can be made public, if the ACL on that object is set to allow everyone access. Private buckets do not allow you to set public permissions on any object.

#### Q48. What privilege is specific to the AWS root account, and cannot be granted to another IAM user on the account?

- [ ] Revoke the AdministratorAccess role or grant it to another IAM user.
- [ ] Create a new hosted zone in Route 53.
- [x] Delete the AWS account.
- [ ] Modify the billing details.

#### Q49. Your application is sending 50,000 emails through SES each day. Since you must maintain a low bounce rate to avoid being put on probation, what simple system do you architect to automatically process hard bounces?

- [x] Configure SES to send all bounce events to an SNS topic. Create a Lambda function that processes each hard bounce event and automatically flags that account as a bounce in your application to prevent further sending attempts.
- [ ] Configure SES to no longer send to email addresses that are on your bounce list.
- [ ] Configure SES to send the logs of all delivery attempts through Kinesis Firehose. Process each event and look for bounce types and remove these emails from your list.
- [ ] Send all emails through SES with a custom reply-to header. Configure SES to listen for events on this email address and flag any email address that replies to this account as a bounced message and remove it from your email list.

#### Q50. Your web application is getting a suspicious amount of bad requests from foreign IP addresses. Your business is operating in only a few countries and you would like to block any other traffic. What is the best practice for limiting access to your web application by country?

- [x] Use Web Application Firewall and create a geo match condition to drop all requests from countries that aren't on your allow list.
- [ ] Use Application Load Balancer to create a new routing rule that looks at source IP address. Add an IP block for the countries that have access.
- [ ] Host the front end of your website in CloudFront and configure a geo restriction on the distribution.
- [ ] Use CloudTrail to monitor the IP addresses of the bad requests. Use Lambda to add these IP addresses to an Application Load Balancer rule that blocks the IPs.

#### Q51. What is the best practice for maintaining Windows EC2 instances and applying updates?

- [ ] Turn on auto update in Windows Update on each EC2 that is launched, or create your own AMI with this feature enabled and launch all of your EC2 instances from this AMI.
- [ ] Create a maintenance schedule that an employee must fill out each week confirming a visual inspection of each instance was conducted and which patches were applied.
- [x] Use AWS Systems Manager Patch Manager to find an patch instances that require updates during a set maintenance window.
- [ ] Install Window Server Update Services on your primary Active Directory controller.

#### Q52. In addition to CloudFormation, you can use other orchestration tools to automate server formation and maintenance. Which tool is _not_ an efficient choice for the orchestration of a large infrastructure?

- [ ] Chef
- [ ] Ansible
- [ ] Puppet
- [x] Vagrant

#### Q53. What happens to a SQL Server RDS instance if the databases increase in size and go over the allocated space?

- [ ] RDS will automatically increase the allocated space by 10% and will send the AWS root account an email with resolution steps. Allocate more space to avoid overage charges.
- [x] The database instance will report a STORAGE_FULL status and become inaccessible if the instance does not have enough remaining storage to operate. Allocate more space to the instance.
- [ ] SQL Server will close all existing connections to the databases and attempt to shrink its log files to reclaim storage space.
- [ ] RDS will automatically increase the allocated space by 5% and will continue to allocate new space up to 50% of the orginal allocated space. When storage space has increase 50%, RDS will automatically stop the instance to preserve data integrity.

#### Q54. You have a fleet of IoT devices that send telemetry to a server-side application provided by your IoT vendor for decoding a proprietary messaging format. The devices are provisioned to send telemetry reports to your server via UDP on port 6339. What is the best way scale this server as more Iot devices are added to your fleet?

- [ ] Use a Network Load Balancer to distribute the traffic across your servers. Use UDP health checks to determine if the server is available to receive traffic.
- [x] Use Route 53 with HTTP health checks. Create an application on the server to report the readiness status of the vendor-provided server software to Route 53 via HTTP.
- [ ] Use Route 53 with UDP health checks. As you scale up, Route 53 wiwll route the traffic to the new servers if they pass the health checks.
- [ ] Use Application Load Balancer to distribute the traffic across your servers.

#### Q55. the outbound rules of a security group only allow traffic going to 0.0.0.0/0 on TCP Port 22 (SSH) and TCP port 3306 (MySQL). Review the inbound rules listed in the image below. What is the most important issue to fix with this security group configuration, for an Ubuntu EC2 instance acting as a web server?

![image](https://user-images.githubusercontent.com/8637045/112515574-c077e780-8d6c-11eb-96a6-11f27a0547cf.png?raw=png)

- [ ] The outbound rules block UDP port 53, so the server will not be able to resolve any DNS lookups.
- [x] The outbound rules do not allow for HTTP traffic to leave the instance, so inbound HTTP requests will fail because the clients will never get HTTP responses.
- [ ] The incoming SSH port should not be open to the public. Limit SSH to a single IP address or IP range of controlled addressed, or use a VPN to access the VPC for this server.
- [ ] The all incoming TCP ports are exposed, which overrides the HTTP and SSH rules and exposes all TCP ports to the public internet.

#### Q56. An EC2 instance running a WordPress site keeps getting hacked, even though you have restored the server several times and have patched WordPress. What AWS service can help you detect and prevent further attacks?

- [ ] CloudWatch
- [x] GuardDuty
- [ ] Shield
- [ ] Security Advisor

#### Q57. A nontechnical client wants to migrate a WordPress site to AWS from a private server managed by a third-party hosting company. Which AWS service should you recommend to migrate the site to?

- [ ] CloudFront
- [ ] An EC2 instance launched from the official WordPress AMI
- [ ] S3
- [x] Lightsail

#### Q58. Your company has on-premise servers with an existing onsite backup solution that also replicates backups to another campus on the other side of the country with its own on-site backup solution. You have been asked to create a third level of redundancy by also storing these backups in the cloud. In the event of a primary and secondary backup failure, your boss wants to know that the cloud backups can be accessible as fast as possible to reduce downtime during the recovery. What S3 storage class do you recommend for cost and performance?

- [ ] S3 Standard
- [ ] S3 Intelligent-Tiering
- [ ] S3 Glacier
- [x] S3 One Zone-Infrequent Access

#### Q59. Which big data store will let you store large streams of user activity data coming from both web and mobile applications?

- [ ] Neptune
- [ ] Aurora
- [ ] RDS for SQL Server
- [x] Redshift

#### Q60. What option is best for Auto Scaling your EC2 instances for predictable traffic patterns?

- [x] scale based on a schedule
- [ ] manual scaling
- [ ] scale based on demand
- [ ] maintain current levels at all times

#### Q61. You are migrating an on-premise RabbitMQ cluster into AWS. Which migration path should you choose for ease of both maintenance and deployment?

- [ ] Rewrite the parts of your application that use RabbitMQ to use SQS.
- [ ] Launch a RabbitMQ cluster with EC2 instances using a supported AMI.
- [ ] Rewrite the parts of your application that use RabbitMQ to use Kinesis.
- [x] Rewrite the parts of your application that use RabbitMQ to use Amazon MQ.

#### Q62. When creating a new RDS instance, what does the Multi-AZ option do?

- [ ] replicates backups of your database to S3 and makes them available across regions to prevent against any data loss
- [x] creates a second passive database instance within the same region that will become the primary database during a failover
- [ ] creates a highly available database cluster that will host your database cluster in at least two regions
- [ ] creates another database instance in another region and keeps a hot standby active to failover to during regional failures

#### Q63. What is the best EC2 instance class for a server that continuously has a heavy CPU load?

- [x] C5
- [ ] T2
- [ ] R5
- [ ] H1

#### Q64. Your application performance management (APM) system can read the status of your CloudWatch monitors and perform scripted actions. When the CloudWatch metric StatusCheckFailed enters a failed state (a value of 1), you would like your APM to automatically repair the instance. Which script do you use?

- [x] A

```
aws ec2 stop-instances --instance-ids i-0b263919b6498b123
aws ec2 start-instances --instance-ids i-0b263919b6498b123
```

- [ ] B

```
aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
```

- [ ] C

```
aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
wait 30
aws ec2 start-instance --instance-ids i-0b263919b6498b123
```

- [ ] D

```
aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
aws ec2 start-instances --instance-ids i-0b263919b6498b123
```

#### Q65. What is wrong with the third incoming security group rule, which allows all traffic from sg-269afc5e to go to an Ubuntu EC2 instance configured as a web server?

![065](https://user-images.githubusercontent.com/33999631/179728393-8a2636ea-04e7-4597-b0cc-8150e2bc91de.png?raw=png)

- [ ] All traffic on all ports is being denied into this instance, which overwrites the HTTP rule and makes it redundant.
- [x] The instance was launched with the default security group, but there is no way for an administrator to SSH into the instance.
      Add another rule that allows for SSH access from a secured source, such as a single IP or a range of managed IP addresses.
- [ ] There is nothing wrong with this security group rule. Assuming that sg-269afc5e is applied to other resources that are properly
      secured, this rule allows all traffic to pass through that is also assigned security group sg-269afc5e.
- [ ] All traffic on all ports are allowed into this instance. This exposes the instance to all public internet traffic and
      overwrites the incoming HTTP rule.

#### Q66. You have a VPC that has a public and private subnet. There is a NAT gateway in the public subnet that allows instances in the private subnet to access the internet without having public exposure outside of the VPC. What should the routing tables be for the private subnet?

![image](images/003.png?raw=png)

- [x] A

```
Destination 1: 10.0.0.0/16, Target 1: local;
Destination 2: 0.0.0.0/0, Target 2: nat-09b4832
```

- [ ] B

```
Destination 1: 10.0.0.0/24, Target 1: local;
Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6
```

- [ ] C

```
Destination 1: 10.0.0.0/24, Target 1: subnet-1948ba2;
Destination 2: 0.0.0.0/0, Target 2: nat-09b4832
```

- [ ] D

```
Destination 1: 10.0.0.0/16, Target 1: vpc-12bd09ac2;
Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6
```

#### Q67. To comply with auditing requirements of some compliance standards, which AWS tool can be enabled to maintain an audit log of access and changes to your AWS infrastructure?

- [x] CloudTrail
- [ ] CloudWatch
- [ ] AWS Audit and Compliance Tool
- [ ] GuardDuty

#### Q68. You have an application that generates long-running reports, stores them in an S3 bucket, and then emails the user who requested the report with a link to download it. What is the best practice for storing the report data in S3?

- [ ] Create a public S3 bucket. When your application creates the report object in S3, generate two randomly generated long
      folder names and place the file within the deepest subfolder. Set the retention policy on the object to one hour and email this link to
      the user. The link will be active for one hour.
- [ ] Create a public S3 bucket. Use a hash of the user's email address and the date and time the report was requested to generate a
      unique object name. Email this link to the user and have a scheduled task run within your application to remove objects that are older
      than seven days.
- [x] Create a private S3 bucket. The link in the email should take the user to your application, where you can verify the active user
      session or force the user to log in. After verifying the user has rights to access this file, have the application retrieve the object
      from S3 and return it in the HTTP response. Delete the file from the S3 bucket after the request is completed.
- [ ] Create a private S3 bucket. The link in the email should take the user to your application, where you can verify the active user
      session or force the user to log in. Set the report object in S3 to public. Show the user a "Download" button in the browser that links
      to the public object.

#### Q69. When sending a large volume of email through SES, what is the most important set of metrics to monitor?

- [x] your complaint and bounce rates
- [ ] opens and clicks
- [ ] clicks and deliveries
- [ ] sending volume over the past 15 minutes and over one day to watch for billing spikes

#### Q70. You are going to host an application that uses a MySQL database. Which database should you select if you don't want to manage scaling or database administration tasks?

- [ ] Launch an AMI image from the marketplace containing a preconfigured MySQL server.
- [x] Aurora
- [ ] RDS for MySQL
- [ ] Redshift

#### Q71. A form in web application is sending sign-up data to "http://example.com/signup/new?source=web" and this data needs to be handled by an ECS service behind Application Load Balancer (ALB). Which ALB rule will route this request?

![image](images/004.png?raw=png)

- [ ] A

```
IF (all match)
    Path is /signup*
    Query string is signup:new
Then
    Forward to ecs-cluse-service <there is a typo - yes!
```

- [ ] B

```
IF (all match)
    Path is /sign/new/&
    Query request method is POST
Then
    Forward to ecs-cluse-service
```

- [ ] C ...One more with POST
- [x] D ...Only one with Get

#### Q72. Which AWS service can host the web application server for a WordPress site?

- [ ] S3
- [x] Elastic BeanStalk
- [ ] ElasticCache
- [ ] CloudFront

#### Q73. What does the following AWS CLI `create-service` command for ECS do?

```
aws ecs create-service \
 --cluster production \
 --service-name rest-api \
 --task-definition rest-api:1 \
 --desired-count 2 \
 --launch-type "FARGATE" \
 --network-configuration \
 "awsvpcConfiguration={subnets=[subnet-0b29129ab],securityGroups=[sg-0b29129ab]}"
```

- [ ] changes the security groups of the running **rest-api** task
- [ ] creates a cluster called **production** and launches two containers into Fargate with the **rest-api** task definition
- [x] launches two containers onto Fargate into the existing **production** cluster using the **rest-api** task definition
- [ ] creates a service definition for the **rest-api** task; put two containers on the production cluster when launched **ecs-cli** up command

#### Q74. You want to make your public API quickly accessible from all regions. What is the best way to do this?

- [ ] Create a single API gateway endpoint in a central region.
- [ ] Create a private API gateway endpoint for each region.
- [ ] Create a regional API gateway endpoint for each region.
- [x] Create edge-optimized API gateway endpoints and deploy them to a CloudFront network.

#### Q75. What type of data solution should you use for data coming from nonrelational and relational data from IoT devices, websites, mobile apps, etc.?

- [ ] Amazon DynamoDB
- [x] AWS Lake Formation
- [ ] Amazon Redshift
- [ ] Amazon Aurora

#### Q76. You have an analytics suite that produces reports about the usage patterns of your web application. After completing your migration to AWS and using Application Load Balancer to balance the load across your web application, your marketing department noticed that location-based reports on the web traffic only show traffic originating from a single location. What is the problem?

- [ ] Use a Classic Load Balancer, not Application Load Balancer.
- [x] Application Load Balancer does not preserve the original source IP address. The analytics software needs to be configured to look at the 'X-Forwarded-For' HTTP request header for the correct source IP address.
- [ ] Application Load Balencer has to be configured to retain the source IP address of the traffic it is forwarding. Create a policy that enables ProxyProtocol support and attach it to the ALB using the AWS CLI.
- [ ] Configure the web server EC2 instances to only have private IP addresses. The public IP addresses of the instances are being recorded into the web server logs, bug only ALB should have a public interface and it will route traffic to instances via the private interface.

#### Q77. What is `not` a default user of a common Linux instance launched from an AMI?

- [ ] ubuntu
- [x] system-user
- [ ] ec2-user
- [ ] admin

[Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)

#### Q78. You have replicated the infrastructure that serves the backend API for your web application across regions to better serve your customers in the US and the EU. What is the best way to direct your web application at the nearest data center?

- [x] Use Route 53 with geolocation lookups to direct traffic between the two regions.
- [ ] Create a WAF redirection rule that redirects traffic at the EU data center if the source IP comes from certain countries.
- [ ] Purchase a country domain extension and direct your users to the correct site, such as example.com and example.co
- [ ] Have your front-end application test the latency between each data center and use the data center that is responding the fastest.

[Reference](https://aws.amazon.com/premiumsupport/knowledge-center/geolocation-routing-policy/)

#### Q79. You have recently launched your new web product and are expecting 1,000 new users each month. However, you have just received word from the CEO that your product will be featured at an upcoming conference covered by several media outlets, and this could lead to 20,000 new users over the next week. How do you plan for a sudden increase in traffic?

- [ ] Replicate your infrastructure across two regions. You will harden the application to a regional failure and you will double your capacity.
- [ ] Take an AMI image of a front-end server to save your configuration and then add more servers to your cluster pror to the conference. Remove the servers from the cluster after the spike from the conference.
- [ ] Test to determine your throughput and how many users you can support. Develop a scaling plan for your front end, microservices, and database based on CloudWatch metrics that align with the tested bottlenecks.
- [x] Use Auto Scaling groups to create more front-end servers when the CloudWatch metrics for CPU usage on a single instance rise above 80% for five minutes.

[Reference](https://aws.amazon.com/ec2/autoscaling/)

#### Q80. How do you connect via SSH to a Linux EC2 instance with an EBS volume if you lost your key pair?

- [ ] Stop the instance and create an AMI image. Launch the image using a new key pair.
- [ ] Contact AWS support. A support specialist can remotely restore access to your instance and send you a new key pair.
- [ ] You can not connect to this EC2 instance. The key pair is displayed only one time. If you lose it, you have lost all access to this instance. Connect the EBS volume to another instance to recover your files.
- [x] Attach the EBS volume to a temporary instance launched with a new key pair, and overwrite ~/.ssh/authorized_keys using the same file from the new instance.

[Reference](https://medium.com/the-10x-dev/how-to-recover-access-login-to-your-aws-instance-after-losing-your-pem-keypair-file-e0d31bae2da4)

#### Q81. Your on-premise data center (172.16.128.0/24) is already connected to your AWS VPC (10.0.0.0/16) by a customer gateway. You wish to connect another data center for a company you just acquired (172.16.130.0/24) to your VPC as shown in the image. What is the best way to create this link?

![image](images/Q80.png?raw=png)

- [ ] Establish a connection between your two data centers and connect the second data center to the first through a private tunnel. Traffic will flow from the second data center and then through the first data, and then into AWS.
- [ ] Create a second customer gateway and configure your VPN client at your second data center to connect to the virtual private gateway.
- [x] Create a second virtual private gateway (VPG) and attach it to the VPC. Create a customer gateway for the new virtual private gateway and use your VPN client at your second data center to establish a connection to the VPG.
- [ ] You can not have more than one customer gateway per VPC, so the proposed solution will not work. Create a second VPC with a virtual private gateway and a customer gateway. Bridge the two VPCs using VPC peering.

#### Q82. You are migrating a 200 GB database from an on-premise SQL Server to RDS for SQL Server. The database needs to have minimal downtime during the migration. What is the best practice for migrating this database?

- [ ] Close all existing connections to the SQL Server database and use Database Migration Service to transfer the data to RDS.
- [x] Use Database Migration Service to replicate the database to RDS and keep it in sync during the migration. Repoint your applications to use the new RDS endpoint.
- [ ] Detach the SQL Server database during the migration. Take a backup of the database and use SQ with Accelerated Transfer to upload the backups to S3. Restore the backups to the RDS instance.
- [ ] Use the Import and Export wizard within SQL Server Enterprise Manager to create an export task and export the tables to the RDS instance.

[Reference](https://aws.amazon.com/dms/)

#### Q83. You have enabled Multi-Factor Authentication (MFA) for your AWS root account and you lost your MFA device. What do you need to do to recover access to your account?

- [ ] You cannot recover access to your AWS root account. Contact AWS support.
- [x] An email will be sent to the email address on file to verify ownership of the account. You will then need to provide the phone number on the account.
- [ ] An email will be sent to the email address on file. After clicking in the link in your email, provide one of the MFA recovery codes that were created when MFA was enabled.
- [ ] Use the AWS CLI with the root account access token to disable MFA on the root account. Then use the CLI to set a new password on the root account.

[Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html)

#### Q84. How do you assign an Elastic IP to several EC2 instances?

- [ ] In the VPC dashboard, click Elastic IPs. Select the Elastic IP and click Associate Address. Select each EC2 instance you wish to assign this address to.
- [ ] In the EC2 dashboard, click on EC2 instance. Under Actions, select networking > Manage IP Addresses. click to add a new IP address and type in the address of the Elastic IP. Repeat the process for each EC2 instance you want to assign this Elastic IP to.
- [ ] Use the AWS CLI and pass in several '--instance-id' options to hte aws ec2 assosiate-address command.
- [x] An elastic IP cannot be assigned to multiple EC2 instances. It can only be assosiated to a single EC2 instance.

[Reference](https://stackoverflow.com/questions/54742522/assign-multiple-ec2-instances-to-one-elastic-ip)

#### Q85. You created a VPC that has a public subnet and a private subnet. A web server was placed in the public subnet and a database server was placed in the private subnet. The web server is able to connect to the database server; however, the database server at 10.0.1.2 is unable to get software updates. What is the cause of this issue?

- [x] There is no NAT gateway for the private subnet, so the database server has no routes that give it public internet access to download software updates.
- [ ] The database server needs to be assigned a public address from the pool, or assigned an Elastic IP similar to the instance 10.0.0.2.
- [ ] The router is not configured properly on the VPC. Add a route to route table for the VPC that routes all traffic for 0.0.0.0/0 to the ID of the internet gateway.
- [ ] There is no egress-only internet gateway attached to the private subnet of the VPC.

#### Q86. Benefit of using S3 Glacier?

- [ ] access time
- [ ] store for small duration
- [x] cost
- [ ] cross-region

#### Q87. After installing AWS Amplify's CLI, what command allows the user to connect an AWS account with the local install?

- [ ] amplify admin
- [x] amplify configure
- [ ] amplify connect
- [ ] amplify init

[Reference](https://docs.amplify.aws/cli/start/install/#option-2-follow-the-instructions)

#### Q88. How do you limit access to an S3 bucket by source IP address?

- [ ] Create the S3 bucket as a target for Application Load Balancer. Use Web Application Firewall (WAF) to create a rule to limit access to the S3 bucket by source IP.
- [ ] You can not limit access to an S3 bucket by IP address.
- [ ] In the preperties of the S3 bucket, add an access control option that limit access to the bucket by source IP address. Input the list of IPs into dialog.
- [x] Create a bucket policy with a condition that limit access to a list of approved IP addresses. Attach this policy to the bucket.

#### Q89. What is the benefits of using S3 Glacier for storage?

- [ ] granual fetching
- [ ] cross-region caching
- [ ] speed of access
- [x] cost

#### Q90. Which of these AWS services can be related to Lambda via a trigger?

- [ ] Cognito Sync Trigger, SNS
- [ ] SNS, SQS
- [x] all of these answers
- [ ] SQS, DynamoDB

#### Q91. When creating a RESTful API into a DynamoDB table, which is the right service to facilitate this?

- [ ] API Sync
- [ ] AppSync
- [ ] CloudAPI
- [x] API Gateway

[Reference](https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/)

#### Q92. Which AWS service is valid data source for AppSync?

- [x] DynamoDB table
- [ ] ElastiCache
- [ ] none of these answers
- [ ] Step Functions

[Reference](https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions)

#### Q93. If a single instance has failed to launch within 24 hours due to some issues during a set up of Auto-scaling. Then what will happen to the Auto-Scaling condition?

- [ ] Auto Scaling will continue to launch the instance for straight 3 days
- [x] The Auto Scaling group will be automatically terminated.
- [ ] In a separate region Auto Scaling will start an instance
- [ ] Auto Scaling will remove the scaling process

#### Q94. Point out the wrong statement.

- [ ] Amazon Machine Instances are sized at various levels and rented on a computing/hour basis
- [ ] The metrics obtained by CloudWatch may be used to enable a feature called Auto Scaling
- [ ] A number of tools are used to support EC2 services
- [x] None of the mentioned

#### Q95. In terms of Amazon VPC design, a VPC with a single public subnet is ideal for which of the following application designs?

- [x] A single-tier application
- [ ] A serverless application
- [ ] A microservice application
- [ ] A multi-tier application

#### Q96. If you stop and restart an EC2 instance, does it retain its private IP address?

- [x] Yes, the instance retains its private IP addresses
- [ ] No, it retains only the public IP addresses
- [ ] No, it retains only the Elastic IP addresses
- [ ] No, it does not retain its private IP addresses

#### Q97. All the Amazon EC2 instances you launch into a nondefault VPC are **\_** by default.

- [ ] stateless
- [ ] protected
- [ ] public
- [x] private

#### Q98. When you launch an instance into a dedicated-tenancy VPC, what happens?

- [x] Your instance is automatically a Dedicated instance, regardless of the instance's specific tenancy attribute
- [ ] You receive an error message notifying you that you must set your instance's tenancy attribute to dedicated
- [ ] Your instance launch fails, but AWS prompts you to launch a new one with the tenancy attribute set to dedicated
- [ ] Your instance launch fails immediately

#### Q99. Use the **\_** protocol in a VPC security group to communicate with a DB instance.

- [ ] SSH
- [ ] SSL
- [x] TCP
- [ ] UDP

#### 100. Which is default user in Ec2 Linux-red hat/amazon.

- [ ] root
- [ ] Ec2user
- [x] ec2-user
- [ ] linux

#### Q101. When using Systems Manager, you can create policies through Systems Manager \_\_\_\_.

- [ ] Policy Manager
- [ ] State Manager
- [x] Documents
- [ ] Inventory

#### Q102. Businesses are increasingly moving towards hybrid cloud environments with automated IT. What Amazon EC2 State Manager feature is particularly useful for these companies?

- [ ] validity
- [x] consistency
- [ ] reliability
- [ ] redundancy

#### Q103. Your DevOps manager has noticed that there is a problem with the installation of the MySQL software in one of your Windows instances and asks you to repair it. What would be the recommended way to fix this issue with AWS Systems Manager?

- [ ] Write a Power Shell script that re-installs the msi file and run it with Run Command.
- [ ] Execute the AWS-ApplyPatchBaseline command.
- [ ] Allow State Manager to automatically fix it on batch.
- [x] Use Run Command to execute the AWS-InstallApplication document.

#### Q104. Within EC2 Systems Manager, you can use Patch \_\_\_\_ to pick the patches you want to install with your instances.

- [ ] Levels
- [ ] Manager
- [x] Baselines
- [ ] Policy

#### Q105. When is an AWS Batch job's status runnable?

- [ ] When a submitted job's resources are being deployed
- [ ] When a submitted job has been evaluated
- [x] When a submitted, evaluated job has zero dependencies outstanding
- [ ] When a submitted job is next in the job queue

#### Q106. Which statement regarding AWS Batch automated retries is correct?

- [ ] Each job is provided a single job attempt by default, but a user can modify this to unlimited attempts if desired.
- [ ] Each job is provided a single job attempt by default, but the AWS Batch job scheduler may modify this after evaluating the submitted job.
- [x] Each job is provided a single job attempt by default, but a user can modify this to as many as 10 attempts if desired.
- [ ] Each job is limited to a single attempt before being classified as succeeded or failed.

#### Q107. What AWS Batch job parameter can you specify to prevent an unsuccessful job from being stuck in a loop?

- [x] The duration of job timeout
- [ ] A resource expenditure cap
- [ ] The number of automated job retries
- [ ] An AWS Batch job agent

#### Q108. In which of the following AWS Batch components can a user set a priority level, for time-sensitive or low-priority jobs?

- [ ] Within the job scheduler
- [ ] Within the job itself
- [ ] Within the job definition
- [x] Within a job queue

#### Q109. You may invalidate up to **\_** path files each month from Amazon CloudFront at no additional charge.

- [ ] 100
- [ ] 5,000
- [x] 1,000
- [ ] 500

#### Q110. Which of the following is recommended when you want to analyze Access Logs of a single stream more quickly and accurately for a given period?

- [ ] Check all the log files you receive for a given period one by one.
- [ ] Analyze all the log files line by line.
- [x] Combine all the log files you receive for a given period into one file.
- [ ] Compare log files with Amazon CloudWatch results.

#### Q111. In regard to Amazon CloudFront, when you create a new web distribution, the Path Pattern for the default cache behavior is set to \***\*\_\*\***.

- [x] `*` (all files) and cannot be changed
- [ ] HTML files and cannot be changed
- [ ] HTML files and can be changed
- [ ] `*` (all files) and can be changed

#### Q112. In Amazon CloudFront, if you add a CNAME for www.example.com to your distribution, you also need to create (or update) a CNAME record with your DNS service.

- [x] TRUE
- [ ] False, you cannot add a CNAME to your distribution.
- [ ] False, you should add a CNAME record with your CloudWatch metrics and not the DNS.
- [ ] False, it is not necessary to create a CNAME record with your DNS service as it is done automatically by Amazon.

#### Q113. Which of the following statements is true of Amazon CloudFront when you can control how long your objects stay in a CloudFront cache before it forwards another request to your origin?

- [x] All answers listed are correct.
- [ ] Reducing the duration allows you to serve dynamic content.
- [ ] Increasing the duration means your customers get better performance.
- [ ] A longer duration also reduces the load on your origin.
