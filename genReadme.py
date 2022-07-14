headerBadges = """
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
"""
footerBadges = """
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
"""
cvm = """# CVM #

Chime Virtual Machine, is a project the aims to provide a simple VM for retro computers and homemade CPUs. This would allow people to program them in a higher level language.
"""


info = """
## Stacks ##
there are 7 stack in the machine  

```
Code=0
Frame=1
a=2
b=3
c=4
d=5
e=6
f=7
```

## loops ##

    loop (set up a true or false on stack) do

    (code to be ran here)

    endLoop
"""

from helper import help

with open("README.md", "w+") as file:
    sections = [headerBadges, cvm, help(), info, footerBadges]
    for section in sections:
        file.write(section)
        file.write("\n")

print("dont forget to format the doc")
