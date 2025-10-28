## Amazon Web Services (AWS)

#### Q1. 您有一个使用100 GB MySQL数据库的应用程序,正在迁移到AWS。在决定将数据库托管在RDS for MySQL还是Aurora时,应该考虑哪些因素?

- [ ] 成本
- [ ] 维护的便利性与控制的细粒度
- [ ] 应用程序当前使用的存储引擎,例如InnoDB或MyISAM
- [x] All of the above

#### Q2. 哪种数据库是NoSQL数据库类型,可以快速存储和检索键值对?

- [ ] Aurora
- [ ] Neptune
- [ ] RDS for MySQL
- [x] DynamoDB

#### Q3. 您的数据库是一个运行SQL Server的RDS实例,启用了Multi-AZ复制,并且有几个旧的.NET控制台工具每15秒执行一次数据库操作。当集群需要将主数据库服务器切换到次级AZ时,.NET工具开始报告数据库连接失败,而其他应用程序能够正常访问数据库。如何解决这个问题?

- [ ] 使用RDS控制台强制重启数据库实例,使主服务器再次成为主服务器。
- [ ] 运行.NET工具的服务器正在缓存数据库集群地址的DNS查找。清除服务器的DNS缓存,并强制C#工具打开新的数据库连接。
- [ ] .NET应用程序会保留连接字符串的IP地址,直到主机机器重新启动。
- [x] .NET工具需要在连接字符串中更改SQL Server端点,以使用try/catch从次级数据库服务器读取。

#### Q4. 哪些AWS服务可以帮助您自动化开发管道,实现持续集成和持续部署?

- [ ] CodePipeline
- [ ] CodeDeploy
- [ ] CodeBuild
- [x] All of the above

#### Q5. 哪个AWS服务符合Payment Card Industry Data Security Standard (PCI DSS) Level 1的处理和传输信用卡数据的标准?

- [ ] API Gateway
- [ ] Simple Queue Service (SQS)
- [ ] Kinesis Data Streams
- [x] All of the above

#### Q6. 您的网络附加存储阵列上有大量文件,必须归档并保存10年以满足行业法规要求。这些数据将很少被访问,但必须保留。存储这些数据的最佳AWS服务是什么?

- [ ] EFS
- [ ] Snowball
- [ ] OEBS
- [x] S3 Glacier

#### Q7. 对于您的AWS根账户,您生成了一个最大允许长度的随机密码,并包含特殊字符。您还应该采取哪些额外步骤来保护您的AWS根账户?

- [ ] 为账户管理员创建一个具有最高权限的IAM角色。不存储根密码,但当需要使用根账户时,通过电子邮件确认重置根账户密码,并重复此过程。
- [ ] 使用诸如1Password或LastPass之类的服务将随机生成的密码存储在组织的秘密数据库中,并仅授予DevOps团队访问此秘密的权限。
- [ ] 为管理员创建IAM账户,并将AdministratorAccess策略附加到他们的账户。禁用用户设置中的根账户。
- [x] 为账户管理员创建一个具有最高权限的IAM角色,并且不要在日常操作中使用根账户。启用根账户的双因素认证。

#### Q8. 哪种Elastic Load Balancing选项支持Lambda作为目标?

- [ ] Network Load Balancer
- [ ] Lambda不能直接通过传入的网络请求调用。您必须使用API Gateway。
- [ ] Classic Load Balancer
- [x] Application Load Balancer

#### Q9. 如何设计一个解决方案,使SQL Server数据库在AWS区域之间以active-active架构进行复制?

- [ ] 使用RDS for SQL Server,并在两个不同的区域创建相同的实例。使用Database Migration Service保持每个数据库同步。
- [ ] 使用VPN或VPC peering在每个区域的VPC之间建立连接。在每个区域的EC2实例上安装SQL Server Enterprise Edition,并配置Always On availability group。
- [x] 使用RDS for SQL Server 2016或2017 Enterprise Edition。启用Multi-AZ支持并选择Mirroring/Always On选项。为mirroring选项选择另一个区域。
- [ ] 无法设置跨地理区域的SQL Server active-active架构。

[Reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html?opt_id=oeu1612780272452r0.9199525073583283)

#### Q10. 从AWS Marketplace启动EC2实例的费用是多少?

- [ ] AWS Marketplace中的所有镜像都会产生额外的每小时费用,此外还有您选择的实例大小的费用。
- [ ] 您只能启动由其他用户在您的AWS账户上创建的镜像,因此您只需支付您选择的实例大小的费用以及基础镜像的S3存储费用。
- [x] 每个镜像都有自己的定价,可以是免费的,也可以包括软件许可费用。您还需要支付运行镜像的实例费用。
- [ ] AWS Marketplace中的所有镜像仅包含开源软件,没有额外费用,并由其他AWS用户创建。您只需支付您选择的实例大小费用。

#### Q11. 使用带有EC2实例的ECS集群时,您应该对EC2执行哪些维护任务?

- [ ] ECS创建的实例不需要应用补丁;但是,您应该确保您的容器包含任何重要的安全更新。
- [x] 使用最新的ECS AMI刷新集群实例。
- [ ] ECS集群不使用EC2实例。
- [ ] 您不应该直接操作ECS创建的EC2实例。AWS会自动更新这些实例。

#### Q12. 哪种内存缓存服务器不受ElastiCache支持?

- [ ] Redis 5
- [ ] Memcached
- [x] Elasticsearch
- [ ] Redis 3

#### Q13. 哪个AWS服务可以用来帮助生成各种合规标准(如Payment Card Industry Data Security Standard (PCI DSS) Level 1)所需的文档?

- [x] Artifact
- [ ] DocumentDB
- [ ] 打印AWS Compliance summary,并将其与审计所需的文档一起保存。
- [ ] Secrets Manager

#### Q14. 在计划迁移之前使用AWS进行研发时,如何防止账单出现意外增加或峰值?

