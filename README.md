[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# CVM

Chime Virtual Machine, is a project the aims to provide a simple VM for retro computers and homemade CPUs. This would allow people to program them in a higher level language.

## Commands

| functions  | args                   | description                                                                                          |
| ---------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| print      | ['String']             | prints out the top of the stack                                                                      |
| println    | ['String']             | prints out the top of the stack with a new line                                                      |
| string     | ['Integer']            | convert int to string on the top of the stack                                                        |
| input      | None                   | gets user input and stores it on top of the stack                                                    |
| add        | ['Integer', 'Integer'] | adds the top two ints and stores on top of stack                                                     |
| min        | ['Integer', 'Integer'] | subtracts the top two numbers                                                                        |
| clone      | ['any']                | duplicates the top of the stack                                                                      |
| swap       | ['Integer']            | takes the second frame and swaps it with index from the top of the stack                             |
| EQ         | ['Integer', 'Integer'] | tests that the top two values are equal puts a non zero value on the stack                           |
| LT         | ['Integer', 'Integer'] | tests that the top two values are less then puts a non zero value on the stack                       |
| GT         | ['Integer', 'Integer'] | tests that the top two values are grater then puts a non zero value on the stack                     |
| NT         | ['Integer', 'Integer'] | tests that the top two values are not equal puts a non zero value on the stack                       |
| True       | None                   | puts a non zerp ( True) value on the stack                                                           |
| False      | None                   | puts a zero value (false) on the stack                                                               |
| drop       | None                   | pops off the top of the stack                                                                        |
| dropx      | ['Integer']            | pops off the x frames off the stack                                                                  |
| if         | ['Boolean']            | if the top of the stack is a non zero number if true the code between the if and endif will run      |
| stackSize  | None                   | puts the size of the stack on top of the stack                                                       |
| sysCall    | ['String']             | None                                                                                                 |
| def        | None                   | defines a functions with the next token as the name and the following tokens till endDef as the code |
| func       | None                   | runs the function that is named after it                                                             |
| loop       | None                   | this will start a loop                                                                               |
| endLoop    | None                   | These should never be called,they should be handled by the opening call                              |
| endDef     | None                   | These should never be called,they should be handled by the opening call                              |
| endIf      | None                   | These should never be called,they should be handled by the opening call                              |
| swapStack  | ['Integer', 'Integer'] | swaps two stacks                                                                                     |
| cloneStack | ['Integer', 'Integer'] | clone one stack to another stacks (from to)                                                          |

## loops

    loop (set up a true or false on stack) do

    (code to be ran here)

    endLoop

## stacks

    Code=0
    the code stack holds the rest of the program that has yet to be ran
    Frame=1
    The Frame stack is where all the data is stored
    a=2
    b=3
    c=4
    d=5
    e=6
    f=7

[contributors-shield]: https://img.shields.io/github/contributors/himehowareu/CVM.svg?style=for-the-badge
[contributors-url]: https://github.com/himehowareu/CVM/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/himehowareu/CVM.svg?style=for-the-badge
[forks-url]: https://github.com/himehowareu/CVM/network/members
[stars-shield]: https://img.shields.io/github/stars/himehowareu/CVM.svg?style=for-the-badge
[stars-url]: https://github.com/himehowareu/CVM/stargazers
[issues-shield]: https://img.shields.io/github/issues/himehowareu/CVM.svg?style=for-the-badge
[issues-url]: https://github.com/himehowareu/CVM/issues
[license-shield]: https://img.shields.io/github/license/himehowareu/CVM.svg?style=for-the-badge
[license-url]: https://github.com/himehowareu/CVM/blob/master/LICENSE.txt
