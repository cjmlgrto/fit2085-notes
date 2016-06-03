            .data
str1:       .asciiz "Enter a number: "
str2:       .asciiz "Enter another number: "
str3:       .asciiz " + "
str4:       .asciiz " = "
var1:       .word 0
var2:       .word 0
var3:       .word 0

            .text

            # print str1
            la      $a0, str1
            li      $v0, 4
            syscall

            # read input as var1
            li      $v0, 5
            syscall
            sw      $v0, var1

            # print str2
            la      $a0, str2
            li      $v0, 4
            syscall

            # read input as var2
            li      $v0, 5
            syscall
            sw      $v0, var2

            # compute
            lw      $t0, var1
            lw      $t1, var2
            add     $t0, $t0, $t1
            sw      $50, var3

            # print results
            lw      $a0, var1
            li      $v0, 1
            syscall
            la      $a0, str3
            li      $v0, 4
            syscall
            lw      $a0, var2
            li      $v0, 1
            syscall
            la      $a0, str4
            li      $v0, 4
            syscall
            lw      $a0, var3
            li      $v0, 1
            syscall

            # exit
            li      $v0, 10
            syscall