- [ ] 使用billing dashboard创建成本预算。输入您每月希望被收取的最大金额。任何超过此金额的费用将导致AWS自动暂停这些资源。
- [ ] 使用根AWS账户激活IAM对账户billing information的访问权限。确保您的IAM用户具有Billing FullAccessGroup策略。然后从billing dashboard每天检查累计费用。
- [ ] 如果您使用AWS free tier,您必须确认任何超出AWS free tier限制的服务使用。
- [x] 使用根AWS账户在user preferences中启用Billing Alerts。然后使用CloudWatch创建billing alarm,并为您的estimated monthly charges设置一个特定的美元金额threshold。

#### Q15. 您正在创建一个DynamoDB表来存储自1938年以来发布的所有电影。您的应用程序将允许用户按电影标题搜索并查看该电影的详细信息。根据下面显示的电影数据样本,您将导入的最佳键设置是什么?

```json
{
  "title": "The Avengers",
  "year": 2012,
  "cast": ["Mark Ruffalo", "Robert Downey, Jr."],
  "genres": ["Action"]
}
```

- [ ] primary key应该是title字段的partition key。
- [ ] primary key应该是title字段,partition key应该是genres字段。
- [ ] primary key应该是由title字段的partition key和year字段的sort key组成的composite key。
- [x] primary key应该创建为完全唯一的值,例如电影ID的sequential numerical list。partition key应该是title字段,以便快速查找。

#### Q16. 哪种数据存储提供了一种简单快捷的方式,以对象格式存储基本用户属性?

- [ ] ORDS for Oracle
- [ ] Redshift
- [ ] Neptune
- [x] DynamoDB

#### Q17. 您需要一个schematic database。哪个Amazon数据库服务提供了这种解决方案?

- [ ] ORDS
- [ ] Aurora
- [ ] Redshift
- [x] DynamoDB

#### Q18. SNS不原生支持哪种通信渠道?

- [ ] SMS text message
- [ ] push notification
- [ ] email
- [x] automated phone call

#### Q19. 在使用Lambda设计serverless Web应用程序时,必须考虑什么关键概念?

- [ ] serverless Web应用程序在用户的Web浏览器中运行,因此您需要将用户更改的任何数据直接存储在数据库中。
- [ ] Lambda仅允许您使用JavaScript编写函数。
- [ ] Lambda不使用服务器,因此它只能向每个用户返回相同的请求。
- [x] Lambda是stateless,因此它不会在请求之间记住用户身份。

#### Q20. DevOps的一个原则是将基础设施视为代码。哪个AWS服务允许您编写AWS基础设施脚本?

- [ ] CloudTrail
- [x] CloudFormation
- [ ] AWS Config
- [ ] AWS Service Catalog

#### Q21. 您创建了一个带有公共IP地址的Windows EC2实例,并安装了SQL Server。在尝试从本地计算机上的SQL Server Enterprise Manager连接到SQL Server时,Windows EC2实例无法与服务器建立连接。您首先应该检查什么?

- [ ] 检查VPC的routing table。
- [x] 验证分配的security group是否允许来自您当前IP地址的TCP端口1433流量。
- [ ] 检查Windows防火墙中的策略。
- [ ] 验证您是否使用非sa用户连接到实例。

#### Q22. 您正在托管一个应用程序,该应用程序配置为通过TCP端口3380-3384、3386-3388和3390向其客户端流式传输媒体。下面的Inbound选项卡显示了附加到此实例的三个传入security group策略。您应该使用哪个策略?

![image](../../../aws/images/001.png)

- [x] 暴露TCP端口3380-3390的规则也会将端口3389 (RDP)公开给整个互联网。编写单独的规则以仅暴露所需的端口。
- [ ] 第一个security group规则允许所有流量进入此实例。将整个实例暴露给整个互联网会使服务器开放给其他端口号运行的各种攻击。
- [ ] 验证AWS账户所有者是否实际控制12.228.11.0-255的整个CIDR C block,并确保这些是用于RDP访问此实例的安全IP。
- [ ] 没有建议需要提出。

#### Q23. 您有四个前端Web服务器位于load balancer后面,这些服务器使用NFS访问另一个EC2实例,该实例用于调整前端应用程序的图像大小并存储图像。应该为这些服务器分配哪些security group策略?

- [ ] 为所有实例分配Elastic IP,并创建一个组,允许所有流量在五个Elastic IP地址之间传递,并允许所有入站HTTPS流量。
- [x] 前端Web服务器应该允许HTTPS。为所有实例分配另一个组,允许使用该组的实例之间的所有流量。
- [ ] 创建一个security group,允许来自所有IP地址的入站NFS、HTTP和HTTPS流量。将此组应用于所有服务器。
- [ ] 创建一个security group,允许来自所有IP地址的入站HTTP和HTTPS流量,并将其应用于Web服务器。为NFS文件存储创建第二个security group,允许向前端Web服务器的private IP范围发送出站NFS流量。

#### Q24. 您有一个Linux EC2 Web服务器,突然所有HTTP请求和SSH连接尝试都超时。您注意到它在EC2控制台中未通过system status check。您应该采取什么行动?

- [x] 从最后的AMI镜像恢复实例。system status check表明实例上的文件系统已损坏。
- [ ] 停止并启动实例。这将使实例移动到另一个主机。
- [ ] 联系AWS支持。未通过system status check表明底层硬件出现故障,必须由AWS代表解决。
- [ ] 重启实例。这将停止并启动实例,并将其移动到另一个主机。

#### Q25. 您有几个本地服务器,希望将异地备份存储在AWS上。您可以使用什么完全托管的备份服务将备份发送到AWS?

- [ ] Windows Server 2016支持使用Storage Replica时将S3作为目标。
- [x] 使用Storage Gateway。
- [ ] 使用AWS CLI将文件直接同步到S3。
- [ ] 使用RDS console强制重启数据库实例,使主服务器重新成为主服务器。

