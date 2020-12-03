#### Q1. When a javaScript function is invoked (called) in Node, where is a new frame placed?

    - the call stack <<<<-----Correct
    - the event loop
    - the poll phase
    - the events queue

#### Q2. Which of the following is a core module in Node?

    - webpack
    - crypto <<<<-----Correct
    - request
    - chalk

#### Q3. Which of the following Buffer class methods returns an uninitialized buffer?

    - allocUnsafe <<<<-----Correct
    - concat
    - from
    - alloc

#### Q4. Which of the following modules is NOT a built-in module in Node?

    - ftp <<<<-----Correct
    - events
    - dgram
    - http2

#### Q5. Which fs module method can be used to read the content of a file without buffering it in memory?

    - read
    - readFile
    - createReadStream <<<<----Correct
    From official docs: [https://nodejs.org/api/fs.html#fs_dir_read](https://nodejs.org/api/fs.html#fs_dir_read)
    To minimize memory costs, when possible prefer streaming via fs.createReadStream().
    - readFileSync

#### Q6. Which of the following DNS module methods uses the underlying OS facilities and does not necessarily perform any network communication?

    - lookup <<<<----Correct
    - resolve
    - resolve4
    - reverse

#### Q7. How do you check that a value is a date object in Node?

    - util.types.isDate(value) <<<<----Correct
    - assert.isDate(value)
    - console.isDate(value)
    - util.date(value)

#### Q8. Can you create an https web server with Node.js?

    - no, there are no modules supporting it yet
    - yes, with the https or http2 modules <<<<----Correct
    - yes, through the path module
    - yes, with the http module

#### Q9. What is the Api that is designed to insulate Addons from changes in the underlying JavaScript engine?

    - A-API
    - Z-API
    - N-API <<<<----Correct
    - X-API

#### Q10. Which CLI option can you use to debug a node script in Chrome DevTools?

    - --dev-tools
    - --inspect <<<<----Correct
    - --chrome
    - --debug

#### Q11. How can you count the number of logical CPUs on the machine that is running Node?

    - node -p "process.cpus"
    - node -p "util.cpus().size"
    - node -p "process.os.cpus"
    - node -p "os.cpus().length" <<<<----Correct

#### Q12. Which of the following is a method on the console obejct?

    - exit
    - test
    - time <<<<----Correct
    - print

#### Q13. Which object is used to manage the cache of required modules?

    - global.cache
    - module.cache
    - process.cache
    - require.cache <<<<----Correct

#### Q14. What is the command to silence all process warnings?

    - node index.js --trace-warnings
    - node --no-warnings <<<<----Correct
    - node -trace-warnings
    - node index.js --no-warnings

#### Q15. How can you use the promise API with a callback-based function like child_process.exec?

    - new Promise(child_process.exec())
    - util.promisify(child_process.exec())
    - util.promisify(child_process.exec) <<<<----Correct
    - new Promise(child_process.exec)

#### Q16. Which of the following is NOT a Node repl command?

    - .brake
    - .history <<<<----Correct
    - .editor
    - .save

#### Q17. Which statement is true when you run the code shown below?

    ```js
    require('child_process').fork('script.js');
    ```
    - The forked process shares the event loop with the parent process
    - A new VM instance is created and the two VM instances will be shared between the forked process and the parent process.
    - The forked process will have its own VM instance. <<<<----May be
    - The forked process shares the same VM thread with the parent process.

#### Q18. If EventEmitter is in scope, which of the following lines of code will have an event emitter emitting a change event?

    - EventEmitter.emit(change);  <<<<----Correct //Because the EventEmitter is already in scope. No need to create new one.
    - EventEmitter.new().emit(change);
    - (new EventEmitter()).emit(change);
    - new EventEmitter(change);

#### Q19. Which of the following objects is a stream

    - process.uptime
    - process.stdout <<<<-----Correct // Buffer is Buffer type.
    - process
    - Buffer

#### Q20. Which module variable holds the resolved aboslute path of the current module file?

    - __pathname
    - __location
    - __flder
    - __filename <<<<----Correct

#### 21. If the child_process module methods are in scope, what is a current way to execute the command ps -ef using a child process?

    - spawn("ps -ef")
    - exec("ps -ef") <<<<-----Correct
    - exec("ps", "-ef")
    - fork("ps -ef")

#### Q22.Which console method can be used to print the stack trace to the point of its execution?

    - stack
    - trace ---> correct
    - debug
    - print

#### Q23.When you run JavaScript in a Node.js application, which of the following elements in a Node.js stack actually executes that JavaScript?

     - the libuv library
     - the c-ares library
     - the VM (like VS or Chakra)-----> correct
     - the repl module

#### Q24. Looking at the code below, what does the console show?

```const http = require('http');
 const hostname = '127.0.0.1'; const port = 3000;
 const server = http.createServer((req, res) => {
  res.statusCode = 200;  res.setHeader("Content-Type", "text/plain");  res.end("Hello World\n");
});
server.listen(port, hostname, () => { console.log(`server running at http://${hostname}:${port}/`); });
```

    -  server running at http://localhost:3000/
    -  server running at port 3000
     - server running at http://localhost:4000/
    -  server running at http://127.0.0.1:3000/ -----> correct

#### Q25.What is the purpose of the path module?

    -  to provide utilities to play with file and directory paths -----> correct
    -  to provide utilities to add and remove files
    -  It is a retiring module.
    -  to provide utilities to test files

#### Q26.How do you make an HTTP server object active and listen to requests on certain ports?

    - server. start
    - server.activate
    - server.listen -----> correct
    - server. run

#### Q27.What does the code shown below do?

```
const fs = require('fs'); const os o require('os');
const system = os.platform(); const user = os.userInfo().username;
fs.appendFilechello.txt'l 'Hello ${user} on ${system}r, (err) => { if (err) throw err; console.log('The data was appended to file!');
) ;
```

    -  creates a text file hello.txt and appends customized text -----> correct
    -  creates an image file
    -  console logs system information
    -  creates a file named data and append numbers

#### Q28.How do you start a Node application, if the entry file is indexjs?

    -  nodemon start
    -  start index.js
    -  node index.js -----> correct
     - node start

#### Q29.What is the purpose of the file system (fs) module?

    - to provide methods to work with requests and responses
    - to provide methods to work with files -----> correct
    - to provide methods to work with databases
    - to find new file systems

#### Q30.What is the Node LTS version?

    -  It is the current unstable version and is to be avoided.
    -  It is the version that will be retired soon.
    -  It is the version with the latest features.
    -  It is the safest version for long-term support. -----> correct

#### Q31. Which of the following is NOT a valid stream in Node?

    - process. stdinfo -----> correct
    - process. stdin
    - process. stdout
    - process. stderr

#### Q32. You have a script.js file with the single line of code shown here. What will be the output of executing script.js with the node command?

`console.log(arguments);` - ReferenceError: arguments is not defined - an empty string - undefined - an object representing an array that has five elements -----> correct

### Q33. Which choice is null a valid method on event emitters?

- [ ] startnull
- [ ] onnull
- [ ] oncenull
- [ ] off

### Q34. Which special object is an instance of EventEmitter?Which special object is an instance of null?

- [ ] processnull
- [ ] Buffernull
- [ ] rootnull
- [ ] require

### Q35. What is the command to get a list of available commands for Node.js?What is the command to get a list of available commands for Node.js?

- [ ] node index.js -xnull
- [ ] node -vnull
- [ ] node -hnull
- [ ] node index.js -h

### Q36. When a request event is received in the HTTP module, what is the type of the first argument passed to that event, usually named req?When a request event is received in the HTTP module, what is the type of the first argument passed to that event, usually named null?

- [ ] http.IncomingMessagenull
- [ ] http.ServerRequestnull
- [ ] http.ClientRequestnull
- [ ] http.ServerResponse
