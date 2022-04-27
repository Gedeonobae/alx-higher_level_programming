# Web stack debugging #3

This was the fourth in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.

<h3>Concepts</h3>

For this project, students are expected to look at these concepts:

<ul>
<li><a href="https://alx-intranet.hbtn.io/concepts/17">Web Server</a></li>
<li><a href="https://alx-intranet.hbtn.io/concepts/68">Web stack debugging</a></li>
</ul>

<h2>Background Context</h2>

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png">


## Tasks :page_with_curl:

* **0. Strace is your friend**
  * [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp): Puppet manifest
  that fixes a typo error causing a WordPress application being served by an Apache
  web server to fail.
  * Usage: `puppet apply 0-strace_is_your_friend.pp`

