            .data
prompt:     .asciiz "Enter an int: "
msg:        .asciiz "Negative!"

            .text
            # print prompt
            la      $a0, prompt
            li      $v0, 4
            syscall

            # $v0 = input
            li      $v0, 5
            syscall

            # if 0 < $v0, jump to exit
            blt     $0, $v0, exit

            # print msg
            la      $a0, msg
            li      $v0, 4
            syscall

            # exit
exit:       li      $v0, 10
            syscall