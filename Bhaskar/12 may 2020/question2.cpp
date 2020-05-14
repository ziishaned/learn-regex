#include <stdio.h>
int main()
{
  int n, a[100], b[100], count = 0, c, d;

  printf("Enter number of elements in array\n");
  scanf("%d", &n);

  printf("Enter %d integers\n", n);

  for (c = 0; c < n; c++)
    scanf("%d", &a[c]);

  for (c = 0; c < n; c++)
  {
    for (d = 0; d < count; d++)
    {
      if(a[c] == b[d])
        break;
    }
    if (d == count)
    {
      b[count] = a[c];
      count++;
    }
  }

  printf("Array obtained after removing duplicate elements:\n");

  for (c = 0; c < count; c++)
    printf("%d\n", b[c]);

  return 0;
}
