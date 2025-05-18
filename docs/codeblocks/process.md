## Defining Processes
A script can be declared as a process by including the `PROCESS` header at the top of it. Process names can be given special characters using the same syntax as variables.
```tc
PROCESS ProcessName;
# code here
```

```tc
PROCESS ("process with special chars!!");
# code here
```

## Starting Processes
Processes can be started using the `start` keyword followed by the process' name. 

```tc
start ProcessName;
start ("process with special chars!!");
```

To change local variable and target behavior, use tags in the same way you would for any other action.

```tc
start gameLoop{"Target Mode" = "With no targets","Local Variables" = "Don't copy"};
```