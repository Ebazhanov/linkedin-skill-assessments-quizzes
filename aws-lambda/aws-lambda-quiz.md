## AWS Lambda

#### Q1. How can you increase the CPU resources for your Lambda?

- [ ] Increase the configured CPU value
- [ ] Increase the configured timeout value
- [x] Increase the configured memory value
- [ ] Increase the configured concurrency value

#### Q2. How can additional code or content be provided for your Lambda?

- [ ] blocks
- [x] layers
- [ ] aliases
- [ ] handlers

#### Q3. How can Step Functions call Lambdas?

- [ ] in sequence
- [x] both of these answers
- [ ] neither of these answers
- [ ] in parallel

#### Q4. Which AWS CLI command invokes a function?

- [ ] aws lambda invoke --function ReturnBucketName outputfile.txt
- [ ] aws lambda execute --function-name ReturnBucketName outputfile.txt
- [x] aws lambda invoke --function-name ReturnBucketName outputfile.txt
- [ ] aws lambda execute --function ReturnBucketName outputfile.txt

#### Q5. What adds tracing capabilities to a Lambda?

- [ ] AWS Trace
- [ ] CloudStack
- [ ] CloudTrail
- [x] AWS X-Ray

#### Q6. You need to build a continuous integration/deployment pipeline for a set of Lambdas. What should you do?

- [ ] Create configuration files and deploy them using AWS CodePipeline.
- [ ] Create CloudFormation templates and deploy them using AWS CodeBuild
- [ ] Create configuration file and deploy using AWS CodeBuild
- [x] Create CloudFormation templates and deploy them using AWS CodePipeline.

#### Q7. What can you use to monitor function invocations?

- [ ] API Gateway
- [ ] S3
- [ ] SAS
- [x] CloudTrail

#### Q8. It is AWS best practice to enable Lambda logging by which of these methods.

- [ ] Use S3 metrics and CloudWatch alarms
- [ ] Create custom metrics within your Lambda code.
- [ ] Create custom metrics within your CloudWatch code.
- [x] Use Lambda metrics and CloudWatch alarms.

#### Q9. What may be provided for environment variables?

- [ ] an SSL certificate
- [ ] a bitmask
- [x] an AWS KMS key
- [ ] an HTTP protocol

#### Q10. Lambdas allow for running of what other things?

- [ ] binaries.
- [x] all of these answers
- [ ] executables
- [ ] Shell scripts

#### Q11. In what style must you write Lambda code?

- [ ] MVC
- [ ] virtual
- [x] stateless
- [ ] protocol

#### Q12. How can a developer provide Lambda code?

- [ ] by uploading a .zip file
- [x] all of these answers
- [ ] by editing inline
- [ ] from an S3 bucket

#### Q13. You are performance-testing your Lambda to verify that you set the memory size adequately. Where do you verify the execution overhead?

- [ ] CLoudWatch logs
- [ ] DynamoDB logs
- [ ] S3 logs
- [x] Lambda logs.

#### Q14. What facilitates continuous delivery of Lambdas?

- [ ] CodeStack
- [ ] ElasticStack
- [ ] Mobile Hub
- [x] CodeDeploy

#### Q15. How are computing resources allocated to Lambdas?

- [x] proportionally
- [ ] equally
- [ ] periodically
- [ ] daily

#### Q16. You can restrict the scope of a user's permissions by specifying which two items in an IAM policy?

- [ ] resources and users
- [x] resources and conditions
- [ ] events and users
- [ ] events and conditions

#### Q17. What does Lambda logging include?

- [x] logging streams
- [ ] rotating streams
- [ ] logging events
- [ ] advancing log groups

#### Q18. What can AWS Amplify NOT do for a Lambda?

- [ ] create a Lambda
- [x] be an event source
- [ ] assign an IAM role
- [ ] delete a Lambda

#### Q19. How do you author a Lambda in a programming language that AWS does not support?

- [ ] Create a Lambda function with a custom runtime and reference the function in your Lambda
- [x] Create a Lambda layer with a custom runtime and reference the layer in your lambda
- [ ] You cannot use Lambda in this situation
- [ ] Create a Lambda function with a custom runtime

#### Q20. What are listed downstream resources based on?

- [ ] the execution policy
- [x] the Lambda configuration
- [ ] the Lambda nodes
- [ ] the IAM user

#### Q21. Which is an equivalent and valid tag for a pair of Lambdas?

