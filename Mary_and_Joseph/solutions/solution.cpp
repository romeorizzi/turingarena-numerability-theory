#include<cassert>

int f(int n) {
  assert( n >= 0); 
  if(n % 2 == 0)
    return n+2;
  else
    return n;    
}

int f_inv(int n) {
  assert( n > 0); 
  if(n % 2 == 0)
    return n-2;
  else
    return n;    
}

int fixed_point_num(int index) {
  return 2*index +1;
}
