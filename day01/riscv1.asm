.data
    filename:   .asciz "C:\\Users\\Nathan\\Documents\\advent2024\\day01\\example1.txt"
    buffer:     .space 200       # Increased buffer size
    list1:      .space 400       # Space for 100 integers (4 bytes each)
    list2:      .space 400       # Space for 100 integers (4 bytes each)
    result_str: .asciz "Total Difference: "
    error_str:  .asciz "File open error\n"

.text
.globl main

main:
    # Try to open file
    li a7, 1024       # open syscall
    la a0, filename   # filename
    li a1, 0          # read-only mode
    li a2, 0          # mode (ignored)
    ecall
    
    # Check for file open error
    bltz a0, file_error
    mv s0, a0         # save file descriptor

    # Initialize counters and pointers
    li s1, 0          # counter for number of lines
    la s2, list1      # pointer to list1
    la s3, list2      # pointer to list2

read_line:
    # Read a line
    li a7, 63         # read syscall
    mv a0, s0         # file descriptor
    la a1, buffer     # buffer address
    li a2, 200        # buffer size
    ecall

    # Check for end of file or read error
    blez a0, close_file

    # Process the line
    la t0, buffer     # load buffer address
    
    # Extract first number
    jal parse_number  # returns parsed number in a0
    sw a0, (s2)       # store in list1
    addi s2, s2, 4    # move list1 pointer

    # Skip space separator
    jal skip_spaces

    # Extract second number
    jal parse_number  # returns parsed number in a0
    sw a0, (s3)       # store in list2
    addi s3, s3, 4    # move list2 pointer

    # Increment line counter
    addi s1, s1, 1
    j read_line

file_error:
    # Print error message
    li a7, 4
    la a0, error_str
    ecall
    j exit

close_file:
    # Close file
    li a7, 57
    mv a0, s0
    ecall

    # Sort list1 - bubble sort
    la a0, list1
    mv a1, s1
    jal bubble_sort

    # Sort list2 - bubble sort
    la a0, list2
    mv a1, s1
    jal bubble_sort

    # Calculate total difference
    li t0, 0          # total_difference
    la s2, list1
    la s3, list2
    li t1, 0          # loop counter

difference_loop:
    beq t1, s1, print_result
    
    # Load sorted values
    lw t4, (s2)
    lw t5, (s3)

    # Calculate absolute difference
    sub t6, t4, t5
    bgez t6, positive_diff
    neg t6, t6

positive_diff:
    add t0, t0, t6    # add to total_difference

    # Move pointers and increment counter
    addi s2, s2, 4
    addi s3, s3, 4
    addi t1, t1, 1
    j difference_loop

print_result:
    # Print result string
    li a7, 4
    la a0, result_str
    ecall

    # Print total difference
    li a7, 1
    mv a0, t0
    ecall

exit:
    # Exit program
    li a7, 10
    ecall

# Helper function to parse number from string
parse_number:
    li t1, 0          # parsed number
    li t2, 10         # multiplication factor

parse_digit:
    lb t3, (t0)
    
    # Check if end of line or non-digit
    li t4, '0'
    blt t3, t4, parse_done
    li t4, '9'
    bgt t3, t4, parse_done

    # Convert digit
    addi t3, t3, -48  # ASCII to integer
    mul t1, t1, t2    # shift previous digits
    add t1, t1, t3    # add current digit

    addi t0, t0, 1    # move to next character
    j parse_digit

parse_done:
    mv a0, t1         # return parsed number
    ret

# Helper function to skip spaces
skip_spaces:
skip_space_loop:
    lb t3, (t0)
    li t4, ' '
    bne t3, t4, skip_space_done
    addi t0, t0, 1
    j skip_space_loop

skip_space_done:
    ret

# Bubble sort function
bubble_sort:
    mv t0, a0         # list base address
    mv t1, a1         # list length
    addi t1, t1, -1   # n-1 passes

outer_loop:
    beqz t1, sort_done
    mv t2, a0         # reset list base
    mv t3, t1         # inner loop counter

inner_loop:
    beqz t3, outer_loop_end
    lw t4, (t2)
    lw t5, 4(t2)
    ble t4, t5, no_swap
    
    # Swap elements
    sw t5, (t2)
    sw t4, 4(t2)

no_swap:
    addi t2, t2, 4
    addi t3, t3, -1
    j inner_loop

outer_loop_end:
    addi t1, t1, -1
    j outer_loop

sort_done:
    ret