            .data
list:       .word 0
counter:    .word 0

            .text

            # ask user for list size
            li      $v0, 5
            syscall
            add     $t0, $v0, $0

            # allocate list memory
            li      $t1, 4
            mul     $t0, $t1
            mflo    $t2
            add     $a0, $t2, $t1
            li      $v0, 9
            syscall
            sw      $v0, list
            sw      $t1, ($v0)

            # loop n times to add every item to list

            sw      $0, i

loop:       lw      $t0, i
            lw      $t1, list
            lw      $t2, ($t1)
            slt     $t3, $t0, $t1
            beq     $t3, $0, endloop

            # ask user for item
            li      $v0, 5
            syscall

            # manipulate list to get i-th item
            li      $t3, 4
            mult    $t3, $t0
            mflo    $t4
            add     $t4, $t4, $t3

            # $t4 = (4i + 4) + list address, which is $t1
            add     $t4, $t4, $t1

            # store the value
            sw      $v0, ($t4)

            # increment the counter
            addi    $t0, $t0, 1
            sw      $t0, i

            j       loop

endloop: # another loop print the list, or sum, or etc
