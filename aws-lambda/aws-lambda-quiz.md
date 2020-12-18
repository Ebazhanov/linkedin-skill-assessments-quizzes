## AWS LAMBDA Assessment

#### Q1. How can you increase the CPU resources for your Lambda?

- [ ] `Increase the configured CPU value`
- [ ] `Increase the configured timeout value`
- [x] `Increase the configured memory value`
- [ ] `Increase the configured concurrency value`

#### Q2. How can additional code or content can be provided for Lambda?

- [ ] `blocks`
- [x] `layers`
- [ ] `aliases`
- [ ] `handlers`

#### Q3. How can Step Functions call Lambdas?

- [ ] `in sequence`
- [x] `both of these answers`
- [ ] `neither of these answers`
- [ ] `in parallel`

#### Q4. Which AWS CLI command invokes a function?

- [ ] `aws lambda invoke --function ReturnBucketName outputfile.txt`
- [ ] `aws lambda execute --function-name ReturnBucketName outputfile.txt`
- [x] `aws lambda invoke --function-name ReturnBucketName outputfile.txt`
- [ ] `aws lambda execute --function ReturnBucketName outputfile.txt`

#### Q5. What adds tracing capabilities to a Lambda?

- [ ] `AWS Trace`
- [ ] `CloudStack`
- [ ] `CloudTrail`
- [x] `AWS X-Ray`

#### Q6. You need to build a continuous integration/deployment pipeline for a set of Lambdas. What should you do?

- [ ] `Create configuration files and deploy them using AWS CodePipeline.`
- [ ] `Create CloudFormation templates and deploy them using AWS CodeBuild`
- [ ] `Create configuration file and deploy using AWS CodeBuild`
- [x] `Create CloudFormation templates and deploy them using AWS CodePipeline.`

#### Q7. What can you use to monitor function invocations?

- [ ] `API Gateway`
- [ ] `S3`
- [ ] `SAS`
- [x] `CLoudTrail`

#### Q8. It is AWS best practice to enable Lambda logging by which of these methods.

- [ ] `Use S3 metrics and CloudWatch alarms`
- [ ] `Create custom metrics within your Lambda code.`
- [ ] `Create custom metrics within your CloudWatch code.`
- [x] `Use Lambda metrics and CloudWatch alarms.`

#### Q9. What may be provided for environment variables?

- [ ] `an SSL certificate`
- [ ] `a bitmask`
- [x] `an AWS KMS key`
- [ ] `an HTTP protocol `

#### Q10. Lambda allows for running of what other things?

- [ ] `binaries.`
- [x] `all of these answers`
- [ ] `executables`
- [ ] `Shell scripts`

#### Q11. In what style must you write Lambda code?

- [ ] `MVC`
- [ ] `virtual`
- [x] `stateless`
- [ ] `protocol`

#### Q12. How can a developer provide Lambda code?

- [ ] `by uploading a .zip file`
- [x] `all of these answers`
- [ ] `by editing inline`
- [ ] `from an S3 bucket`

#### Q13. You are performance-testing your Lambda to verify that you set the memory size adequately. Where do you verify the exectuon overhead?

- [ ] `CLoudWatch logs`
- [ ] `DynamoDB logs`
- [ ] `S3 logs`
- [x] `Lambda logs.`

#### Q14. What facilitates continuous delivery of Lambdas?

- [ ] `CodeStack`
- [ ] `ElasticStack`
- [ ] `Mobile Hub`
- [x] `CodeDeploy`

#### Q15. How are computing resources allocated to Lambdas?

- [x] `proportionally`
- [ ] `equally`
- [ ] `periodically`
- [ ] `daily`

#### Q16. You can restrict the scope of a user's permissions by specifying which two items in an IAM policy?

- [ ] `resources and users`
- [x] `resources and conditions`
- [ ] `events and users`
- [ ] `events and conditions`

#### Q17. What does Lambda logging include?

- [x] `logging streams`
- [ ] `rotating streams`
- [ ] `logging events`
- [ ] `advancing log groups`

#### Q18. What can AWS Amplify NOT do for a Lambda?

- [ ] `create a Lambda`
- [x] `be an event source`
- [ ] `assign an IAM role`
- [ ] `delete a Lambda`

#### Q19. How do you author a Lambda in a programming language that AWS does not support?

- [ ] `Create a Lambda function with a custom runtime and reference the function in your Lambda`
- [x] `Create a Lambda layer with a custom runtime and reference the layer in your lambda`
- [ ] `You cannot use Lambda in this situation`
- [ ] `Create a Lambda function with a custom runtime`

#### Q20. What are listed downstream resources based on?

- [ ] `the execution policy`
- [x] `the Lambda configuration`
- [ ] `the Lambda nodes`
- [ ] `the IAM user`

#### Q21. Which is an equivalent and valid tag for a pair of Lambdas?

- [ ] `department:Sales,department:Sales`
- [x] `department:Sales,department:sales`
- [ ] `aws:demo;aws:demo`
- [ ] `aws:demo;aws:DEMO`