#### Q26. 在RDS中创建一个高可用的PostgreSQL数据库以应对单个AWS区域故障的最佳实践是什么?

- [ ] PostgreSQL无法跨区域复制。从S3存储桶恢复数据库备份,并将数据库连接指向新的实例。
- [ ] 在其他AWS区域创建read replica。在区域故障解决之前,可以从任何read replica中指定一个新的primary database。
- [ ] 验证您的实例是否配置了Multi-AZ支持。在发生故障时,数据库更改将自动同步到另一个区域,RDS将自动选择新的primary database,直到区域故障解决。
- [x] 在其他AWS区域创建read replica。确保对数据库的读取操作发生在可用的read replica上,如果primary database宕机,可以将read replica提升为standalone database以进行写操作。

#### Q27. 您创建了一个新的Linux EC2实例并安装了PostgreSQL,但无法从本地计算机连接到服务器。您会采取哪些步骤来解决此问题?

- [ ] 创建一个允许来自0.0.0.0/0的所有流量的security group规则。这将验证是否有其他规则拒绝了流量。
- [x] 验证分配的security group是否允许来自您的IP地址到port 5432的流量。验证PostgreSQL是否配置为监听外部流量并绑定到公共接口。
- [ ] 确保您正在使用Elastic IP,并且它已包含在`postgresql.conf`配置文件中。
- [ ] 停止并重新启动实例。新的security group规则只有在重启后才会生效。

#### Q28. 此S3 bucket policy的statement主体做了什么?

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

- [ ] bucketpolicy1允许任何用户对userreports存储桶中的对象执行任何操作,但限制来自68.249.108.0到68.249.108.255的用户对对象的只读权限 - 除了68.249.108.128。
- [ ] bucketpolicy1允许来自IP范围68.249.108.0的任何用户访问userreports存储桶中的对象,并拒绝68.249.108.128的访问。
- [ ] bucketpolicy1允许任何用户对userreports存储桶中的对象执行任何操作 - 除了来自IP 68.249.108.128的用户。
- [x] bucketpolicy1允许来自IP范围68.249.108.0到68.249.108.255的任何用户访问userreports存储桶中的对象 - 除了来自IP 68.249.108.128的用户。

#### Q29. 一位新开发人员加入团队,您被要求提供访问组织AWS账户的权限。授予访问权限的最佳实践是什么?

- [ ] 将分配给开发团队的IAM登录信息提供给新开发人员。此IAM用户应该已经包含开发人员需要的所有策略。
- [ ] 为新开发人员创建一个IAM用户。手动为新的IAM用户账户分配策略。
- [ ] 不要给新开发人员访问AWS控制台的权限。使用分配给开发组的IAM用户,为其生成一组新的access keys,并标记为开发人员的名字。
- [x] 为新开发人员创建一个IAM用户。将新开发人员分配到您已为其他开发人员创建的开发组。

#### Q30. 启动支持instance store的实例类型的EC2实例时,instance store的最佳使用场景是什么?

- [x] 使用instance store来服务需要低I/O latency的临时文件。
- [ ] 使用instance store来处理用户上传的文件。由于它比EBS volume更安全,可以隔离任何恶意文件以防止感染服务器。
- [ ] instance store比EBS volume更快,因此将操作系统的root安装在此volume上以加快服务器性能。
- [ ] instance store是一种已弃用的存储选项,不应使用。

#### Q31. 水平扩展一个依赖Active Directory的传统ASP.NET Web应用程序的最佳实践是什么?该应用程序目前部署在单个Windows EC2实例上。

- [x] 使用Sysprep在维护窗口期间关闭实例。创建一个AMI镜像,并将两个服务器放置在带有sticky session的Application Load Balancer后面。
- [ ] 启动一个新的EC2实例,安装最新版本的Windows Server并重新安装应用程序。使用Application Load Balancer和sticky session在两个服务器之间进行负载均衡。
- [ ] 使用AMI镜像创建服务器的克隆,并使用Application Load Balancer通过sticky session在两个实例之间平衡流量。
- [ ] 在这种情况下,水平扩展不是最佳实践。增加现有EC2实例的大小并垂直扩展应用程序。

#### Q32. 此CloudFormation模板的小部分代码段的作用是什么?

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

- [x] 它将VPC network flow logs写入CloudWatch FlowLogsGroup log group。您可以使用此功能检查VPC的网络连接。
- [ ] 它记录VPC内的所有网络流量,除了由LogVpcID定义的instance ID,并将其记录到CloudWatch FlowLogsGroup log group。
- [ ] 它将单个EC2实例的所有网络流量记录到CloudWatch FlowLogsGroup log group。您可以使用此功能检查进入EC2实例的可疑网络流量。
- [ ] 它记录VPC内资源发出的所有DNS请求,并将其记录到CloudWatch FlowLogsGroup。使用此功能诊断环境中的DNS lookup错误。

#### Q33. 您正在ECS上运行Docker容器。最重要的监控指标是什么?

- [ ] CloudWatch中每个service的运行容器数量。
- [ ] CloudWatch中集群中每个EC2实例的instance health。
- [ ] 监控EC2 Service Dashboard。关注ECS服务的发布故障。
- [x] CloudWatch中集群中每个EC2实例的memory consumption。

#### Q34. Application Load Balancer可以根据多种条件将流量路由到多个target group。以下哪个用例不受Application Load Balancer支持?

- [ ] 带有HTTP header `X-Requested-With: staging`的请求可以路由到ECS service的target group,该服务位于您的staging环境中。
- [ ] 源IP匹配192.0.2.0/24且监听port为1433的请求可以路由到RDS SQL Server集群的target group。
- [ ] 路径为/signup*的请求可以路由到处理新用户注册的Lambda函数的target group。
- [x] 源IP匹配192.0.2.0/24且监听port为1433的请求可以路由到RDS SQL Server集群的target group。

