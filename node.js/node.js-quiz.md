## Node.js

#### Q1. When a javaScript function is invoked (called) in Node, where is a new frame placed?

- [x] the call stack
- [ ] the event loop
- [ ] the poll phase
- [ ] the events queue

#### Q2. Which of the following is a core module in Node?

- [ ] webpack
- [x] crypto
- [ ] request
- [ ] chalk

#### Q3. Which of the following Buffer class methods returns an uninitialized buffer?

- [x] allocUnsafe
- [ ] concat
- [ ] from
- [ ] alloc

#### Q4. Which of the following modules is NOT a built-in module in Node?

- [x] ftp
- [ ] events
- [ ] dgram
- [ ] http2

#### Q5. Which fs module method can be used to read the content of a file without buffering it in memory?

- [ ] read
- [ ] readFile
- [x] createReadStream
- [ ] readFileSync

**Explanation:**

_From official docs: [https://nodejs.org/api/fs.html#fs_dir_read](https://nodejs.org/api/fs.html#fs_dir_read)
To minimize memory costs, when possible prefer streaming via fs.createReadStream()._

#### Q6. Which of the following DNS module methods uses the underlying OS facilities and does not necessarily perform any network communication?

- [x] lookup
- [ ] resolve
- [ ] resolve4
- [ ] reverse

#### Q7. How do you check that a value is a date object in Node?

- [x] util.types.isDate(value)
- [ ] assert.isDate(value)
- [ ] console.isDate(value)
- [ ] util.date(value)

#### Q8. Can you create an https web server with Node.js?

- [ ] no, there are no modules supporting it yet
- [x] yes, with the https or http2 modules
- [ ] yes, through the path module
- [ ] yes, with the http module

#### Q9. What is the Api that is designed to insulate Addons from changes in the underlying JavaScript engine?

- [ ] A-API
- [ ] Z-API
- [x] N-API
- [ ] X-API

#### Q10. Which CLI option can you use to debug a node script in Chrome DevTools?

- [ ] --dev-tools
- [x] --inspect
- [ ] --chrome
- [ ] --debug

#### Q11. How can you count the number of logical CPUs on the machine that is running Node?

- [ ] node -p "process.cpus"
- [ ] node -p "util.cpus().size"
- [ ] node -p "process.os.cpus"
- [x] node -p "os.cpus().length"

#### Q12. Which of the following is a method on the console object?

- [ ] exit
- [ ] test
- [x] time
- [ ] print

#### Q13. Which object is used to manage the cache of required modules?

- [ ] global.cache
- [ ] module.cache
- [ ] process.cache
- [x] require.cache

#### Q14. What is the command to silence all process warnings?

- [ ] node index.js --trace-warnings
- [x] node --no-warnings
- [ ] node -trace-warnings
- [ ] node index.js --no-warnings

#### Q15. How can you use the promise API with a callback-based function like child_process.exec?

- [ ] new Promise(child_process.exec())
- [ ] util.promisify(child_process.exec())
- [x] util.promisify(child_process.exec)
- [ ] new Promise(child_process.exec)

#### Q16. Which of the following is NOT a Node repl command?

- [ ] .brake
- [x] .history
- [ ] .editor
- [ ] .save

#### Q17. Which statement is true when you run the code shown below?

`require('child_process').fork('script.js');`

- [ ] The forked process shares the event loop with the parent process
- [ ] A new VM instance is created and the two VM instances will be shared between the forked process and the parent process.
- [x] The forked process will have its own VM instance.
- [ ] The forked process shares the same VM thread with the parent process.

#### Q18. If EventEmitter is in scope, which of the following lines of code will have an event emitter emitting a change event?

- [x] EventEmitter.emit('change');
- [ ] EventEmitter.new().emit('change');
- [ ] (new EventEmitter()).emit('change');
- [ ] new EventEmitter('change');

**Explanation:**

_Because the EventEmitter is already in scope. No need to create new one._

#### Q19. Which of the following objects is a stream

- [ ] process.uptime
- [x] process.stdout
- [ ] process
- [ ] Buffer

**Explanation:**

_process.stdout is Buffer type._

#### Q20. Which module variable holds the resolved aboslute path of the current module file?

- [ ] \_\_pathname
- [ ] \_\_location
- [ ] \_\_flder
- [x] \_\_filename

#### 21. If the child_process module methods are in scope, what is a current way to execute the command ps -ef using a child process?

- [ ] spawn("ps -ef")
- [x] exec("ps -ef")
- [ ] exec("ps", "-ef")
- [ ] fork("ps -ef")

#### Q22.Which console method can be used to print the stack trace to the point of its execution?

- [ ] stack
- [x] trace
- [ ] debug
- [ ] print

#### Q23.When you run JavaScript in a Node.js application, which of the following elements in a Node.js stack actually executes that JavaScript?

- [ ] the libuv library
- [ ] the c-ares library
- [x] the VM (like VS or Chakra)
- [ ] the repl module

#### Q24. Looking at the code below, what does the console show?

```
const http = require('http');
 const hostname = '127.0.0.1'; const port = 3000;
 const server = http.createServer((req, res) => {
  res.statusCode = 200;  res.setHeader("Content-Type", "text/plain");  res.end("Hello World\n");
});
server.listen(port, hostname, () => { console.log(`server running at http://${hostname}:${port}/`); });
```

- [ ] server running at http://localhost:3000/
- [ ] server running at port 3000
- [ ] server running at http://localhost:4000/
- [x] server running at http://127.0.0.1:3000/

#### Q25.What is the purpose of the path module?

- [x] to provide utilities to play with file and directory paths
- [ ] to provide utilities to add and remove files
- [ ] It is a retiring module.
- [ ] to provide utilities to test files

#### Q26.How do you make an HTTP server object active and listen to requests on certain ports?

- [ ] server. start
- [ ] server.activate
- [x] server.listen
- [ ] server. run

#### Q27.What does the code shown below do?

```
const fs = require('fs'); const os = require('os');
const system = os.platform(); const user = os.userInfo().username;
fs.appendFile('hello.txt', `Hello ${user} on ${system}`, (err) => { if (err) throw err; console.log('The data was appended to file!');}
);
```

- [x] creates a text file hello.txt and appends customized text
- [ ] creates an image file
- [ ] console logs system information
- [ ] creates a file named data and append numbers

#### Q28.How do you start a Node application, if the entry file is indexjs?

- [ ] nodemon start
- [ ] start index.js
- [x] node index.js
- [ ] node start

#### Q29.What is the purpose of the file system (fs) module?

- [ ] to provide methods to work with requests and responses
- [x] to provide methods to work with files
- [ ] to provide methods to work with databases
- [ ] to find new file systems

#### Q30.What is the Node LTS version?

- [ ] It is the current unstable version and is to be avoided.
- [ ] It is the version that will be retired soon.
- [ ] It is the version with the latest features.
- [x] It is the safest version for long-term support.

#### Q31. Which of the following is NOT a valid stream in Node?

- [x] process. stdinfo
- [ ] process. stdin
- [ ] process. stdout
- [ ] process. stderr

#### Q32. You have a script.js file with the single line of code shown here. What will be the output of executing script.js with the node command?

`console.log(arguments);`

- [ ] ReferenceError: arguments is not defined
- [ ] an empty string
- [ ] undefined
- [x] an object representing an array that has five elements

#### Q33. Which choice is not a valid method on event emitters?

- [x] start
- [ ] on
- [ ] once
- [ ] off

#### Q34. Which special object is an instance of EventEmitter?Which special object is an instance of null?

- [ ] process
- [ ] Buffer
- [ ] root
- [x] require

#### Q35. What is the command to get a list of available commands for Node.js?What is the command to get a list of available commands for Node.js?

- [ ] node index.js -x
- [ ] node -v
- [x] node -h
- [ ] node index.js -h

#### Q36. When a request event is received in the HTTP module, what is the type of the first argument passed to that event, usually named req?

- [x] http.IncomingMessage
- [ ] http.ServerRequest
- [ ] http.ClientRequest
- [ ] http.ServerResponse

#### Q37. What are the arguments passed to the module wrapper function?

- [ ] exports, **filename, **dirname
- [ ] exports, process, require, module, **filename, **dirname
- [ ] exports, module, **filename, **dirname
- [x] exports, require, module, **filename, **dirname

#### Q38. Which library provides Node.js with the event loop?

- [ ] V8
- [ ] c-ares
- [x] libuv
- [ ] events

#### Q39. What does the .node file extension represent?

- [ ] a C++ file that can have a .node extension and that Node will be able to execute directly.
- [x] a C++ Addon file that is built with node-gyp
- [ ] a JSON file that can have a .node extension as well as the .json extension
- [ ] a JavaScript file that can have a .node extension as well as the .js extension

#### Q40. What can you export with module.exports?

- [ ] only objects.
- [ ] only functions
- [ ] only variables and arrays
- [x] functions, objects, arrays, or anything you assign to the module

#### Q41. Which core module in Node can you use to take advantage of multicore systems?

- [ ] os
- [ ] util
- [x] cluster
- [ ] net

#### Q42. Which core Node module has wrappers for OpenSSL methods?

- [ ] SSL
- [ ] hash
- [x] crypto
- [ ] TLS

#### Q43. Which line imports a promise-based version of the readFile method?

- [x] const { readFile } = require(fs).promises
- [ ] const { readFile } = require(fs)
- [ ] const { readFilePromises: readFile } = require(fs)
- [ ] const { readFile } = require(promises)

#### Q44. According to the rules of semantic versioning, what does a release incrementing the third number in an npm version string communicate to users about the release changes?

- [ ] Changes are not backwards compatible.
- [ ] Changes might not be backward compatible and might break existing code.
- [x] Changes are just bug fixes and no new features were added.
- [ ] Changes will add new functionality but will not break any existing code.

#### Q45. What does REPL stand for?

- [ ] run, examine, put, loop
- [x] read, eval, print, loop
- [ ] run, edit, print, loop
- [ ] read, extend, print, loop

#### Q46. Which file does node-gyp use to read the build configuration of module ?

- [ ] .gyprc
- [x] binding.gyp
- [ ] gyp.json
- [ ] package.gyp

#### Q47. Which core module in Node can you use for testing?

- [ ] chai
- [ ] jest
- [x] assert
- [ ] mocha

#### Q48. Which core module in Node provides an API to register callbacks to track asynchronous resources created inside a Node.js application?

- [ ] cluster
- [x] async_hooks
- [ ] dgram
- [ ] inspector

#### Q49. Which Node.js module should you use when you need to decode raw data into strings?

- [ ] buffer
- [ ] util
- [x] string_decoder
- [ ] string_buffer

#### Q50. Which global object acts like a bridge between a Node script and the host operating system?

- [ ] v8
- [ ] env
- [x] process
- [ ] child_process

**Explanation:**

_process is an global object and act like a bridge, the others aren't (please see https://nodejs.org/api/globals.html or https://nodejs.org/api/process.html#process_process)._

#### Q51. Which statement is true about Node.js and threads?

- [ ] Every Node process runs in a single thread, and all the I/O work is run in that same thread.
- [ ] Every Node process gets four threads that it can share between its JavaScript VM and the event loop.
- [x] The event loop is single-threaded, but a JavaScript VM can use multiple threads.
- [ ] JavaScript execution in Node.js is single-threaded, but I/O operations are executed using multiple threads.

**Explanation:**

_https://www.geeksforgeeks.org/why-node-js-is-a-single-threaded-language/_

#### Q52. Which statement about event emitters is false?

- [x] Event names must be camelCase strings.
- [ ] The emit method allows a arbitrary set of arguments to be passed to the listener functions.
- [ ] Any values returned by the listeners for an emitted events are ignored.
- [ ] When an event emitter objeect emits an event, all of the functions attached to that specific event are called synchronously.

#### Q53. Which core module in Node can you use to compile and run JavaScript code in a sandbox environment?

- [ ] sandbox
- [ ] buffer
- [x] vm
- [ ] v8

#### Q54. How would you determine the number of cluster instances to start when using the cluster module?

- [ ] const numInstances = cluster.instances().length;
- [ ] const numInstances = cluster.instances();
- [ ] const numInstances = require('os').cpus().length;
- [x] const numInstances = process.cpus().length;

**Explanation:**

_From official docs: [https://nodejs.org/api/cluster.html#cluster_cluster](https://nodejs.org/api/cluster.html#cluster_cluster)_

#### Q55. You have to read a large text file, replace some words in it, and write it back to a new file. You know that the memory on your target system is limited. What should you do?

- [ ] Use regular expressions directly on the file.
- [ ] Use Promises and async/await to offload the task to libuv.
- [ ] Copy the file into a database and perform the operations there.
- [x] Use readline together with streams to read and transform and write the file contents line by line.

**Explanation:**

_From official docs: [https://nodejs.org/api/readline.html#readline_example_read_file_stream_line_by_line](https://nodejs.org/api/readline.html#readline_example_read_file_stream_line_by_line)_

#### Q56. Which choice is not a global object?

- [ ] process
- [ ] exports
- [ ] setTimeout
- [x] Buffer

**Explanation:**

_process, exports and setTimeout are global objects, Buffer isn't (please see https://nodejs.org/api/globals.html)_