#### Q22. Outbound connections from Lambdas must be **\_\_**.

- [ ] `neither of these answers`
- [ ] `UDP/IP`
- [ ] `TCP/IP`
- [x] `both of these answers`

#### Q23. How are CloudWatch actions configured?

- [ ] `automatically`
- [ ] `none of these answers`
- [x] `manually`
- [ ] `ad hoc`

#### Q24. You are testing your stream-based application and the associated Lambda. AWS best practice advises you to test by varying what?

- [ ] `stream and record sizes`
- [ ] `stream and shard sizes`
- [x] `batch and record sizes`
- [ ] `batch and shard sizes`

#### Q25. You need to make your Lambda available to services in multiple VPCs. What do you do?

- [ ] `Place each subnet in a VPC. Associate all subnets to your Lambda.`
- [ ] `Place all subnets in a VPC. Associate all subnets to your Lambda.`
- [ ] `Configure your Lambda to be available to multiple VPCs.`
- [x] `Configure all application VPCs to be peered.`

#### Q26. How is the cost associated with Lambda function calculated?

- [ ] `number of function calls`
- [ ] `amount of code run`
- [x] `compute time`
- [ ] `amount of infrastructure used`

#### Q27. What is the fastest way to get started with Lambda?

- [ ] `Author a Lambda from scratch.`
- [x] `Use a blueprint.`
- [ ] `Use a .zip deployment package.`
- [ ] `Use the serverless app repository.`

#### Q28. Where is the disk space allocated for Lambda functions?

- [x] `/tmp`
- [ ] `/default`
- [ ] `/temp`
- [ ] `/ds`

#### Q29. How do you stop a running Lambda that is stuck in a recursive loop?

- [ ] `Delete the function.`
- [x] `Set the function concurrent execution limit to 0 while you update the code.`
- [ ] `Reset the function.`
- [ ] `Set the function concurrent execution limit to 100 while you update the code.`

#### Q30. What is AWS best practice for Lambda configuration?

- [x] `Overprovision memory to run your functions faster and reduce your costs. Do not overprovision your function timeout settings.`
- [ ] `Overprovision memory and your function timeout settings to run your functions faster and reduce your costs.`
- [ ] `Do not overprovision memory. Overprovision your function timeout settings to run your functions faster and reduce costs.`
- [ ] `Do not overprovision memory. Do not overprovision your function timeout settings to run your functions faster and reduce costs.`

#### Q31. Basic Lambda permissions include permissions for what?

- [ ] `removing log groups`
- [ ] `none of these answers`
- [ ] `creating log groups`
- [x] `updating log groups`

#### Q32. How are environment variables stored?

- [ ] `DynamoDB tables`
- [x] `key-value pairs`
- [ ] `S3 buckets`
- [ ] `none of these answers`

#### Q33. You need to use a Lambda to provide backend logic to your website. Which service do you use to make your Lambda available to your website?

- [ ] `S3`
- [x] `API Gateway`
- [ ] `X-Ray`
- [ ] `DynamoDB`

#### Q34. How can additional code or content be provided for your Lambda?

- [ ] `aliases`
- [ ] `blocks`
- [ ] `handlers`
- [x] `layers`

#### Q35. Lambdas allow for running of what other things?

- [ ] `binaries`
- [ ] `executables`
- [x] `all of these answers`
- [ ] `shell scripts`

#### Q37. You are creating a Lambda to trigger on change to files in an S3 bucket. Where should you put the bucket name?

- [ ] `in the Lambda function code`
- [x] `in a Lambda environment variable`
- [ ] `in the Lambda tags`
- [ ] `in another S3 bucket`

#### Q38. What action is needed before you can test a Lambda?

- [ ] `Deploy the Lambda.`
- [ ] `Export the function`
- [ ] `none of these answers`
- [x] `Configure a test event.`

#### Q39. What kind of packages can you use with Node.js for Lambdas?

- [ ] `Fleece`
- [x] `NPM`
- [ ] `none of these answers`
- [ ] `Pod`

#### Q41. Lambdas are monitored by default using which service?

- [ ] `CloudTrail`
- [x] `CloudWatch`
- [ ] `CloudFormation`
- [ ] `LogWatch`

#### Q42. What can trigger a Lambda function execution?

- [ ] `a table definition`
- [ ] `queue isolation`
- [ ] `STS Write`
- [x] `an SNS topic`

#### Q43. You need to set an S3 event trigger on your Lambda to respond when data is added to your bucket from another S3 bucket. Which event type do you configure?

- [ ] `POST`
- [ ] `"All object create events"`
- [x] `PUT`
- [ ] `COPY`

#### Q44. To make Lambdas more testable, it is AWS best practice to separate which of these?

- [ ] `Lambda configuration from logging code`
- [ ] `Lambda handler from logging code`
- [x] `Lambda handler from core logic`
- [ ] `Lambda configuration from core logic`
