## SOLIDITY

#### Q1. In a Solidity contract, what is the purpose of the "view" and "pure" function modifiers?

- [ ] "view" modifies a function to prevent external calls, while "pure" indicates a function is non-constant.
- [x] "view" signifies a function will not alter the contract's state, while "pure" implies it won't even read the state.
- [ ] "view" restricts a function's visibility to the contract owner, while "pure" makes it inaccessible from other contracts.
- [ ] "view" and "pure" are used interchangeably and have no distinct purpose.

#### Q2. What is the purpose of the "revert" statement in Solidity?

- [ ] To reject incoming Ether payments
- [x] To terminate the execution of a function without reverting state changes
- [ ] To refund gas fees to the caller
- [ ] To provide an alias for custom error messages

#### Q3. Which Ethereum gas cost is typically the most expensive in a Solidity contract execution?

- [ ] SLOAD (storage load)
- [x] SSTORE (storage store)
- [ ] GAS (base cost)
- [ ] CALL (external contract call)

#### Q4. What is the purpose of the "assembly" block in Solidity?

- [ ] To define custom data types
- [x] To enable low-level, inline assembly code
- [ ] To group related functions within a contract
- [ ] To handle contract deployment
Answer: b. To enable low-level, inline assembly code

#### Q5. Which Solidity design pattern is used to reduce gas costs by avoiding redundant storage writes?

- [ ] Factory pattern
- [ ] State machine pattern
- [x] Proxy pattern
- [ ] Events pattern

#### Q6. In Solidity, what is the purpose of "function modifiers"?

- [ ] To specify the visibility of functions
- [ ] To enable function overloading
- [ ] To change the state of a contract
- [x] To change the behavior of functions

#### Q7. What is the primary advantage of using the "ERC-20" standard for token contracts in Solidity?

- [ ] It allows for faster block confirmations.
- [x] It provides a standardized interface for interoperability with other contracts.
- [ ] It enforces strict access control to token balances.
- [ ] It requires all tokens to be mined through proof-of-work.

#### Q8. In Solidity, what is "stack too deep" error, and how can it be addressed?

- [ ] It indicates a stack overflow and can be resolved by increasing the gas limit.
- [x] It occurs when there are too many variables in a single function and can be fixed by refactoring the code.
- [ ] It's a memory allocation issue that can be fixed by using "storage" instead of "memory."
- [ ] It's a known bug in the Solidity compiler and cannot be addressed.