- [ ] department:Sales,department:Sales
- [x] department:Sales,department:sales
- [ ] aws:demo;aws:demo
- [ ] aws:demo;aws:DEMO

#### Q22. Outbound connections from Lambdas must be `_`.

- [ ] neither of these answers
- [ ] UDP/IP
- [ ] TCP/IP
- [x] both of these answers

#### Q23. How are CloudWatch actions configured?

- [ ] automatically
- [ ] none of these answers
- [x] manually
- [ ] ad hoc

#### Q24. You are testing your stream-based application and the associated Lambda. AWS best practice advises you to test by varying what?

- [ ] stream and record sizes
- [ ] stream and shard sizes
- [x] batch and record sizes
- [ ] batch and shard sizes

#### Q25. You need to make your Lambda available to services in multiple VPCs. What do you do?

- [ ] Place each subnet in a VPC. Associate all subnets to your Lambda.
- [ ] Place all subnets in a VPC. Associate all subnets to your Lambda.
- [ ] Configure your Lambda to be available to multiple VPCs.
- [x] Configure all application VPCs to be peered.

#### Q26. How is the cost associated with Lambda function calculated?

- [ ] number of function calls
- [ ] amount of code run
- [x] compute time
- [ ] amount of infrastructure used

#### Q27. What is the fastest way to get started with Lambda?

- [ ] Author a Lambda from scratch.
- [x] Use a blueprint.
- [ ] Use a .zip deployment package.
- [ ] Use the serverless app repository.

#### Q28. Where is the disk space allocated for Lambda functions?

- [x] /tmp
- [ ] /default
- [ ] /temp
- [ ] /ds

#### Q29. How do you stop a running Lambda that is stuck in a recursive loop?

- [ ] Delete the function.
- [x] Set the function concurrent execution limit to 0 while you update the code.
- [ ] Reset the function.
- [ ] Set the function concurrent execution limit to 100 while you update the code.

#### Q30. What is AWS best practice for Lambda configuration?

- [x] Overprovision memory to run your functions faster and reduce your costs. Do not overprovision your function timeout settings.
- [ ] Overprovision memory and your function timeout settings to run your functions faster and reduce your costs.
- [ ] Do not overprovision memory. Overprovision your function timeout settings to run your functions faster and reduce costs.
- [ ] Do not overprovision memory. Do not overprovision your function timeout settings to run your functions faster and reduce costs.

#### Q31. Basic Lambda permissions include permissions for what?

- [ ] removing log groups
- [ ] none of these answers
- [ ] creating log groups
- [x] updating log groups

#### Q32. How are environment variables stored?

- [ ] DynamoDB tables
- [x] key-value pairs
- [ ] S3 buckets
- [ ] none of these answers

#### Q33. You need to use a Lambda to provide backend logic to your website. Which service do you use to make your Lambda available to your website?

- [ ] S3
- [x] API Gateway
- [ ] X-Ray
- [ ] DynamoDB

#### Q34. You are creating a Lambda to trigger on change to files in an S3 bucket. Where should you put the bucket name?

- [ ] in the Lambda function code
- [x] in a Lambda environment variable
- [ ] in the Lambda tags
- [ ] in another S3 bucket

#### Q35. What action is needed before you can test a Lambda?

- [ ] Deploy the Lambda
- [ ] Export the function
- [ ] none of these answers
- [x] Configure a test event

#### Q36. What kind of packages can you use with Node.js for Lambdas?

- [ ] Fleece
- [x] NPM
- [ ] none of these answers
- [ ] Pod

#### Q37. Lambdas are monitored by default using which service?

- [ ] CloudTrail
- [x] CloudWatch
- [ ] CloudFormation
- [ ] LogWatch

#### Q38. What can trigger a Lambda function execution?

- [ ] a table definition
- [ ] queue isolation
- [ ] STS Write
- [x] an SNS topic

#### Q39. You need to set an S3 event trigger on your Lambda to respond when data is added to your bucket from another S3 bucket. Which event type do you configure?

- [ ] POST
- [ ] "All object create events"
- [x] PUT
- [ ] COPY

#### Q40. To make Lambdas more testable, it is AWS best practice to separate which of these?

- [ ] Lambda configuration from logging code
- [ ] Lambda handler from logging code
- [x] Lambda handler from core logic
- [ ] Lambda configuration from core logic

#### Q41. What is included in an exported Lambda deployment package?

