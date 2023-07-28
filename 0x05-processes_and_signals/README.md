# C Programming and System Engineering DevOps
### 0x05. Processes and signals
---
`0x05-processes_and_signals`
---
`0x05-processes_and_signals`
> 0. What is my PID - a Bash script that displays its own PID
---
`1-list_your_processes`
> 1. List your processes - a Bash script that displays a list of currently running processes
---
`2-show_your_bash_pid`
> 2. Show your Bash PID - a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process
---
`3-show_your_bash_pid_made_easy`
> 3. Show your Bash PID made easy - a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash
---
`4-to_infinity_and_beyond`
> 4. To infinity and beyond - a Bash script that displays `To infinity and beyond` indefinitely
---
`5-dont_stop_me_now`
> 5. Don't stop me now! - a Bash script that stops `4-to_infinity_and_beyond` process
---
`6-stop_me_if_you_can`
> 6. Stop me if you can - a Bash script that stops `4-to_infinity_and_beyond` process
---
`7-highlander`
> 7. Highlander - a Bash script that displays:
> `To infinity and beyond` indefinitely
> With a `sleep 2` in between each iteration
> `I am invincible!!!` when receiving a `SIGTERM` signal
---
`8-beheaded_process`
> 8. Beheaded process - a Bash script that kills the process `7-highlander`
---
`100-process_and_pid_file`
> 9. Process and PID file - a Bash script that:
> Creates the file `/var/run/myscript.pid` containing its PID
> Displays `To infinity and beyond` indefinitely
> Displays `I hate the kill command` when receiving a `SIGTERM` signal
> Displays `Y U no love me?!` when receiving a `SIGINT` signal
> Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal
---
`101-manage_my_process`
> 10. Manage my process
---
`102-zombie.c`
> 11. Zombie -  a C program that creates 5 zombie processes
---
