#include <stdio.h>  // for printf()
#include <string.h> // for strlen()

// reverse the given null-terminated String in place
void inplace_reverse(char * str)
{
  if (str)
  {
    char * end = str + strlen(str) - 1;

    // swap the values in the two given variables
    // XXX: fails when a and b refer to same memory location
#   define XOR_SWAP(a,b) do\
    {\
      a ^= b;\
      b ^= a;\
      a ^= b;\
    } while (0)

    // walk inwards from both ends of the String, 
    // swapping until we get to the middle
    while (str < end)
    {
      XOR_SWAP(*str, *end);
      str++;
      end--;
    }
#   undef XOR_SWAP
  }
}

int main() {
    // Test the inplace_reverse function
    char test_str[] = "Hello World!";
    
    printf("Original string: %s\n", test_str);
    inplace_reverse(test_str);
    printf("Reversed string: %s\n", test_str);
    
    return 0;
}