#### Q35. 您有一个Aurora MySQL数据库正在大量使用,由于速度较慢导致应用程序超时。应该采取什么步骤来诊断这些超时问题?

- [x] 使用CloudWatch监控Aurora MySQL的CPU、内存、网络吞吐量和可用连接。使用这些指标确定性能问题是由于CPU或网络过载、内存不足还是连接太多造成的。
- [ ] 使用CloudWatch监控正在运行的Aurora MySQL查询,并使用内置的slow query log功能识别运行时间超过10秒的查询。
- [ ] 使用Performance Insights检查正在运行的查询并追踪发生超时问题的确切时间。
- [ ] 创建一个Lambda函数来记录Aurora MySQL数据库的查询运行时间。将该函数配置为在查询执行时间超过10秒时触发CloudWatch警报。

#### Q36. Aurora Serverless的主要优势是什么?

- [x] 自动扩展数据库容量以根据实际应用需求匹配,并在不活动期间自动关闭。
- [ ] 提供更高的数据库性能,特别是对于具有大量concurrent connection的应用。
- [ ] 允许在单个Aurora cluster中运行MySQL和PostgreSQL数据库。
- [ ] 提供读写分离功能以提高应用程序性能。

#### Q37. 哪个AWS service允许您运行代码而无需预配置或管理服务器?

- [x] AWS Lambda
- [ ] Amazon EC2
- [ ] Amazon ECS
- [ ] AWS Fargate

#### Q38. 使用DynamoDB时,什么是partition key?

- [ ] 一个可选的第二列,用于排序表中的数据
- [x] 一个必需的主键列,用于在表内唯一标识每个项目
- [ ] 用于将相关项目分组在一起的列
- [ ] 用于实现consistent read的列

#### Q39. 以下哪个不是S3 storage class?

- [ ] S3 Standard
- [ ] S3 Intelligent-Tiering
- [ ] S3 Glacier
- [x] S3 Temporary

#### Q40. 在Route 53中,什么是alias record?

- [ ] 一个将一个域名指向另一个域名的DNS record
- [x] 一个将域名指向AWS resource(如ELB或CloudFront distribution)的DNS record
- [ ] 一个临时DNS record,在指定时间后过期
- [ ] 一个加密的DNS record,提供额外的安全性

#### Q41. 您的公司正在将大量on-premises数据迁移到AWS。您需要在保持数据安全的同时快速传输数PB的数据。最好的方法是什么?

- [ ] 使用AWS Direct Connect建立专用网络连接
- [ ] 使用AWS DataSync over internet传输数据
- [x] 使用AWS Snowball Edge设备传输数据
- [ ] 使用S3 Transfer Acceleration上传数据

#### Q42. 什么是VPC peering?

- [x] 两个VPC之间的网络连接,允许它们使用private IP地址相互通信
- [ ] 一个允许VPC访问internet的gateway
- [ ] 一个在VPC内部隔离资源的安全功能
- [ ] 一个允许多个AWS账户共享同一个VPC的机制

#### Q43. 在使用Elastic Beanstalk部署应用程序时,以下哪项是正确的?

- [ ] 您必须手动配置load balancer和auto scaling
- [x] Elastic Beanstalk自动处理capacity provisioning、load balancing和auto scaling
- [ ] 您无法自定义底层基础设施配置
- [ ] Elastic Beanstalk仅支持Java应用程序

#### Q44. CloudWatch Logs的主要用途是什么?

- [ ] 监控AWS账单和成本
- [x] 收集、监控和存储来自AWS resources和应用程序的log文件
- [ ] 创建AWS资源的备份
- [ ] 管理IAM用户和权限

#### Q45. 什么是AWS Organizations?

- [x] 一个允许您集中管理和治理多个AWS账户的service
- [ ] 一个用于组织S3 bucket中文件的工具
- [ ] 一个用于创建organizational chart的service
- [ ] 一个用于管理IAM用户组的功能

#### Q46. 使用AWS Systems Manager Parameter Store的主要好处是什么?

- [ ] 它提供了一个图形界面来管理EC2实例
- [ ] 它自动备份您的数据库
- [x] 它提供安全、分层的配置数据和secrets management存储
- [ ] 它监控应用程序性能

#### Q47. CloudFront的主要用途是什么?

- [ ] 存储和归档数据
- [ ] 运行serverless函数
- [x] 通过全球edge location网络以低延迟向用户分发内容
- [ ] 管理数据库复制

#### Q48. 在VPC中,什么是network ACL (NACL)?

- [ ] 一个在instance级别控制inbound和outbound traffic的virtual firewall
- [x] 一个在subnet级别控制inbound和outbound traffic的可选安全层
- [ ] 一个用于监控网络性能的工具
- [ ] 一个用于加密网络流量的协议

#### Q49. AWS Config的主要用途是什么?

- [ ] 配置EC2实例的operating system
- [x] 评估、审计和评估AWS resources的配置
- [ ] 创建和管理VPC配置
- [ ] 配置load balancer设置

#### Q50. 什么是AWS CloudTrail?

- [x] 一个记录AWS账户activity和API调用的service
- [ ] 一个用于创建backup trails的工具
- [ ] 一个用于优化应用程序路由的service
- [ ] 一个用于监控cloud formation的功能

#### Q51. 使用Amazon ECS与Fargate launch type相比于EC2 launch type的主要优势是什么?

- [ ] Fargate提供更好的性能
- [ ] Fargate支持更多的container runtime
- [x] Fargate消除了管理底层EC2实例的需要
- [ ] Fargate成本更低

#### Q52. AWS Secrets Manager的主要用途是什么?

- [ ] 管理VPC security groups
- [ ] 加密S3 buckets
- [x] 轻松管理、检索和轮换数据库credentials、API keys和其他secrets
- [ ] 创建backup secrets

#### Q53. 在S3中,什么是versioning?

- [x] 一个在同一bucket中保存对象的多个versions的功能
- [ ] 一个创建bucket的不同versions的方法
- [ ] 一个跟踪API version的工具
- [ ] 一个用于version control的AWS service

