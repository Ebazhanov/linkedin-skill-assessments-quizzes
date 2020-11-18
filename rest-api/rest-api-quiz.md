## REST API Assessment

---

#### Q1. What type of relationship is defined as one resource existing only if another parent resource exist-for example, pages in a book?

- [ ] `Partial`
- [ ] `dependent`
- [ ] `associative`
- [ ] `linked`

#### Q2. Which URL pattern s recommended when working with one resource and a collection of resources?

- [ ] `/companies/{id} and/company`
- [ ] `/company/{id} and/companies`
- [x] `/companies/{id} and/companies`
- [ ] `/company/{id} and/company`

#### Q3. When dealing with JSON web Tokens (JWTs), what is a claim?

- [x] `data in the token`
- [ ] `Ownership`
- [ ] `a permission`
- [ ] `and integer`

#### Q4. Which REST contraint specifies that knowledge and understanding obtained from one component of the API should be generally applicable elsewhere in the API?

- [x] `Uniform Interface`
- [ ] `Client-Server`
- [ ] `Stateless`
- [ ] `Chacheable`

#### Q5. What would you enable to allow a browser on another site to make an AJAX request to your API?

- [ ] `HTTP`
- [ ] `REST`
- [ ] `OPTIONS`
- [x] `CORS`

#### Q6. APIs commonly use webhooks to **\*\*\*\***\_\_\_\_**\*\*\*\***.

- [x] `notify other systems of an event`
- [ ] `catch error faster`
- [ ] `improve error logging`
- [ ] `log additional data`

#### Q7. What is the underlying goal of all APIs?

- [ ] `to add new technologies to an organization's infrastructure.`
- [x] `to share features and functionality with other system.`
- [ ] `to move infrastructure to the cloud.`
- [ ] `to appease the latest digital transformation effort.`

#### Q8. Which is a common command-line tool for using or exploring an API?

- [ ] `bash`
- [x] `curl`
- [ ] `ssh`
- [ ] `powerShell`

#### Q9. What is the modern specification for describing an API?

- [x] `OpenAPI (Swagger)`
- [ ] `WADL`
- [ ] `WSDL`
- [ ] `OAuth`

#### Q10. Which HTTP verb is normally used to update or create a resource in an API?

- [ ] `SUBMIT`
- [ ] `WRITE`
- [x] `POST`
- [ ] `CREATE`

#### Q11. What is one benefit of server-side caching in APIs?

- [ ] `Mobile app work better.`
- [ ] `It improves uptime.`
- [ ] `It offers better security.`
- [x] `It reduce load on servers.`

#### Q12. Your API resource does no allow deletion, and a client application attempted to delete the resource. What HTTP respose code should you return?

- [ ] `409 Conflict`
- [ ] `400 Bad Request`
- [ ] `406 Not Acceptable`
- [x] `405 Method Not Allowed`

#### Q13. What is OpenID Connect?

- [x] `an identify layer on top of OAuth 2.0`
- [ ] `the new name for SAML 3.0`
- [ ] `a modern replacement for API keys`
- [ ] `an SSO competitor for OAuth 2.0`

#### Q14. What is one benefit of GraphQl over REST approaches?

- [x] `flexible querying/responses`
- [ ] `more stable APIs`
- [ ] `compatible with more gateways`
- [ ] `more secure by default`

#### Q15. Which REST constraint specifies that there should be no shared context?

- [x] `Stateless`
- [ ] `Client-Server`
- [ ] `Uniform Interface`
- [ ] `Cacheable`

#### Q16. What purpose does a User-Agent serve?

- [ ] `It identifies the user ID.`
- [x] `It identifies the client application or SDK.`
- [ ] `It identifies if the API should expect a user authentication.`
- [ ] `It identifies if the API should accept microservice traffic.`

#### Q17. If you were to add versioning by using the Accept and Content-Type header, what would be the correct format of the header value?

- [ ] `application/json`
- [ ] `application/json_version2`
- [x] `text/html`
- [ ] `application/vnd.myapp.v2+json`

#### Q18. What is one benefit that OAuth provides over an API key approach?