- [ ] YAML definition
- [ ] CloudFormation stack configuration
- [ ] SAML deployment stack
- [x] Zip file of all related files

#### Q42. When can you change the execution role of a Lambda?

- [ ] only at creation
- [ ] only before deployment
- [ ] never
- [x] anytime via configuration

#### Q43. What is the relationship between SAM template and CloudFormation template files?

- [ ] SAM templates have some overlap with CloudFormation templates. Both SAM and CloudFormation templates include resource types that are not in the other type of template.
- [x] SAM templates are a superset of CloudFormation templates. SAM templates include additional resource types.
- [ ] CloudFormation templates are a superset of SAM templates. CloudFormation templates include additional resource types.
- [ ] SAM templates are a different name for CloudFormation templates. Both template types include the same resource types.

#### Q44. What service deploys Lambdas regionally?

- [ ] EdgeCloud
- [ ] CloudEdge
- [x] CloudFront
- [ ] CloudStack

#### Q45. What programming language does AWS Lambda support?

- [ ] custom
- [x] all of these answers
- [ ] Java
- [ ] Ruby

#### Q46. You need to setup a mechanism to put controls in place to notify you when you have a spike in Lambda concurrency. What should you do?

- [ ] Deploy a CloudTrail alarm that notifies you when function metrics exceed your threshold. Create an AWS budget to monitor costs.
- [x] Deploy a CloudWatch alarm that notifies you when function metrics exceed your threshold. Create an AWS budget to monitor costs.
- [ ] Deploy a CloudWatch alarm that notifies you when function metrics exceed your threshold. Create an AWS CostMonitor to monitor costs.
- [ ] Deploy a CloudTrail alarm that notifies you when function metrics exceed your threshold. Create an AWS CostMonitor to monitor costs.

#### Q47. You want to minimize cold start time for your Lambda. What do you do?

- [x] Add extra code to check if the transient cache, or the /tmp directory, has the data that you stored.
- [ ] Add extra code to check if the permanent cache, or the /cache directory, has the data that you stored.
- [ ] Do nothing. AWS minimizes cols start time by default.
- [ ] Create a warm-up Lambda that calls your Lambda every minute