#### Q54. AWS Direct Connect的主要好处是什么?

- [ ] 它提供了更快的internet连接
- [x] 它在您的on-premises和AWS之间提供专用的private network connection
- [ ] 它自动加密所有网络流量
- [ ] 它减少了数据传输的latency

#### Q55. 什么是AWS Step Functions?

- [x] 一个用于协调分布式应用程序和microservices的serverless orchestration service
- [ ] 一个用于创建step-by-step教程的工具
- [ ] 一个用于管理EC2实例启动steps的service
- [ ] 一个用于追踪application deployment steps的功能

#### Q56. Amazon Kinesis的主要用途是什么?

- [ ] 管理容器化应用程序
- [ ] 创建machine learning模型
- [x] 实时收集、处理和分析streaming data
- [ ] 存储和归档log文件

#### Q57. 在IAM中,什么是policy?

- [x] 一个定义permissions的JSON文档,指定对AWS resources的允许或拒绝actions
- [ ] 一个用于管理user passwords的工具
- [ ] 一个用于配置network security的设置
- [ ] 一个用于监控compliance的功能

#### Q58. AWS Auto Scaling的主要优势是什么?

- [ ] 它减少了所有AWS services的成本
- [x] 它根据需求自动调整capacity以维持稳定、可预测的性能
- [ ] 它自动备份您的数据
- [ ] 它提高了database query性能

#### Q59. 什么是Amazon RDS Read Replica?

- [x] 一个数据库的只读副本,可以用于扩展read-heavy workloads
- [ ] 一个primary database的备份
- [ ] 一个用于存储database logs的工具
- [ ] 一个用于复制database schema的功能

#### Q60. AWS CodePipeline的主要用途是什么?

- [ ] 管理data pipelines
- [ ] 创建network pipelines
- [x] 自动化release pipelines以实现快速、可靠的应用程序和基础设施更新
- [ ] 优化code performance

#### Q61. 在S3中,什么是lifecycle policy?

- [x] 一组定义S3如何管理objects在其lifetime期间的规则
- [ ] 一个用于管理bucket lifecycles的工具
- [ ] 一个用于定义application lifecycle的策略
- [ ] 一个用于监控object age的功能

#### Q62. AWS Elastic Beanstalk支持哪些platform?

- [ ] 仅支持Java
- [ ] 仅支持.NET
- [ ] 仅支持Python
- [x] 支持多种platforms,包括Java、.NET、PHP、Node.js、Python、Ruby、Go和Docker

#### Q63. 什么是AWS WAF (Web Application Firewall)?

- [x] 一个帮助保护web applications免受常见web exploits的web application firewall
- [ ] 一个用于管理wireless access的工具
- [ ] 一个用于加速web applications的service
- [ ] 一个用于监控web traffic的功能

#### Q64. Amazon SNS (Simple Notification Service)的主要用途是什么?

- [ ] 管理database notifications
- [x] 向distributed systems、microservices和mobile applications发送messages和notifications
- [ ] 创建social network applications
- [ ] 管理DNS records

#### Q65. 在DynamoDB中,什么是GSI (Global Secondary Index)?

- [x] 一个具有可能与table不同的partition key和sort key的index
- [ ] 一个global backup index
- [ ] 一个用于搜索global data的工具
- [ ] 一个用于复制tables across regions的功能

#### Q66. AWS Glue的主要用途是什么?

- [ ] 管理application dependencies
- [ ] 连接VPCs
- [x] 一个用于ETL (extract, transform, load)的完全托管的数据集成service
- [ ] 粘合CloudFormation stacks

#### Q67. 什么是Amazon EMR (Elastic MapReduce)?

- [ ] 一个email marketing service
- [ ] 一个用于创建emergency responses的工具
- [x] 一个用于处理vast amounts of data的big data platform,使用Hadoop、Spark等开源工具
- [ ] 一个用于管理EC2 reservations的功能

#### Q68. AWS Certificate Manager的主要用途是什么?

- [ ] 管理professional certificates
- [x] 轻松provision、管理和deploy SSL/TLS certificates以与AWS services和内部connected resources一起使用
- [ ] 创建certification programs
- [ ] 验证user certifications

#### Q69. 在VPC中,什么是Internet Gateway?

- [x] 一个允许VPC中的resources访问internet的horizontally scaled、redundant和highly available component
- [ ] 一个监控internet traffic的工具
- [ ] 一个加密internet communications的service
- [ ] 一个优化internet速度的功能

#### Q70. Amazon Redshift的主要用途是什么?

- [ ] 管理traffic routing
- [ ] 创建data shifts
- [x] 一个快速、可扩展的data warehouse,可以轻松分析所有数据
- [ ] 重定向application traffic

#### Q71. 什么是AWS Fargate?

- [x] 一个用于Amazon ECS和EKS的serverless compute engine,允许您运行containers而无需管理servers或clusters
- [ ] 一个用于长距离data transfer的工具
- [ ] 一个用于管理API gateways的service
- [ ] 一个用于优化network routing的功能

#### Q72. AWS CodeBuild的主要用途是什么?

- [ ] 构建physical infrastructure
- [ ] 创建organizational structures
- [x] 一个完全托管的continuous integration service,可以编译source code、运行tests并产生可部署的software packages
- [ ] 管理building access

#### Q73. 在S3中,什么是object tagging?

- [x] 一个允许您为S3 objects分配key-value pairs作为metadata的功能
- [ ] 一个用于标记deleted objects的工具
- [ ] 一个用于创建object hierarchies的方法
- [ ] 一个用于监控object access的功能

#### Q74. AWS CodeDeploy的主要用途是什么?

- [ ] 部署physical servers
- [ ] 管理employee deployments
- [x] 一个自动化向各种compute services(如EC2、Fargate、Lambda)部署applications的deployment service
- [ ] 创建deployment schedules