- [ ] `A token is encrypted.`
- [ ] `A token is encoded.`
- [x] `A token is scoped to the use case.`
- [ ] `A token can be shared between systems.`

#### Q19. The ability to execute the same API request over and over again without changing the resource's state is an example of **\_**.

- [ ] `stateless architecture`
- [x] `idempotency`
- [ ] `a uniform interface`
- [ ] `cacheability`

#### Q20. What component can you use to wrap legacy architectures or protocols into a REST interface for easier consumption and integration?

- [x] `API proxy`
- [ ] `API gateway`
- [ ] `OpenAPI`
- [ ] `OAuth authorization server`

#### Q21. What protection does a JSON Web Token (JWT) offer to mitigate tampering with its contents?

- [ ] `transport over SSL`
- [ ] `encrypted payload`
- [x] `a signature`
- [ ] `encoded payload`

#### Q22. What OAuth term is used to represent permissions?

- [ ] `token`
- [x] `scope`
- [ ] `claim`
- [ ] `back channel`

#### Q23. What additional type of token would you see when using OpenID Connect?

- [x] `ID token`
- [ ] `refresh token`
- [ ] `access token`
- [ ] `auth code token`

#### Q24. What should you add to a Cache-Control response header to specify that a response should not be stored in an intermediary cache?

- [ ] `no-proxy`
- [ ] `client-only`
- [ ] `restricted`
- [x] `private`
      [reference](https://www.digitalocean.com/community/tutorials/web-caching-basics-terminology-http-headers-and-caching-strategies)

#### Q25. Which OAuth grant type can support a refresh token?

- [ ] `Authorization Code Grant`
- [x] `Client Credentials Grant`
- [ ] `Implicit Grant`
- [ ] `Authentication Grant`

#### Q26. Using OAuth, what scope would you request for write access to the API?

- [ ] `It varies from API to API.`
- [x] `admin`
- [ ] `write`
- [ ] `read-write`

#### Q27. Which property would you use to include subresources directly into a JSON document?

- [ ] `\_embedded`
- [ ] `resources`
- [x] `subresources`
- [ ] `\_links`

#### Q28. What is the best way to track SDK and version usage?

- [x] `tracking downloads`
- [ ] `Accept headers`
- [ ] `user agents`
- [ ] `polling users`

#### Q29. Which REST constraint allows for the presence of caching, routing, and other systems between the client and server?

- [ ] `Layered System`
- [ ] `Stateless`
- [ ] `Client-Server`
- [ ] `Cacheable`

#### Q30. Which content is best to include in your documentation?

- [ ] `your tech stack`
- [ ] `reasoning for your naming schema`
- [ ] `your mission statement`
- [x] `sample code`

#### Q31. What metric tracks overall availability for your API?

- [ ] `Response Time`
- [ ] `Time to First Hello World`
- [ ] `TTL`
- [x] `Uptime`

#### Q32. What is the recommended method and URL pattern for retrieving a specific user?

- [ ] `GET /user/{id}`
- [x] `GET /users/{id}`
- [ ] `GET /user?id={id}`
- [ ] `GET /users?id={id}`

#### Q33. What is the purpose of a link relation?

- [ ] `to describe relationships between resources or actions`
- [ ] `to describe subresources related to the current one`
- [ ] `to link two resources together`
- [ ] `to describe a resource and its purpose`

#### Q34. When building SDKs, which languages should you support?

- [ ] Java, Javascript, and .NET
- [ ] and you can support
- [ ] PHP, Python, and Go
- [ ] the languages that your target users use

#### Q35. Which property would you use to include references to other resources in a JSON document?

- [ ] resources
- [ ] _embedded
- [ ] subresources
- [ ] _links

#### Q36. What is OAuth?

- [ ] an authorization framework for granted delegated access
- [ ] an approach to single sign-on for APIs
- [ ] a method for API authentication
- [ ] HTTP Basic Authentication 2.0

#### Q37. What should your API documentation describe?

- [ ] JSON
- [ ] HTTP
- [ ] common use cases
- [ ] your tech stack

#### Q34. What is the purpose of an OAuth refresh token?

- [ ] to share user profile information
- [ ] to update an API configuration
- [ ] to keep a web session active
- [ ] to retrive an access token