[Reference](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/

#### Q48. When is Lambda code stored encrypted?

- [x] at rest
- [ ] at runtime
- [ ] at deployment
- [ ] non of these answers

[Reference](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-functions-and-layers.html)

#### Q49. When you use a resource-based policy to give a service, resource, or account access to your function, how can you apply the scope of that permission??

- [ ] at the function level
- [ ] at the alias or function level
- [x] at the version, alias, or function level
- [ ] at the version or function level

[Reference](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)

#### Q50. Lambda can read events from which other AWS services? (ref-https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)

- [ ] Kinesis, S3, and SQS
- [ ] Kinesis, S3, and SNS
- [ ] Kinesis, DynamoDB, and SNS
- [x] Kinesis, DynamoDB, and SQS

**Explanation**

- `Lambda can used for all services mentioned on the question: Kinesis, S3, SNS, SQS, DynamoDB. But as you can see in the reference, Lambda's responsibility and method invocation can be categorized by Lambda polling and Event Driven (synchronous invocation). When you implement an event-driven architecture, you grant the event-generating service permission to invoke your function in the function's resource-based policy. Then you configure that service to generate events that invoke your function. When you implement a Lambda polling architecture, you grant Lambda permission to access the other service in the function's execution role. Lambda reads data from the other service, creates an event, and invokes your function. According to this analytics, Kinesis-DynamoDB-SQS use same method invocation, Lambda polling.`

#### Q51. Via what can a Lambda be called?

- [x] all of these answers
- [ ] a DynamoDB trigger
- [ ] an API Gateway
- [ ] an S3 bucket event

**Explanation** (source google)

- `With DynamoDB Streams, you can trigger a Lambda function to perform additional work each time a DynamoDB table is updated. Lambda reads records from the stream and invokes your function synchronously with an event that contains stream records.`
- `These events are considered synchronous events. Simply put, it means that when somebody is calling an API Gateway, it will trigger your Lambda function. It's a synchronous event because your Lambda function has to respond to the client directly at the end of its invocation.`
- `You can use Lambda to process event notifications from Amazon Simple Storage Service. Amazon S3 can send an event to a Lambda function when an object is created or deleted.`

#### 52. which is use case of lambda ?

- [ ] Image processing
- [ ] web application
- [x] both
- [ ] Neither 1st and 2nd

#### Q53. Events are AWS resources that trigger the Lambda function. What data type is the SAM file Events property?

- [ ] Integer
- [ ] Float
- [x] Array
- [ ] String

#### Q54. A company is using an API built using Amazon Lambda, Amazon API Gateway, and Amazon DynamoDB in production. The developer has observed high latency during peak periods. Which approach would best resolve the issue?

- [ ] Increase the Lambda function timeout
- [ ] Route traffic to API Gateway using a Route 53 alias
- [ ] Disable payload compression for the API
- [x] Enable API Gateway stage-level caching

#### Q55. The AWS Serverless Application Model (AWS SAM) is a model that \_\_\_\_ .

- [x] defines serverless applications
- [ ] associates permissions policies
- [ ] creates Lambda functions
- [ ] packages deployment artifacts

#### Q56. The code that you want AWS Lambda to invoke as per some defined triggers is known as **\_**.

- [ ] the event source
- [ ] the downstream resource
- [ ] the log stream
- [x] the Lambda function

#### Q57. A developer has created a Lambda function to scrub real-time data of extraneous information and then send the scrubbed data to Kinesis for further processing and storage. Some of the data showing up in Kinesis seems to be inaccurate. What's the best way for the developer to debug this?

- [ ] Look directly at the Lambda Logs in CloudWatch
- [ ] Send the Lambda failures to a Dead Letter Queue
- [x] Use AWS X-Ray to step through the function
- [ ] Use Kinesis to write their own custom logging tool

#### Q58. Lambdas can be created **\_**.

- [x] All of these answers
- [ ] From scratch
- [ ] From the app repository
- [ ] Using a blueprint

#### Q59. You need to quickly understand execution times for two different Lambda functions with different invocation types: asynchronous and synchronous. What do you do?

- [x] Enable tracing, rerun the lambdas, and view in the lambda console
- [ ] View the logs in CloudTrail
- [ ] View the logs in CloudWatch
- [ ] Enable tracing, rerun the Lambdas, and view in the X-Ray console

#### Q60. Which tool would you use to test a Lambda locally?

- [ ] AWS SAM
- [ ] AWS CLI
- [ ] AWS CloudFormation
- [x] AWS SAM CLI

#### Q61. Your function failed to execute due to a timeout. What type of error is this?

- [ ] Caller
- [x] Runtime
- [ ] Request
- [ ] Account

#### Q62. A company will be modernizing their application which is currently running on Amazon Elastic Cloud Compute (EC2) instances. They have experience with scaling this infrastructure using Amazon EC2 Autoscaling. They want to move to serverless infrastructure consisting of an Amazon API Gateway that triggers Lambda functions. They are consulting you about scaling this new infrastructure. What should the company consider in order to make sure the serverless infrastructure scales to their needs?

- [ ] Enable Auto Scaling Groups for AWS Lambda to ensure that enough Lambda functions are ready to handle the incoming requests
- [ ] Throttle Lambda functions by configuring reserved concurrency, sending the excess traffic to Dead Letter Queues (DLQ) that will be handled when the request volume reduces.
- [x] Look at service limits for Amazon API Gateway and Lambda functions used in order to identify potential bottlenecks and balance performance requirements, costs, and business impact
- [ ] Do nothing. API Gateway and AWS Lambda are managed services that have built-in horizontal scaling, security, and high availability to handle unlimited amount of requests

**Explanation**

- `In serverless it is important to understand the service limits of all the services used end to end to understand the level of requests that can be handled.`

#### Q63. Can we use pakages with AWS Lambda?

- [ ] No, AWS Lambda does not support the use of external packages.
- [x] Yes, AWS Lambda supports the use of custom and NPM packages
- [ ] AWS Lambda only supports built-in packages.
- [ ] Packages can be used but require additional fees.

#### Q64. Are AWS Lambda functions available and to what extent?

- [ ] AWS Lambda functions are available 24/7 without any limitations.
- [ ] AWS Lambda functions are available but may experience scheduled downtimes.
- [x] AWS Lambda functions are highly available with redundancy and replications.
- [ ] AWS Lambda functions are available only during business hours.

#### Q65. Is there any default limit to be applied at a functional level?

- [ ] Yes, there is a default limit to be applied at a functional level.
- [x] No, there is no default limit to be applied at a functional level.
- [ ] The default limit depends on the AWS Lambda service plan.
- [ ] Functional limits are set by users during configuration.

#### Q66. How long can an AWS Lambda function execute?

- [ ] 60 seconds
- [x] 300 seconds
- [ ] 600 seconds
- [ ] 30 seconds

#### Q67. How does AWS Lambda secure my code?

- [ ] AWS Lambda stores code in plaintext without encryption
- [x] AWS Lambda encrypts and stores it in Amazon S3.
- [ ] AWS Lambda does not provide any security measures for code.
- [ ] AWS Lambda relies on third-party security tools for code protection.

#### Q68. Which languages are supported by AWS Lambda?

- [x] Python, C#, JavaScript and Java
- [ ] Ruby, PHP, Swift
- [ ] C++ and Rust
- [ ] # HTML and CSS
  In serverless it is important to understand the service limits of all the services used end to end to understand the level of requests that can be handled.

#### Q63. What does AWS Lambda mean?

- [ ] a) AWS Lambda is a database service offered by AWS.
- [x] b) AWS Lambda is a serverless computing service provided by AWS.
- [ ] c) AWS Lambda is a machine learning framework developed by AWS.
- [ ] d) AWS Lambda is an IoT platform developed by AWS.