#### Q75. 什么是Amazon CloudWatch Metrics?

- [x] 代表您的AWS resources和applications的time-ordered数据点集合
- [ ] 一个用于测量physical distances的工具
- [ ] 一个用于创建metric reports的service
- [ ] 一个用于comparing performance metrics的功能

#### Q76. AWS Systems Manager的主要用途是什么?

- [ ] 管理file systems
- [ ] 创建system architectures
- [x] 为AWS和on-premises resources提供统一的user interface,可以查看operational data和自动化operational tasks
- [ ] 监控system performance

#### Q77. 在CloudFront中,什么是origin?

- [x] CloudFront distribution从中获取files的server - 例如S3 bucket或HTTP server
- [ ] 数据起源的地理位置
- [ ] 创建distribution的original user
- [ ] distribution的starting point

#### Q78. Amazon SQS (Simple Queue Service)的主要用途是什么?

- [ ] 管理database queries
- [x] 一个完全托管的message queuing service,使您能够decouple和scale microservices、distributed systems和serverless applications
- [ ] 创建application queues
- [ ] 优化SQL queries

#### Q79. 什么是AWS Transit Gateway?

- [x] 一个network transit hub,可用于互连您的VPCs和on-premises networks
- [ ] 一个用于管理public transportation的service
- [ ] 一个用于transitioning applications to cloud的工具
- [ ] 一个用于monitoring network transitions的功能

#### Q80. AWS Lambda@Edge的主要用途是什么?

- [ ] 在edge devices上运行Lambda functions
- [x] 在更接近users的AWS locations运行Lambda functions,以customize content delivered through CloudFront
- [ ] 管理network edges
- [ ] 优化lambda performance

#### Q81. 在IAM中,什么是role?

- [x] 一个具有定义AWS services和resources可以执行的actions的permissions的identity
- [ ] 一个用于定义user job roles的工具
- [ ] 一个用于assigning user responsibilities的function
- [ ] 一个用于managing organizational roles的service

#### Q82. Amazon EBS (Elastic Block Store)的主要用途是什么?

- [ ] 创建elastic applications
- [ ] 管理block lists
- [x] 为EC2 instances提供persistent block storage volumes
- [ ] 存储building blocks

#### Q83. 什么是AWS Organizations的Service Control Policy (SCP)?

- [x] 一个用于管理organization中permissions的policy
- [ ] 一个用于controlling services的tool
- [ ] 一个用于managing organizational services的service
- [ ] 一个用于monitoring service usage的功能

#### Q84. AWS Backup的主要用途是什么?

- [ ] 创建backup plans
- [ ] 管理backup storage
- [x] 一个完全托管的service,可以集中化和自动化跨AWS services的data backup
- [ ] 监控backup status

#### Q85. 在RDS中,什么是Multi-AZ deployment?

- [x] 一个在不同Availability Zone中提供synchronous standby replica的high availability解决方案
- [ ] 一个在multiple zones部署databases的方法
- [ ] 一个用于managing multiple databases的tool
- [ ] 一个用于optimizing zone performance的功能

#### Q86. AWS CodeCommit的主要用途是什么?

- [ ] 管理code commits
- [ ] 创建commitment schedules
- [x] 一个完全托管的source control service,托管secure Git-based repositories
- [ ] 监控code changes

#### Q87. 什么是Amazon CloudWatch Events (现在称为Amazon EventBridge)?

- [x] 一个serverless event bus service,可以轻松将applications与来自各种sources的data连接起来
- [ ] 一个用于managing calendar events的tool
- [ ] 一个用于creating event schedules的service
- [ ] 一个用于monitoring event attendance的功能

#### Q88. AWS Service Catalog的主要用途是什么?

- [ ] 创建service catalogs
- [ ] 管理product catalogs
- [x] 允许organizations创建和管理approved products catalogs以在AWS上使用
- [ ] 监控service usage

#### Q89. 在S3中,什么是Cross-Region Replication (CRR)?

- [x] 一个自动将objects从一个AWS Region的bucket复制到不同Region的另一个bucket的功能
- [ ] 一个用于creating regional backups的tool
- [ ] 一个用于managing cross-region traffic的service
- [ ] 一个用于optimizing region performance的功能

#### Q90. Amazon EKS (Elastic Kubernetes Service)的主要用途是什么?

- [ ] 管理elastic keys
- [ ] 创建kubernetes clusters manually
- [x] 一个完全托管的Kubernetes service,使在AWS上运行Kubernetes变得容易
- [ ] 监控kubernetes performance

#### Q91. 什么是AWS CloudFormation StackSets?

- [x] 一个允许您使用single operation跨multiple accounts和regions创建、更新或删除stacks的功能
- [ ] 一个用于managing stack collections的tool
- [ ] 一个用于creating stack hierarchies的service
- [ ] 一个用于monitoring stack performance的功能

#### Q92. AWS Data Pipeline的主要用途是什么?

- [ ] 管理data pipes
- [ ] 创建pipeline architectures
- [x] 一个web service,帮助您可靠地在不同AWS compute和storage services之间以及与on-premises data sources之间处理和移动data
- [ ] 优化data flow

#### Q93. 如果Auto Scaling组因达到AWS service limit而无法启动实例,会发生什么?

- [ ] Auto Scaling将继续尝试启动实例,持续3天。
- [x] Auto Scaling组将自动终止。
- [ ] Auto Scaling会在另一个region启动实例。
- [ ] Auto Scaling将移除scaling过程。

#### Q94. 指出错误的陈述。

- [ ] Amazon Machine Instances按不同level定价,并按compute/hour租用。
- [ ] CloudWatch获取的metrics可用于启用Auto Scaling功能。
- [ ] 多种tools用于支持EC2 service。
- [x] 以上都不是。

#### Q95. 在Amazon VPC设计中,单个public subnet的VPC适合以下哪种应用设计?

