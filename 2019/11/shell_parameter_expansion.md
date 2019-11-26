
[Bash Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Special-Parameters)

# ${parameter:-word}
* If parameter is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted. 
# ${parameter:=word}
* If parameter is unset or null, the expansion of word is assigned to parameter. The value of parameter is then substituted. Positional parameters and special parameters may not be assigned to in this way. 
# ${parameter:?word}
* If parameter is null or unset, the expansion of word (or a message to that effect if word is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.
# ${parameter:+word}
* If parameter is null or unset, nothing is substituted, otherwise the expansion of word is substituted.
# {parameter:offset}
# {parameter:offset:length}
* Get substring from $parameter
# ${!prefix*}
# ${!prefix@}
# ${!name[@]}
# ${!name[*]}
# ${#parameter}
* the length of value of $parameter. If parameter is '*' or '@', the value substituted is the number of positional parameters.
# ${parameter#word}
# ${parameter##word}
# ${parameter%word}
# ${parameter%%word}
# ${parameter/pattern/string}
# ${parameter^pattern}
# ${parameter^^pattern}
# ${parameter,pattern}
# ${parameter,,pattern}
# ${parameter@operator}
