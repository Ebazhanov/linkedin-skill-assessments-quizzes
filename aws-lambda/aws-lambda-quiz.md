AWS LAMBDA Assessment
---------------------

#### Q1. How can you increase the CPU resources for your Lambda?
- Increase the configured CPU value
- Increase the configured timeout  value
- Increase the configured memory value <<<<<<--------------- CORRECT
- Increase the configured concurrency value

#### Q2. How can additional code or content can be provided for Lambda?
- blocks
- layers <<<<<<--------------- CORRECT
- aliases
- handlers

#### Q3. How can Step Functions call Lambdas?
- in sequence
- both of these answers  <<<<<<------------- CORRECT
- neither of these answers
- in parallel

#### Q4. Which AWS CLI command invokes a function?
- aws lambda invoke --function ReturnBucketName outputfile.txt
- aws lambda execute --function-name ReturnBucketName outputfile.txt
- aws lambda invoke --function-name ReturnBucketName outputfile.txt  <<<<<<<<------ CORRECT
- aws lambda execute --function ReturnBucketName outputfile.txt

#### Q5. What adds tracing capabilities to a Lambda?
- AWS Trace
- CloudStack
- CloudTrail
- AWS X-Ray   <<<<<<----- CORRECT

#### Q6. You need to build a continuous integration/deployment pipeline for a set of Lambdas. What should you do?
- Create configuration files and deploy them using AWS CodePipeline.
- Create CloudFormation templates and deploy them using AWS CodeBuild
- Create configuration file and deploy using AWS CodeBuild
- Create CloudFormation templates and deploy them using AWS CodePipeline. <<<<<<<<------ CORRECT

#### Q7. What can you use to monitor function invocations?
- API Gateway
- S3
- SAS
- CLoudTrail <<<<<<--------------- CORRECT

#### Q8. It is AWS best practice to enable Lambda logging by which of these methods.
- Use S3 metrics and CloudWatch alarms
- Create custom metrics within your Lambda code.
- Create custom metrics within your CloudWatch code.
- Use Lambda metrics and CloudWatch alarms. <<<<<<--------------- CORRECT

#### Q9. What may be provided for environment variables?
- an SSL certificate
- a bitmask
- an AWS KMS key  <<<<<<---------- CORRECT
- an HTTP protocol 

#### Q10. Lambda allows for running of what other things?
- binaries.
- all of these answers <<<<<-------------- CORRECT
- executables
- Shell scripts

#### Q11. In what style must you write Lambda code?
- MVC
- virtual
- stateless <<<<<<----------- CORRECT
- protocol

#### Q12. How can a developer provide Lambda code?
- by uploading a .zip file
- all of these answers   <<<<<<----------- CORRECT
- by editing inline
- from an S3 bucket

#### Q13. You are performance-testing your Lambda to verify that you set the memory size adequately. Where do you verify the exectuon overhead?
- CLoudWatch logs
- DynamoDB logs
- S3 logs
- Lambda logs. <<<<<<<<------ CORRECT

#### Q14. What facilitates continuous delivery of Lambdas?
- CodeStack
- ElasticStack
- Mobile Hub
- CodeDeploy <<<<<<<<------ CORRECT

#### Q15. How are computing resources allocated to Lambdas?
- proportionally  <<<<<------- CORRECT
- equally
- periodically
- daily

#### Q16. You can restrict the scope of a user's permissions by specifying which two items in an IAM policy?
- resources and users ???
- resources and conditions
- events and users
- events and conditions

#### Q17. What does Lambda logging include?
- logging streams
- rotating streams
- logging events
- advancing log groups

#### Q18. What can AWS Amplify NOT do for a Lambda?
- create a Lambda
- be an event source
- assign an IAM role
- delete a Lambda

#### Q19. How do you author a Lambda in a programming language that AWS does not support?
- Create a Lambda function with a custom runtime and reference the function in your Lambda
- Create a Lambda layer with a custom runtime and reference the layer in your lambda
- You cannot use Lambda in this situation
- Create a Lambda function with a custom runtime

#### Q20. What are listed downstream resources based on?
- the execution policy
- the Lambda configuration
- the Lambda nodes
- the IAM user

#### Q21. Which is an equivalent and valid tag for a pair of Lambdas?
- department:Sales,department:Sales
- department:Sales,department:sales
- aws:demo;aws:demo
- aws:demo;aws:DEMO

#### Q22. Outbound connections from Lambdas must be ______.
- neither of these answers
- UDP/IP
- TCP/IP  <<<<<------- CORRECT
- both of these answers

#### Q23. How are CloudWatch actions configured?
- automatically
- none of these answers
- manually  <<<<<------- CORRECT
- ad hoc

#### Q24. You are testing your stream-based application and the associated Lambda. AWS best practice advises you to test by varying what?
- stream and record sizes
- stream and shard sizes
- batch and record sizes  <<<<<------- CORRECT
- batch and shard sizes

#### Q25. You need to make your Lambda available to services in multiple VPCs. What do you do?
- Place each subnet in a VPC. Associate all subnets to your Lambda.
- Place all subnets in a VPC. Associate all subnets to your Lambda.
- Configure your Lambda to be available to multiple VPCs.
- Configure all application VPCs to be peered.  <<<<<------- CORRECT

#### Q26. How is the cost associated with Lambda function calculated?
- number of function calls
- amount of code run
- compute time  <<<<<------- CORRECT
- amount of infrastructure used

#### Q27. What is the fastest way to get started with Lambda?
- Author a Lambda from scratch.
- Use a blueprint.  <<<<<------- CORRECT
- Use a .zip deployment package.
- Use the serverless app repository.