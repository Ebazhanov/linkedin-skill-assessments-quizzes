Q1. When a javaScript function is invoked (called) in Node, where is a new frame placed?
- the call stack <<<<-----Correct
- the event loop
- the poll phase
- the events queue

Q2. Which of the following is a core module in Node?
- webpack
- crypto <<<<-----Correct
- request
- chalk

Q3. Which of the following Buffer class methods returns an uninitialized buffer?
- allocUnsafe <<<<-----Correct
- concat
- from
- alloc

Q4. Which of the following modues is NOT a built-in module in Node?
- ftp <<<<-----Correct
- events
- dgram
- http2

Q5. Which fs module method can be used to read the content of a file without buffering it in memory?
- read <<<<----Might be
- readFile
- createReadStream
- readFileSync

Q6. Which of the following DNS module methods uses the underlying OS facilities and does not necessarily perfrom any network communication?
- lookup <<<<----Correct
- resolve
- resolve4
- reverse

Q7. How do you check that a value is a date object in Node?
- util.types.isDate(value) <<<<----Correct
- assert.isDate(value)
- console.isDate(value)
- util.date(value)

Q8. Can you create an https web server with Node.js?
- no, there are no modules supporting it yet
- yes, with the https or http2 modules <<<<----Correct
- yes, through the path module
- yes, with the http module

Q9. What is the Api that is designed to insulate Addons from changes in the underlying JavaDcript engine?
- A-API
- Z-API
- N-API <<<<----Correct
- X-API

Q10. Which CLI option can you use to debug a node script in Chrome DevTools?
- --dev-tools
- --inspect <<<<----Correct
- --chrome
- --debug

Q11. How can you count the number of logical CPUs on the machine that is running Node?
- node -p "process.cpus"
- node -p "util.cpus().size"
- node -p "process.os.cpus"
- node -p "os.cpus().length" <<<<----Correct

Q12. Which of the following is a method on the console obejct?
- exit
- test
- time <<<<----Correct
- print

Q13. Which object is used to manage the cache of required modules?
- global.cache
- module.cache
- process.cache
- require.cache <<<<----Correct

Q14. What is the command to silence all process warnings?
- node index.js --trace-warnings
- node --no-warings <<<<----Correct
- node -trace-warnings
- node index.js --no-warnings

Q15. How can you use the promise API with a callback-based function like child_process.exec?
- new Promise(child_process.exec())
- util.promisify(child_process.exec())
- util.promisify(child_process.exec)
- new Promise(child_process.exec) <<<<----Correct

Q16. Which of the following is NOT a Node repl command?
- .brake
- .history <<<<----Correct
- .editor
- .save

Q17. Which statement is true when you run the code shown below?
```js
require('child_process').fork('script.js');
```
- The forked process shares the event loop with the parent process
- A new VM instance is created and the two VM instances will be shared between the forked process and the prent process.
- The forked process will have its own VM instance. <<<<----May be
- The forked process shares the same VM thread with the parent process.

Q18. If EventEmitter is in scope, which of the following lines of code will have an event emitter emitting a change event?
- EventEmitter.emit(change);
- EventEmitter.new().emit(change);
- (new EventEmitter()).emit(change);
- new EventEmitter(change);  <<<<----Correct

Q19. Which of th following objects is a stream
- process.uptime
- process.stdout
- process
- Buffer <<<<-----Correct

Q20. Whichmodule variable holds the resolved aboslue path of the current module file?
- __pathname
- __location
- __flder
- __filename <<<<----Correct

Q21. If the child_process module methods are in scope, what is a current way to execute the command ps -ef using a child process?
- spawn("ps -ef") <<<<----Correct
- exec("ps -ef")
- exec("ps", "-ef")
- fork("ps -ef")
