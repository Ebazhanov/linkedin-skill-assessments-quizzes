## AWS Assessment

#### Q1. You have an application using a 100 GB MySQL database that you are migrating into AWS. What should you consider when deciding between whether to host the database on RDS for MySQL or Aurora?

- [ ] cost
- [ ] ease of maintenance vs. granularity of control
- [x] all of these answers
- [ ] the current storage engine used by the application, such as InnoDB or MyISAM

#### Q2. Which database is a NoSQL database type that can quickly store and retrieve key-value pairs?

- [ ] Aurora
- [ ] Neptune
- [ ] ORDS for MySQL
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
- [ ] Simple Queue Service (SOS)
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
- [ ] Use a VPN or VPC peering to establish a connection between the VPCs in each region. Install SOL Server Enterprise Edition on EC2 instances in each region and configure an Always On availability group.
- [ ] Use RDS for SQL Server 2016 or 2017 Enterprise Edition. Enable Multi-AZ support and select the Mirroring/Always On option. Select another region for the mirroring option
- [ ] You can not set up an active-active architecture for SQL Server that spans geographic regions.

#### Q10. What does it cost to launch an EC2 instance from the AWS Marketplace?

- [ ] All images in the AWS Marketplace incur additional hourly fees in addition to the charges from the instance size you select.
- [ ] You can only launch images that were created by other users on your AWS account, so you pay only for the instance size you select and the S3 storage costs for the base image.
- [x] Each image has its own pricing that could either be free, or include charges for software licensing costs. You will also pay for the instance the image runs on
- [ ] All images in the AWS Marketplace contain only open-source software with no additional fees and are created by other AWS users. You will pay only for the instance size you select.

#### Q11. When using an ECS cluster with EC2 instances, what maintenance tasks should you perform on the EC2s?

- [ ] The instances created by ECS do not have patches that need to be applied; however you should make sure your containers contain any important security updates,
- [ ] Refresh the cluster with instances built from the latest ECS AML
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

```
    {
        "title":"The Avengers",
        "year": 2012,
        "cast" : ["Mark Ruffalo", "Robert Downey, Jr."],
        "genres" : ["Action"]
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
- [ ] Lambda only allows you to write functions in JavaScript
- [ ] Lambda does not use servers, so it can only return the same request to every user,
- [x] Lambda is stateless, so it won't remember who a user is in between requests

#### Q20. A principle of DevOps is to view infrastructure as code. Which AWS service allows you to script your AWS infrastructure?

- [ ] CloudTrail
- [x] CloudFormation
- [ ] AWS Config
- [ ] AWS Service Catalog

#### Q21. You created a Windows EC2 instance with a public IP address and installed SQL Server. When attempting to connect to SQL Server from SQL Server Enterprise Manager on your local computer, the Windows EC2 instance is unable to establish a connection to the server. What is the first thing you should check?

- [ ] Check the routing tables for the VPC.
- [x] Verify that the assigned security groups allow TCP port 1433 traffic from your current IP address.
- [ ] Check the policies within Windows Firewall
- [ ] Verify that you are connecting to the instance using a user that is not sa.

#### Q22. You are hosting an application configured to stream media to its clients on TCP ports 3380-3384, 3386-3388, and 3390. The Inbound tab below shows three incoming security group policies attached to this instance. Which policy should you use?

- [ ] The rule that exposes TCP ports 3380-3390 would also publicly expose port 3389 (RDP) to the entire internet. Write separate rules to only expose the needed ports.
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

- [х] Restore the instance from the last AMI image. System status checks indicate that the filesystem on the instance is corrupted.
- [ ] Stop and start the instance. This will move the instance to another host.
- [ ] Contact AWS support. Failing a system status check indicates a failure in the underlying hardware and must be addressed by an AWS representative.
- [ ] Reboot the instance. This will stop and start the instance and move it to another host.

#### Q25. You have several on-premise servers and would like to store your offsite backups on AWS. What fully managed backup service can you use to ship your backups to AWS?

- [ ] Windows Server 2016 supports S3 as a target when using storage replicas.
- [х] Use Storage Gateway.
- [ ] Sync files directly to S3 with the AWS CLI.
- [ ] Use the RDS console to force a reboot of the database instance so that the primary server becomes the master server again.

#### Q26. What is the best practice for creating a highly available PostgreSQL database in RDS that can sustain the loss of a single AWS region?

- [ ] PostgreSQL cannot be replicated across regions. Restore the database backups from an S3 bucket and repoint your database connections to the new instance.
- [х] Create Read Replicas in other AWS regions. You can designate a new master database from any of the read replicas until the regional failure is resolved.
- [ ] Verify that your instance is configured for Multi-AZ support. Database changes will be automatically synced to another region in the event of a failure and RDS will automatically select a new master until the regional failure is resolved.
- [ ] Create Read Replicas in other AWS regions. Ensure read operations against the database occur on an available Read Replica, and send write operations to another region if you need to promote a Read Replica to a standalone database if the master is down.

#### Q27. You created a new Linux EC2 instance and installed PostgreSQL but you are not able to establish a connection to the server from your local computer. What steps do you take to resolve this issue?

- [x] Create a security group rule that allows all traffic from 0.0.0.0/0. This will verify whether or not another rule is denying the traffic.
- [ ] Verify that the assigned security groups allow traffic from your IP address to port 5432. Verify that PostgreSQL is configured to listen to external traffic and is bound to the public interface.
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
    "IpAddress": {"aws:SourceIp": "68.249.108.0/24"},
    "NotIpAddress": {"aws:SourceIp": "68.249.108.128/32"}
  }
}
```

- [ ] bucketpolicy1 allows any user to perform any action on the objects in the userreports bucket, but limits the objects to read-only permissions for anyone coming from 68.249.108.0 to 68.249.108.255 - except 68.249.108.128.
- [ ] bucketpolicy1 allows any user coming from the IP range of 68.249.108.0 to access objects in the userreports bucket and denies access to 68.249.108.128.
- [ ] bucketpolicy1 allows any user to perform any action on the objects in the userreports bucket - except anyone coming from the IP of 68.249.108.128.
- [x] bucketpolicy1 allows any user coming from the IP range of 68.249.108.0 to 68.249.108.255 to access objects in the userreports bucket-except anyone coming from the IP of 68.249.108.128.