#### Q64. What restrictions apply to AWS Lambda function code?

- [x] a) Lambda imposes restrictions on the use of outbound network connections.
- [ ] b) Lambda imposes restrictions on trace calls for debugging.
- [ ] c) Lambda allows unlimited TCP port 25 traffic.
- [ ] d) Lambda imposes restrictions on the execution time of functions.

#### Q65. How long can an AWS Lambda function execute?

- [ ] a) 60 seconds
- [x] b) 300 seconds
- [ ] c) 600 seconds
- [ ] d) 30 seconds

#### Q66. How does AWS Lambda secure my code?

- [ ] a) AWS Lambda stores code in plaintext without encryption.
- [x] b) AWS Lambda encrypts code and stores it in Amazon S3.
- [ ] c) AWS Lambda does not provide any security measures for code.
- [ ] d) AWS Lambda relies on third-party security tools for code protection.

#### Q67. Which languages are supported by AWS Lambda?

- [x] a) Python, C#, JavaScript, and Java
- [ ] b) Ruby, PHP, and Swift
- [ ] c) C++ and Rust
- [ ] d) HTML and CSS

#### Q68. What is the definition of Auto-Scaling?

- [ ] a) Auto-Scaling is a feature that automatically scales AWS Lambda functions.
- [x] b) Auto-Scaling is a feature that automatically scales AWS EC2 instances.
- [ ] c) Auto-Scaling is a feature that automatically scales AWS S3 storage.
- [ ] d) Auto-Scaling is a feature that automatically scales AWS RDS databases.

#### Q69. Is the infrastructure accessible on which the AWS Lambda runs?

- [ ] a) Yes, users have full access to the underlying infrastructure.
- [x] b) No, AWS Lambda abstracts the underlying infrastructure and does not provide access.
- [ ] c) Users have access to infrastructure but with limited permissions.
- [ ] d) Users can request access to infrastructure from AWS support.

#### Q70. Can I use packages with AWS Lambda?

- [ ] a) No, AWS Lambda does not support the use of external packages.
- [x] b) Yes, AWS Lambda supports the use of custom and NPM packages.
- [ ] c) AWS Lambda only supports built-in AWS packages.
- [ ] d) Packages can be used but require additional fees.

#### Q71. Are AWS Lambda functions available and to what extent?

- [ ] a) AWS Lambda functions are available 24/7 without any limitations.
- [ ] b) AWS Lambda functions are available but may experience scheduled downtimes.
- [x] c) AWS Lambda functions are highly available with redundancy and replication.
- [ ] d) AWS Lambda functions are available only during business hours.

#### Q72. Is there any default limit to be applied at a functional level?

- [ ] a) Yes, there is a default limit applied at a functional level.
- [x] b) No, there is no default limit applied at a functional level.
- [ ] c) The default limit depends on the AWS Lambda service plan.
- [ ] d) Functional limits are set by users during configuration.

#### Q73. You are using lambda (with large ram allocations) to process videos uploaded to S3 and to convert from their video format to H264. However the operation fails when dealing with particularly large video files. What is the cause of this?

- [x] The default 5 mintutes timeout.
- [ ] Lambda does not allow vedio encoding.
- [ ] s3 transfer bottlenecks
- [ ] s3 cannot talk to Lambda