- [x] 单tier应用
- [ ] serverless应用
- [ ] microservices应用
- [ ] 多tier应用

#### Q96. 如果停止并重新启动EC2实例,它是否保留其private IP地址?

- [x] 是,实例保留其private IP地址。
- [ ] 否,仅保留public IP地址。
- [ ] 否,仅保留Elastic IP地址。
- [ ] 否,不保留其private IP地址。

#### Q97. 所有启动到non-default VPC的Amazon EC2实例默认是**\_**。

- [ ] stateless
- [ ] protected
- [ ] public
- [x] private

#### Q98. 当您将实例启动到dedicated tenancy VPC时,会发生什么?

- [x] 无论实例的特定tenancy attribute如何,您的实例都会自动成为dedicated instance。
- [ ] 您会收到一条error message,通知您必须将实例的tenancy attribute设置为dedicated。
- [ ] 实例启动失败,但AWS会提示您启动一个新的实例并将tenancy attribute设置为dedicated。
- [ ] 实例启动立即失败。

#### Q99. 在VPC security group中使用**\_**协议与database instance通信。

- [ ] SSH
- [ ] SSL
- [x] TCP
- [ ] UDP

#### Q100. 在EC2 Linux-red hat/amazon中的default user是什么?

- [ ] root
- [ ] Ec2user
- [x] ec2-user
- [ ] linux

#### Q101. 使用Systems Manager时,可以通过Systems Manager \_\_\_\_ 创建policies。

- [ ] Policy Manager
- [ ] State Manager
- [x] Documents
- [ ] Inventory

#### Q102. 企业越来越多地转向具有自动化IT的hybrid cloud环境。Amazon EC2 State Manager的哪个功能对这些公司特别有用?

- [ ] 有效性
- [x] 一致性
- [ ] 可靠性
- [ ] 冗余性

#### Q103. 您的DevOps经理注意到您的一个Windows实例中MySQL软件安装出现问题,并要求您修复它。使用AWS Systems Manager修复此问题的推荐方法是什么?

- [ ] 编写一个Power Shell脚本重新安装msi文件,并使用Run Command运行它。
- [ ] 执行AWS-ApplyPatchBaseline命令。
- [ ] 允许State Manager自动批量修复。
- [x] 使用Run Command执行AWS-InstallApplication document。

#### Q104. 在EC2 Systems Manager中,可以使用Patch \_\_\_\_ 来选择要安装到实例的patches。

- [ ] Levels
- [ ] Manager
- [x] Baselines
- [ ] Policy

#### Q105. AWS Batch job的status为runnable时是什么情况?

- [ ] 提交的job resources正在部署。
- [ ] 提交的job已被evaluated。
- [x] 提交的、已evaluated的job没有未完成的dependencies。
- [ ] 提交的job在job queue中排在下一位。

#### Q106. 关于AWS Batch自动retry的正确陈述是什么?

- [ ] 每个job默认提供一次attempt,但用户可以修改为无限次attempts。
- [ ] 每个job默认提供一次attempt,但AWS Batch job scheduler可能会在evaluating提交的job后修改此设置。
- [x] 每个job默认提供一次attempt,但用户可以修改为最多10次attempts。
- [ ] 每个job仅限一次attempt,然后被分类为成功或失败。

#### Q107. AWS Batch job parameters中可以指定什么以防止不成功的jobs陷入循环?

- [x] job timeout的duration
- [ ] 资源支出上限
- [ ] 自动job retry次数
- [ ] AWS Batch job agent

#### Q108. 在以下AWS Batch components中,用户可以设置priority以处理time-sensitive或low-priority的jobs?

- [ ] 在job scheduler中
- [ ] 在job本身中
- [ ] 在job definition中
- [x] 在job queue中

#### Q109. 每月可以从Amazon CloudFront免费使最多**\_**路径文件invalidate。

- [ ] 100
- [ ] 5,000
- [x] 1,000
- [ ] 500

#### Q110. 如果您希望更快、更准确地分析单个stream的access logs以获取指定时间段的数据,推荐的做法是什么?

- [ ] 逐一检查您在指定时间段收到的所有log files。
- [ ] 按行分析所有log files。
- [x] 将指定时间段收到的所有log files合并为一个文件。
- [ ] 将log files与Amazon CloudWatch结果进行比较。

#### Q111. 关于Amazon CloudFront,当您创建新的Web distribution时,default cache behavior的path pattern设置为\***\*\_\*\***。

- [x] `*` (所有文件),且无法更改。
- [ ] HTML文件,且无法更改。
- [ ] HTML文件,且可以更改。
- [ ] `*` (所有文件),且可以更改。

#### Q112. 在Amazon CloudFront中,如果您为distribution添加了www.example.com的CNAME,您还需要使用DNS service创建(或更新)一个CNAME record。

- [x] 正确
- [ ] 错误,无法为distribution添加CNAME。
- [ ] 错误,您应该使用CloudWatch metrics而不是DNS添加CNAME record。
- [ ] 错误,不需要创建CNAME record,因为Amazon会自动完成。

#### Q113. 以下关于Amazon CloudFront的陈述正确的是,当您可以控制objects在CloudFront cache中的存留时间,直到它再次向origin发送请求时:

- [ ] 减少time to live可以提供dynamic content。
- [ ] 增加time to live意味着用户可以获得更好的performance。
- [ ] 较长的time to live也可以减少origin的负载。
- [x] All of the above。

#### Q114. 您的任务是支持移动应用的用户。该应用允许用户查看content(例如图片),但只有登录到应用的用户才能上传图片。以下选项中,哪种方法开发时间最短且安全性最高,以防止未认证用户发布content?

- [ ] 创建一个Cognito Identity Pool,为authorized和unauthorized用户分配roles,并在这些roles上设置适当的permissions。
- [ ] 根据用户的login state在runtime切换API access keys。
- [ ] 在database table (DynamoDB或RDS)上设置user permissions policies。
- [x] 为public use暴露一个API Gateway来fetch content,并为需要auth token的content写入暴露第二个API。

