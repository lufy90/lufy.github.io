#!/bin/bash
# filename: declare.sh
# Author: lufei
# Date: 20191126 15:48:42

testf(){
	declare -n a=$1
	echo "Before declaration of \$1: $a"
	AAA=aaa
	echo "After declaration of \$1: $a"
}



testf AAA
