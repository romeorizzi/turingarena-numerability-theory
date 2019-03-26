#include<cassert>
static const int S = 1;
static const int R = -1;

int new_room_number(int n, int h) {
  assert(n >= 0);
  assert( (h==S) || (h==R) );
  if(h==S)
    return 2*n;
  return  2*n +1;
}
int former_hotel(int n) {
  assert(n >= 0);
  if(n%2 == 0)
    return S;
  return R;
}
int former_room(int n) {
  assert(n >= 0);
  if(n%2 == 0)
    return n/2;
  return (n-1)/2;
}