#### Q115. 如果用户需要programmatic access您的AWS resources,authentication需要什么?

- [x] Access Keys
- [ ] Key pair
- [ ] 用户账户上启用MFA
- [ ] 角色association

[Reference](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)

#### Q116. \***\*\_\_\_\*\***是预定义的、out-of-the-box policies,授予common use cases的permissions,无需确定所需permissions。

- [ ] Resource policies
- [x] AWS managed policies
- [ ] Customer managed policies
- [ ] Inline policies

[Reference](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)

#### Q117. 在IAM policy中,**\_\_** **\_ \_\_\_\_**是top-level policy elements,而其余的是statement-level elements。

- [ ] ID和Principal
- [ ] Version和ID
- [ ] ID和Statement
- [x] Version和Statement

[Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)

#### Q118. 返回流量到VPC新public subnet的所有EC2实例被某种方式阻止。您希望确保未来接收到所有potential clients的return traffic。应该允许哪个port range以确保接收到所有potential clients的return traffic?

- [ ] 1-1024
- [x] 1024-65535
- [ ] 1024-50000
- [ ] 1-65535

[Reference](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#VPC_ACLs_Ephemeral_Ports)

#### Q119. 您管理公司的AWS credentials,该公司正在onboarding两名新员工:一名是HR administrator,另一名是developer。Dev团队规模较大,并在公司AWS accounts中有一个IAM group,但Human Resources目前只有一名员工,且没有扩展部门的计划。公司policy要求以便于在promotions或resignations情况下简单reassignment的方式为AWS员工提供long-term credentials。如何为新developer提供适当的AWS access并遵循公司policy?(选择2个答案)

- [ ] 将适当的IAM policies attach到新developer的IAM user。
- [x] 将新developer添加到Developer IAM Group。
- [ ] 将新的IAM role attach到新developer的IAM user。
- [x] 为developer创建一个新的IAM user。

[Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

#### Q120. 以下哪个是fully-managed AWS database service?

- [ ] Amazon s3
- [x] Amazon RDS
- [ ] Amazon MQ
- [ ] Amazon VPC

#### Q121. 哪个AWS database service是fully managed、serverless、multi-model database,支持document、key-value和wide-column data models?

- [ ] Amazon RDS
- [ ] Amazon Redshift
- [x] Amazon DynamoDB
- [ ] Amazon Neptune
- [ ] Amazon Aurora

#### Q122. 哪项AWS service主要用于随时随地从网络上store和retrieve任意数量的data?

- [ ] Amazon EC2
- [x] Amazon S3
- [ ] Amazon RDS
- [ ] AWS Lambda

**Explanation**

- Amazon S3 (Simple Storage Service)是一种object storage service,允许用户随时store和retrieve任意数量的data。它设计为highly durable和scalable,适合存储各种data types,包括web applications、backups和large data lakes。EC2 (Elastic Compute Cloud)用于scalable computing capacity,RDS (Relational Database Service)用于relational databases,而AWS Lambda用于运行code而无需provisioning或managing servers。

#### Q123. 在single PUT operation中上传到Amazon S3的single object的maximum size是多少?

- [x] 5 GB
- [ ] 100 GB
- [ ] 10 GB
- [ ] 500 MB

**Explanation**

- Amazon S3允许single PUT operation上传最大5 GB的single object。对于超过5 GB的objects,用户需要使用multipart upload,该功能支持最大5 TB的objects。multipart upload功能允许parallel uploads,从而使较大files的upload process更快、更efficient。

#### Q124. 以下哪项service用于自动distribute incoming application traffic到multiple targets,例如EC2 instances、containers和IP addresses?

- [ ] Amazon Route 53
- [ ] AWS Auto Scaling
- [x] AWS Elastic Load Balancer (ELB)
- [ ] AWS CloudFront

**Explanation**

- AWS Elastic Load Balancer (ELB)旨在自动distribute incoming traffic到multiple targets,例如EC2 instances或containers,以确保high availability和fault tolerance。Route 53用于domain name system (DNS) services,Auto Scaling用于自动调整instances数量,而CloudFront是一种content delivery network (CDN),用于以low latency分发content。

#### Q125. 你是一家IT公司的cloud consultant。由于大多数employees在家工作,你需要找到一种方法为他们提供secure access公司internal sites和SaaS applications的途径。你会建议使用以下哪项AWS service?

- [ ] AWS Direct Connect
- [ ] AWS VPN CloudHub
- [x] Amazon WorkSpaces Web
- [ ] Amazon Storage Gateway

#### Q126. 哪项AWS service可以将text转换为lifelike speech?

- [ ] Amazon Translate
- [x] Amazon Polly
- [ ] Amazon Rekognition
- [ ] Amazon Comprehend

以下是两个额外的AWS questions及options和explanations:

#### Q127. 哪项AWS service允许您为organization创建和管理private Certificate Authority (CA)?

- [ ] AWS Certificate Manager
- [ ] AWS Secrets Manager
- [x] AWS Private Certificate Authority
- [ ] AWS Identity and Access Management

**Explanation**  
此AWS service允许您为organization创建和管理private Certificate Authority (CA),从而能够issue和manage private SSL/TLS certificates。这对于securing无法从public internet访问的internal applications和services非常有用。

#### Q128. 您有一个application需要access Amazon RDS for MySQL database。以下哪种方法是securely connect application到database的推荐方式?

- [ ] 使用RDS instance的public IP address并directly从application connect。
- [ ] 使用RDS instance的DNS endpoint并directly从application connect。
- [x] 在与RDS instance相同的VPC中的private subnet中launch application,并使用private IP address进行connect。
- [ ] 使用AWS Lambda function作为proxy connect application到RDS instance。

**Explanation**  
正确答案是:在与RDS instance相同的VPC中的private subnet中launch application,并使用private IP address进行connect。
